# Gemini Integration for Video Analysis

This guide explains how to use Google Gemini to analyze the Designer First Steps YouTube videos directly, providing detailed answers about specific techniques, parameters, and workflows shown in the course.

---

## Overview

Gemini can analyze YouTube videos in real-time and answer questions about their content. This is particularly useful for:

- Getting specific parameter values shown in videos
- Understanding WHY certain settings are used
- Clarifying techniques that may be hard to follow
- Extracting step-by-step workflows from video demonstrations

---

## Prerequisites

1. **Google Account** with access to Gemini Pro
2. **Chrome Browser** with Claude Code extension (for automation)
3. **Access to the Substance Designer Beginner Course Gem**

### Gemini Conversation URL

The existing Gemini conversation with course context:
```
https://gemini.google.com/app/af593c9b8450255c
```

This conversation is set up as a "Gem" (custom Gemini assistant) that has context about the entire Designer First Steps course.

---

## How Gemini Analyzes YouTube Videos

When you ask a question about a specific video or topic:

1. Gemini identifies the relevant video(s) from the course playlist
2. It shows "Focusing on [topic]" while analyzing the video
3. It extracts specific information including:
   - Parameter values and settings
   - Node names and connections
   - Step-by-step procedures
   - Explanations of WHY each step is taken

---

## Query Workflow

### Method 1: Direct Browser Automation

Use Claude Code's browser tools to interact with Gemini:

```
1. Navigate to the Gemini conversation URL
2. Click on the input field
3. Type your question
4. Press Enter
5. Wait for response (may take 5-10 seconds for video analysis)
6. Read and extract the information
```

### Method 2: Manual Query

1. Open Chrome and go to: `https://gemini.google.com/app/af593c9b8450255c`
2. Type your question in the "Ask Gemini" input
3. Wait for the response
4. Copy relevant information to your notes

---

## Effective Query Patterns

### For Specific Parameters

```
In Part [X] about [topic], what are the exact parameter values for the [Node Name] node?
```

**Example:**
```
In Part 9 about fabric embroidery, what are the key parameters for the Tile Sampler node when adding ornaments?
```

**Response includes:**
- Pattern: "Pattern Input"
- Instance Parameters (X/Y Amount): X: 600, Y: 700
- Size (Scale): 3.8
- Rotation: 90 Degrees
- Offset: 0.5 (Staggered)
- Scale Map Input: Connected to ornament mask
- Scale Map Multiplier: Enabled

### For Workflow Steps

```
What are the step-by-step instructions for [technique] shown in Part [X]?
```

**Example:**
```
What are the step-by-step instructions for creating the diamond gemstone shape in Part 13?
```

### For Troubleshooting

```
In Part [X], how does the instructor fix the problem with [issue]?
```

**Example:**
```
In Part 16, how does the instructor fix the vertical gradient artifact in the Curvature Smooth node?
```

### For Concept Explanations

```
Can you explain the concept of [topic] as discussed in the tutorial series?
```

**Example:**
```
Can you explain the concept of inheritance in Substance Designer as discussed in Part 11?
```

---

## Browser Automation Code

### Navigate and Query Gemini

```javascript
// Using Claude Code browser tools

// 1. Get tab context
const tabs = await mcp__claude-in-chrome__tabs_context_mcp();

// 2. Create new tab or use existing
const tabId = await mcp__claude-in-chrome__tabs_create_mcp();

// 3. Navigate to Gemini
await mcp__claude-in-chrome__navigate({
  url: "https://gemini.google.com/app/af593c9b8450255c",
  tabId: tabId
});

// 4. Wait for page load
await mcp__claude-in-chrome__computer({
  action: "wait",
  duration: 3,
  tabId: tabId
});

// 5. Find and click input field
const input = await mcp__claude-in-chrome__find({
  query: "Ask Gemini input field",
  tabId: tabId
});

await mcp__claude-in-chrome__computer({
  action: "left_click",
  ref: input.ref,
  tabId: tabId
});

// 6. Type question
await mcp__claude-in-chrome__computer({
  action: "type",
  text: "Your question here",
  tabId: tabId
});

// 7. Submit
await mcp__claude-in-chrome__computer({
  action: "key",
  text: "Return",
  tabId: tabId
});

// 8. Wait for response
await mcp__claude-in-chrome__computer({
  action: "wait",
  duration: 8,
  tabId: tabId
});

// 9. Take screenshot or read page
await mcp__claude-in-chrome__computer({
  action: "screenshot",
  tabId: tabId
});
```

---

## Video Reference by Part

| Part | Topic | Best Questions |
|------|-------|----------------|
| 1 | What is SD | "What is the difference between Designer and Painter?" |
| 2 | Making Materials | "What is the height-first workflow?" |
| 3 | Interface | "What are the main panels in the interface?" |
| 4 | First Project | "How do you set up the Base Material node?" |
| 5 | Thread | "What are the Fibers node parameters for thread creation?" |
| 6 | Weaving | "How do warp and weft threads interweave?" |
| 7 | Shapes | "How do you create curves with the Spline node?" |
| 8 | Importing | "What's the difference between Import and Link?" |
| 9 | Embroidery | "What Tile Sampler settings create the embroidery effect?" |
| 10 | Custom Shapes | "How do you create the loop trim element?" |
| 11 | Inheritance | "How does inheritance work with Blend nodes?" |
| 12 | Placement | "How do you tile trim elements vertically?" |
| 13 | Gemstones | "What are the three methods to create a diamond shape?" |
| 14 | Masks | "How do you use Dot node portals for masks?" |
| 15 | Imperfections | "How do you create the lip/border effect?" |
| 16 | Colors | "How do you fix the Curvature Smooth vertical artifact?" |
| 17 | Roughness/Metal | "Why invert the curvature for roughness?" |
| 18 | Displacement | "Why blur the displacement input?" |
| 19 | Parameters | "How do you expose parameters with visible_if?" |
| 20 | Presets | "How do you link parameters across multiple nodes?" |
| 21 | Export | "How do you set up automatic export?" |

---

## Response Quality Tips

### Get Better Responses

1. **Reference specific Part numbers** - Gemini knows the course structure
2. **Name the specific node** - More precise than general terms
3. **Ask "why"** - Gets explanations, not just values
4. **Ask about troubleshooting** - Gemini extracts error-fixing steps

### Verify Information

Gemini's responses are based on video analysis and may occasionally misinterpret visuals. Cross-reference with:
- Transcripts in `sources/transcripts/`
- Node parameters in `references/node-parameters.md`
- The actual Ornate_Fabric.sbs project

---

## Integration with Tutor Skill

### When to Use Gemini

1. **Clarifying video-specific details** not captured in transcripts
2. **Visual parameters** shown but not spoken in videos
3. **Step-by-step breakdowns** of complex sequences
4. **Cross-referencing** between different parts

### Workflow: Tutor + Gemini

1. User asks question
2. Tutor checks local knowledge (SKILL.md, transcripts, references)
3. If need video-specific detail:
   - Query Gemini with browser automation
   - Extract relevant information
   - Combine with local knowledge
4. Provide comprehensive answer

---

## Limitations

- **Requires Google account** with Gemini access
- **Network dependent** - needs internet connection
- **Rate limits** - excessive queries may be throttled
- **Video analysis time** - responses take 5-10 seconds
- **Visual interpretation** - may misread some on-screen values

---

## Gemini Conversation Context

The Substance 3D Designer Beginner Course Gem has been pre-configured with:

- Knowledge of all 22 parts of the course
- Playlist links and video structure
- Understanding of the Ornate_Fabric project
- Context about PBR workflows and node-based design

This context persists across queries, allowing for follow-up questions and deeper exploration of topics.
