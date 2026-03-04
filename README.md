# Intent-Based LLM Orchestrator

A modular **multi-expert LLM orchestration system** that analyzes a user's prompt and dynamically routes it to the most suitable specialized model.

Instead of relying on a single model for every task, this project demonstrates a **routing-based architecture** where different models handle different types of problems.

The system uses **OpenRouter** to access multiple models through a unified API.

---

## Overview

Large Language Models are strong generalists, but different models perform better at different tasks.

This project implements a **prompt routing mechanism** that:

1. Analyzes the user's intent  
2. Selects the most appropriate expert model  
3. Sends the request to that model  
4. Returns the generated response  

---

## Architecture

```
User Prompt
      ↓
Intent Routing Model
      ↓
Expert Selection
      ↓
Specialized LLM
      ↓
Response Generation
```

The router evaluates the task requirements and selects the expert most likely to produce the best response.

---

## Available Experts

The system contains multiple expert categories:

| Expert | Purpose |
|------|------|
| **general** | Everyday questions and simple explanations |
| **coding** | Programming help, debugging, algorithms |
| **reasoning** | Logical analysis and step-by-step thinking |
| **research** | Fact-based queries and information retrieval |
| **creative** | Storytelling, writing, creative tasks |
| **math** | Equations, calculations, symbolic reasoning |
| **analysis** | Comparisons, evaluations, trade-offs |
| **fallback** | Used when no category clearly applies |

Each expert maps to a specific **LLM optimized for that task.**

---

## Routing Logic

The router determines the expert by evaluating:

- Whether the prompt requires **technical code generation**
- Whether it requires **logical reasoning**
- Whether it needs **factual or real-time information**
- Whether it involves **creative writing**
- Whether it requires **mathematical calculations**
- Whether it asks for **structured comparison or analysis**

The routing model outputs a structured JSON response:

```json
{
  "selected_expert": "expert_name"
}
```

---

## Example

**User Prompt**

```
Solve 145 × 27 step by step
```

**Router Output**

```json
{
  "selected_expert": "math"
}
```

The request is then forwarded to the **math-optimized model**.

---

## Tech Stack

- Python
- OpenRouter API
- Multiple LLM providers
- Requests library

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/intent-based-llm-orchestrator.git
cd intent-based-llm-orchestrator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file or export your API key:

```
OPENROUTER_API_KEY=your_api_key_here
```

Never commit API keys to a public repository.

---

## Running the Project

```bash
python main.py
```

Example interaction:

```
You: Compare centralized and decentralized systems
```

The router will select the appropriate expert and generate a response.

---

## Project Purpose

This project demonstrates **LLM orchestration**, where multiple specialized models collaborate through routing logic to improve response quality.

It explores **AI system design concepts** such as:

- model routing
- task specialization
- prompt orchestration
- multi-model architectures

---

## Possible Improvements

Future enhancements could include:

- confidence scoring for routing decisions  
- multi-expert collaboration  
- response streaming  
- query caching  
- evaluation metrics for routing accuracy  
- FastAPI backend  
- web interface for routing visualization  

---

## License

MIT License
