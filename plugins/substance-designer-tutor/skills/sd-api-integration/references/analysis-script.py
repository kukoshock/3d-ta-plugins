#!/usr/bin/env python3
"""
SBS File Analyzer
=================

Comprehensive analysis tool for Substance Designer .sbs files.
Extracts structure, parameters, and detects potential issues.

Usage:
    python analysis-script.py <path-to-sbs-file> [--output json|text]

Requirements:
    - pysbs (Substance Automation Toolkit)
    - Python 3.7+

Installation:
    pip install substance-automation-toolkit

    OR use Designer's Python environment:
    Windows: C:\\Program Files\\Adobe\\Adobe Substance 3D Designer\\resources\\python-packages
    macOS: /Applications/Adobe Substance 3D Designer.app/Contents/Resources/python-packages

Author: Substance Designer Tutor Plugin
"""

import sys
import json
from pathlib import Path
from typing import Dict, List, Set, Any
import xml.etree.ElementTree as ET

# Try to import pysbs, but fall back to XML parsing if unavailable
PYSBS_AVAILABLE = False
try:
    from pysbs import context, SBSDocument
    PYSBS_AVAILABLE = True
except ImportError:
    print("INFO: pysbs not available, using XML parsing fallback")
    print("For full capabilities, install: pip install substance-automation-toolkit")
    print()


class SBSAnalyzer:
    """Analyzes .sbs files and detects issues"""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.use_pysbs = PYSBS_AVAILABLE
        if self.use_pysbs:
            self.ctx = context.Context()
            self.doc = None
        else:
            self.tree = None
            self.root = None
        self.results = {
            "file": filepath,
            "graphs": [],
            "dependencies": [],
            "issues": []
        }

    def load_document(self) -> bool:
        """Load .sbs document"""
        try:
            if self.use_pysbs:
                self.doc = SBSDocument(self.ctx, self.filepath)
            else:
                self.tree = ET.parse(self.filepath)
                self.root = self.tree.getroot()
            return True
        except FileNotFoundError:
            print(f"ERROR: File not found: {self.filepath}")
            return False
        except Exception as e:
            print(f"ERROR loading document: {e}")
            return False

    def analyze(self) -> Dict[str, Any]:
        """Run complete analysis"""
        if not self.load_document():
            return self.results

        if self.use_pysbs:
            return self._analyze_with_pysbs()
        else:
            return self._analyze_with_xml()

    def _analyze_with_pysbs(self) -> Dict[str, Any]:
        """Analyze using pysbs API"""
        # Extract dependencies
        self._extract_dependencies()

        # Analyze each graph
        for graph in self.doc.getGraphs():
            graph_data = self._analyze_graph(graph)
            self.results["graphs"].append(graph_data)

        return self.results

    def _analyze_with_xml(self) -> Dict[str, Any]:
        """Analyze using XML parsing"""
        # Extract dependencies
        deps = self.root.findall('.//dependency')
        for dep in deps:
            filename = dep.find('filename')
            uid = dep.find('uid')
            if filename is not None and uid is not None:
                self.results["dependencies"].append({
                    "filename": filename.get('v'),
                    "uid": uid.get('v')
                })

        # Analyze each graph
        graphs = self.root.findall('.//content/graph')
        for graph in graphs:
            graph_data = self._analyze_graph_xml(graph)
            self.results["graphs"].append(graph_data)

        return self.results

    def _analyze_graph_xml(self, graph) -> Dict[str, Any]:
        """Analyze single graph using XML"""
        graph_id_elem = graph.find('identifier')
        graph_id = graph_id_elem.get('v') if graph_id_elem is not None else "unknown"

        graph_data = {
            "identifier": graph_id,
            "node_count": 0,
            "connection_count": 0,
            "output_count": 0,
            "node_types": {},
            "outputs": [],
            "issues": []
        }

        # Count nodes
        nodes_elem = graph.find('compNodes')
        if nodes_elem is not None:
            nodes = nodes_elem.findall('compNode')
            graph_data["node_count"] = len(nodes)

            # Count node types
            for node in nodes:
                impl = node.find('.//compImplementation/compInstance/path')
                if impl is not None:
                    path = impl.get('v', '')
                    if 'pkg:///' in path:
                        node_type = path.split('pkg:///')[1].split('?')[0]
                        graph_data["node_types"][node_type] = \
                            graph_data["node_types"].get(node_type, 0) + 1

            # Check for 8-bit issues
            graph_data["issues"].extend(self._detect_8bit_xml(nodes_elem))

        # Count connections
        conns_elem = graph.find('connections')
        if conns_elem is not None:
            connections = conns_elem.findall('connection')
            graph_data["connection_count"] = len(connections)

        # Analyze outputs
        outputs_elem = graph.find('graphOutputs')
        if outputs_elem is not None:
            outputs = outputs_elem.findall('graphoutput')
            graph_data["output_count"] = len(outputs)
            for output in outputs:
                out_id = output.find('identifier')
                if out_id is not None:
                    graph_data["outputs"].append({
                        "uid": output.find('uid').get('v') if output.find('uid') is not None else "unknown",
                        "identifier": out_id.get('v')
                    })

        return graph_data

    def _detect_8bit_xml(self, nodes_elem) -> List[Dict[str, Any]]:
        """Detect 8-bit nodes using XML"""
        issues = []
        for node in nodes_elem.findall('compNode'):
            uid_elem = node.find('uid')
            params = node.find('parameters')
            if params is not None:
                for param in params.findall('parameter'):
                    name_elem = param.find('name')
                    if name_elem is not None and name_elem.get('v') == 'outputformat':
                        value_elem = param.find('.//int')
                        if value_elem is not None:
                            value = int(value_elem.get('v'))
                            if value == 0:  # 8-bit
                                issues.append({
                                    "node": uid_elem.get('v') if uid_elem is not None else "unknown",
                                    "type": "unknown",
                                    "rule": "8bit_output_format",
                                    "severity": "high",
                                    "message": "Node using 8-bit output (risk of banding)",
                                    "recommendation": "Set to 16-bit Absolute to prevent precision loss"
                                })
        return issues

    def _extract_dependencies(self):
        """Extract external .sbs dependencies"""
        deps = self.doc.getDependencies()
        for dep in deps:
            self.results["dependencies"].append({
                "filename": dep.mFilePath,
                "uid": str(dep.mUid)
            })

    def _analyze_graph(self, graph) -> Dict[str, Any]:
        """Analyze single graph"""
        graph_data = {
            "identifier": graph.mIdentifier,
            "node_count": 0,
            "connection_count": 0,
            "output_count": 0,
            "node_types": {},
            "outputs": [],
            "issues": []
        }

        # Count nodes
        nodes = graph.getAllNodes()
        graph_data["node_count"] = len(nodes)

        # Count connections
        connections = graph.getConnections()
        graph_data["connection_count"] = len(connections)

        # Analyze outputs
        outputs = graph.getAllOutputNodes()
        graph_data["output_count"] = len(outputs)
        for output in outputs:
            output_info = {
                "uid": output.getUid(),
                "identifier": getattr(output, 'mIdentifier', 'unknown')
            }
            graph_data["outputs"].append(output_info)

        # Count node types
        for node in nodes:
            node_type = node.getCompImplementation().mDefinition.mId
            graph_data["node_types"][node_type] = \
                graph_data["node_types"].get(node_type, 0) + 1

        # Run diagnostics
        graph_data["issues"].extend(self._detect_8bit_inheritance(graph))
        graph_data["issues"].extend(self._detect_missing_scale_maps(graph))
        graph_data["issues"].extend(self._detect_disconnected_outputs(graph))
        graph_data["issues"].extend(self._detect_orphaned_nodes(graph))

        return graph_data

    def _detect_8bit_inheritance(self, graph) -> List[Dict[str, Any]]:
        """Detect nodes using 8-bit output format"""
        issues = []

        for node in graph.getAllNodes():
            uid = node.getUid()
            node_type = node.getCompImplementation().mDefinition.mId

            for param in node.getParameters():
                if param.mId in ["outputformat", "output_format"]:
                    if hasattr(param.mValue, 'mValue'):
                        value = param.mValue.mValue
                        # 0 = 8-bit, 1 = 16-bit
                        if value == 0:
                            issues.append({
                                "node": uid,
                                "type": node_type,
                                "rule": "8bit_output_format",
                                "severity": "high",
                                "message": "Node using 8-bit output (risk of banding)",
                                "recommendation": "Set to 16-bit Absolute to prevent precision loss"
                            })

        return issues

    def _detect_missing_scale_maps(self, graph) -> List[Dict[str, Any]]:
        """Detect Tile Sampler nodes without scale maps"""
        issues = []

        for node in graph.getAllNodes():
            node_type = node.getCompImplementation().mDefinition.mId

            if node_type == "tile_sampler":
                uid = node.getUid()

                # Check if scale_map input is connected
                incoming = graph.getConnectionsToNode(node)
                has_scale_map = any(
                    "scale" in conn.getTargetInputIdentifier().lower()
                    for conn in incoming
                )

                if not has_scale_map:
                    issues.append({
                        "node": uid,
                        "type": node_type,
                        "rule": "tile_sampler_no_scale_map",
                        "severity": "medium",
                        "message": "Tile Sampler without scale map variation",
                        "recommendation": "Connect Perlin Noise to Scale Map for organic size variation"
                    })

        return issues

    def _detect_disconnected_outputs(self, graph) -> List[Dict[str, Any]]:
        """Detect output nodes with no input connections"""
        issues = []

        for output in graph.getAllOutputNodes():
            uid = output.getUid()
            incoming = graph.getConnectionsToNode(output)

            if not incoming:
                issues.append({
                    "node": uid,
                    "type": "output",
                    "rule": "disconnected_output",
                    "severity": "high",
                    "message": "Output node has no input connection",
                    "recommendation": "Connect a source node to this output"
                })

        return issues

    def _detect_orphaned_nodes(self, graph) -> List[Dict[str, Any]]:
        """Detect nodes not connected to any output"""
        # Get all node UIDs
        all_nodes = {node.getUid() for node in graph.getAllNodes()}

        # Trace from all outputs
        connected = set()
        for output in graph.getAllOutputNodes():
            deps = self._trace_upstream(graph, output.getUid())
            connected.update(deps)

        # Find unconnected
        orphaned = all_nodes - connected

        if orphaned:
            return [{
                "rule": "orphaned_nodes",
                "severity": "low",
                "message": f"Found {len(orphaned)} nodes not connected to any output",
                "nodes": list(orphaned),
                "recommendation": "Review and remove unused nodes or connect to outputs"
            }]

        return []

    def _trace_upstream(self, graph, node_uid: str, visited: Set[str] = None) -> Set[str]:
        """Recursively trace upstream dependencies"""
        if visited is None:
            visited = set()

        if node_uid in visited:
            return visited

        visited.add(node_uid)

        node = graph.getNodeFromUid(node_uid)
        if not node:
            return visited

        incoming = graph.getConnectionsToNode(node)
        for conn in incoming:
            source_uid = conn.getSourceNodeUID()
            self._trace_upstream(graph, source_uid, visited)

        return visited


def format_text_output(results: Dict[str, Any]) -> str:
    """Format results as human-readable text"""
    output = []
    output.append("=" * 70)
    output.append(f"SBS Analysis Report: {results['file']}")
    output.append("=" * 70)

    # Dependencies
    if results['dependencies']:
        output.append(f"\nDependencies ({len(results['dependencies'])}):")
        for dep in results['dependencies']:
            output.append(f"  - {dep['filename']}")

    # Graphs
    for graph in results['graphs']:
        output.append(f"\n{'=' * 70}")
        output.append(f"Graph: {graph['identifier']}")
        output.append(f"{'=' * 70}")
        output.append(f"Nodes: {graph['node_count']}")
        output.append(f"Connections: {graph['connection_count']}")
        output.append(f"Outputs: {graph['output_count']}")

        # Output details
        if graph['outputs']:
            output.append(f"\nOutput Nodes:")
            for out in graph['outputs']:
                output.append(f"  - {out['identifier']} ({out['uid']})")

        # Node type distribution
        output.append(f"\nNode Types:")
        for node_type, count in sorted(graph['node_types'].items(),
                                      key=lambda x: x[1], reverse=True):
            output.append(f"  {node_type}: {count}")

        # Issues
        if graph['issues']:
            output.append(f"\nIssues Detected ({len(graph['issues'])}):")
            for issue in graph['issues']:
                severity = issue['severity'].upper()
                output.append(f"\n  [{severity}] {issue['rule']}")
                if 'node' in issue:
                    output.append(f"    Node: {issue['node']}")
                output.append(f"    {issue['message']}")
                output.append(f"    Fix: {issue['recommendation']}")
        else:
            output.append("\n[OK] No issues detected")

    return "\n".join(output)


def format_json_output(results: Dict[str, Any]) -> str:
    """Format results as JSON"""
    return json.dumps(results, indent=2)


def main():
    """Main entry point"""
    # Parse arguments
    if len(sys.argv) < 2:
        print("Usage: python analysis-script.py <path-to-sbs-file> [--output json|text]")
        print("\nExample:")
        print("  python analysis-script.py material.sbs")
        print("  python analysis-script.py material.sbs --output json")
        sys.exit(1)

    filepath = sys.argv[1]
    output_format = "text"  # default

    if len(sys.argv) > 2:
        if sys.argv[2] == "--output" and len(sys.argv) > 3:
            output_format = sys.argv[3]

    # Validate file exists
    if not Path(filepath).exists():
        print(f"ERROR: File not found: {filepath}")
        sys.exit(1)

    # Run analysis
    analyzer = SBSAnalyzer(filepath)
    results = analyzer.analyze()

    # Format and print output
    if output_format == "json":
        print(format_json_output(results))
    else:
        print(format_text_output(results))


if __name__ == "__main__":
    main()
