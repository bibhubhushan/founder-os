# Agent Frameworks — Comparison

**Added:** 2025-02-15
**Source:** Research + experience
**Added by:** Aria

## Quick Reference

| Framework | Best For | Language | Complexity |
|-----------|---------|----------|-----------|
| **LangChain/LangGraph** | Complex chains, graph workflows | Python/JS | High |
| **CrewAI** | Multi-agent teams with roles | Python | Medium |
| **AutoGen** | Multi-agent conversation | Python | Medium |
| **OpenAI Agents SDK** | OpenAI tool-use agents | Python | Low |
| **Claude Agent SDK** | Claude tool-use agents | Python | Low |
| **DSPy** | Prompt optimization, pipelines | Python | High |
| **Smolagents** | Lightweight agents | Python | Low |
| **Semantic Kernel** | Enterprise, .NET/Python | C#/Python | Medium |

## When to Use What

- **Just need an agent that uses tools** → OpenAI or Claude SDK (simplest)
- **Need agents talking to each other** → CrewAI or AutoGen
- **Need complex workflows with branching** → LangGraph
- **Need to optimize prompts automatically** → DSPy
- **Building for enterprise** → Semantic Kernel

## Key Insight

Most projects don't need a framework. A well-structured prompt + tool calling is enough for 80% of use cases. Only reach for frameworks when you hit real limitations.
