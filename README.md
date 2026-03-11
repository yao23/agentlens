# AgentLens

Observability for AI Agents.

AI agents execute commands, call APIs, and spend tokens — but most teams have no visibility into what is happening.

AgentLens provides simple logging and cost tracking for AI agents like OpenClaw, LangChain, and AutoGen.

## Features

- Token usage tracking
- Agent action logging
- Cost analysis
- Lightweight Python SDK

## Install

pip install agentlens

## Example

from agentlens.monitor import monitor

monitor.action("api_call", "openai.chat.completions")

monitor.tokens(
    model="gpt-4o",
    tokens=1200,
    cost=0.03
)

## Roadmap

- dashboard
- prompt injection detection
- security scanning
- RBAC and governance
