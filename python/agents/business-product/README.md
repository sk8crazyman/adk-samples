# Business Product Planner

This sample demonstrates a two-stage workflow using the Agent Development Kit. A Business Analyst agent gathers product requirements from the user. When the requirements are complete, it delegates the conversation to a Product Manager agent which proposes a technology stack and a short Product Requirements Document (PRD).

## Setup and Installation

1. **Prerequisites**
   - Python 3.11+
   - [Poetry](https://python-poetry.org/docs/) for dependency management
   - Access to Google Vertex AI or a Gemini API key

2. **Installation**
```bash
# From the repository root
cd python/agents/business-product
poetry install
```

3. **Configuration**
   - Copy `.env.example` to `.env` and fill in the required values or export the following variables:
```bash
export GOOGLE_GENAI_USE_VERTEXAI=true
export GOOGLE_CLOUD_PROJECT=<your-project-id>
export GOOGLE_CLOUD_LOCATION=<your-location>
```

## Running the Agent
Run the agent using the ADK CLI:
```bash
adk run business_product
```
You can also start the web UI using `adk web` and selecting `business_product` from the dropdown.

## Example Interaction
```
User: I need an app for ordering food at concerts.
Agent: Great! Let's gather some details. Who will use the app and what are the key features you need?
...
User: That's everything.
Agent: Here is a summary of the requirements. [ProductManager] tool reported: <PRD and tech stack>
```
