# Exact Match Auto-Reply Plugin  
astrbot_plugin_exact_match

**AstrBot plugin for exact match auto-replies. Supports one-to-one matching between custom keywords and responses.**

### Features
- **Exact match triggering** – Prevents substring false triggers (e.g., configuring "hello" won't respond to "hello there")
- **Multiple rules** – Configure multiple keyword-response pairs simultaneously  
- **@ mention compatible** – Correctly handles messages where the bot is mentioned


### Configuration

- **Trigger Words** – Keywords that trigger replies, one per line (default: `["hello", "help"]`)
- **Responses** – Corresponding replies for each trigger, one per line (default: `["Hi there!", "This is an exact match plugin"]`)

**Note**: The two lists must correspond line-by-line. The first trigger maps to the first response, and so on.

### Usage Example

**Config:**
- Triggers: `["test", "help"]`
- Responses: `["pass", "help document\nv1.0\nthis is a bot"]`

**Conversation:**
```
User: test
Bot: pass

User: help
Bot: help document
v1.0
this is a bot

User: Test
Bot: (Falls back to LLM or no response)

User: help me!!!
Bot: (Falls back to LLM or no response)
```