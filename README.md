Intent-Based LLM Orchestrator

A modular multi-expert LLM orchestration system that analyzes a user's prompt and dynamically routes it to the most suitable specialized model.
The system uses intent detection to decide which expert model (reasoning, coding, math, research, etc.) should generate the response.

Instead of relying on a single LLM for every task, this project demonstrates a routing-based architecture where different models handle different types of problems.

---

Overview

Large Language Models are strong generalists, but different models perform better at different tasks.
This project implements a prompt routing mechanism that:

1. Analyzes the user's intent
2. Selects the most appropriate expert model
3. Sends the request to that model
4. Returns the generated response

The system uses OpenRouter to access multiple models through a unified API.

---

Architecture

User Prompt
↓
Intent Routing Model
↓
Expert Selection
↓
Specialized LLM
↓
Response Generation

The router evaluates the task requirements and chooses the expert most likely to produce the best response.

---

Available Experts

The system includes multiple expert categories:

- general – everyday questions and simple explanations
- coding – programming help, debugging, algorithms
- reasoning – logical analysis and step-by-step thinking
- research – factual queries and information retrieval
- creative – storytelling, writing, and creative tasks
- math – equations, calculations, symbolic reasoning
- analysis – comparisons, critical evaluation, trade-offs
- fallback – used if no clear category is detected

Each expert maps to a specific LLM optimized for that task.

---

Routing Logic

The router determines the expert by evaluating:

- Whether the prompt requires technical code generation
- Whether it needs logical reasoning
- Whether it requires factual information
- Whether it involves creative writing
- Whether it contains mathematical calculations
- Whether it asks for structured analysis or comparison

The routing model outputs a JSON object specifying the selected expert.

---

Example

User Prompt:

Solve 145 × 27 step by step

Router Decision:

{
  "selected_expert": "math"
}

The request is then forwarded to the math-optimized model.

---

Tech Stack

- Python
- OpenRouter API
- Multiple LLMs
- Requests library

---

Installation

Clone the repository:

git clone https://github.com/yourusername/intent-based-llm-orchestrator.git
cd intent-based-llm-orchestrator

Install dependencies:

pip install -r requirements.txt

---

Environment Variables

Create a ".env" file or export your API key:

OPENROUTER_API_KEY=your_api_key_here

Never commit API keys to the repository.

---

Running the Project

python main.py

Then enter your prompt in the terminal.

Example:

You: Compare centralized and decentralized systems

The router will select the appropriate expert and generate a response.

---

Project Purpose

This project demonstrates the concept of LLM orchestration, where multiple models collaborate through routing logic to improve response quality.

It is intended as a learning project exploring AI system design and prompt routing architectures.

---

Possible Improvements

Future extensions could include:

- confidence scoring for expert selection
- multi-expert collaboration
- streaming responses
- caching frequent queries
- evaluation metrics for routing accuracy
- API interface using FastAPI
- UI dashboard for routing visualization

---

License

MIT License
