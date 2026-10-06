# Failure Prediction AI - Technical Documentation

## 📋 Table of Contents

1. [System Overview](#system-overview)
2. [Architecture](#architecture)
3. [Data Sources & Integrations](#data-sources--integrations)
4. [Core Components](#core-components)
5. [API Integration](#api-integration)
6. [Scoring & Statistical Methods](#scoring--statistical-methods)
7. [Risk Classification](#risk-classification)
8. [Performance Optimization](#performance-optimization)
9. [Security Considerations](#security-considerations)
10. [Deployment Guide](#deployment-guide)

## 🎯 System Overview

The **Failure Prediction AI – Startup & Project Risk Analyzer** is a comprehensive, AI-driven decision-support platform built with Streamlit. The system evaluates startup ideas, business proposals, and hackathon projects to predict potential failure risks, output success probabilities, and generate agentic AI mitigation strategies.

### Key Features
- **Real-time Risk Scoring**: Evaluates Financial, Market, Technical, and Operational risks.
- **Agentic AI Workflows**: Utilizes LangGraph to process multi-step reasoning for strategic recommendations.
- **Dynamic Market Sizing**: AI-generated TAM, SAM, and SOM estimations based on industry and budget.
- **Automated SWOT Analysis**: Rule-based generation of Strengths, Weaknesses, Opportunities, and Threats.
- **Interactive Dashboard**: High-contrast, premium UI with real-time KPI tracking and data visualization.

### Technology Stack
- **Frontend/UI**: Streamlit (Python web framework)
- **AI Orchestration**: LangGraph, LangChain
- **LLM Provider**: Groq API (Llama 3 70B) / OpenAI compatible
- **Database**: Supabase (PostgreSQL)
- **Data Processing**: Pandas, Python Standard Library

## 🏗️ Architecture

### System Architecture Diagram
```text
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ User Interface  │    │  Risk & SWOT    │    │ External APIs   │
│ (app.py)        │◄──►│  Engines        │◄──►│ (Groq / OpenAI) │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Analytics       │    │ LangGraph Agent │    │ Cloud Database  │
│ Dashboard       │◄──►│ (Reasoning)     │◄──►│ (Supabase)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Component Breakdown

#### 1. Presentation Layer (`app.py`)
- Main application entry point with 4-tab navigation architecture.
- Handles user state management (`st.session_state`).
- Renders the Cyberpunk-themed UI and interactive charts.

#### 2. Risk & Assessment Engine (`risk_engine.py`, `swot_analysis.py`)
- Core mathematical processing for risk calculations.
- Evaluates categorical inputs to generate numerical 1-5 scale scores.
- Generates structural SWOT matrices.

#### 3. Agentic Workflow Layer (`recommendations_agent.py`)
- Implements LangGraph state machine.
- Passes project context, risks, and SWOT through a multi-node AI reasoning pipeline.
- Generates structured JSON outputs for Action Cards and Mitigations.

#### 4. Data Layer (`database.py`)
- Supabase client initialization.
- Handles insertion of new project profiles.
- Fetches the most recent queries for dashboard telemetry.

## 📊 Data Sources & Integrations

### Primary Integrations

#### Groq API (LLM Inference)
- **Endpoint**: `api.groq.com/openai/v1`
- **Model**: `llama3-70b-8192` (Fallback: `openai/gpt-oss-20b` depending on proxy)
- **Purpose**: Powering LangGraph reasoning and dynamic market analysis.
- **Reliability**: High speed, ultra-low latency inference.

#### Supabase (PostgreSQL)
- **Purpose**: Persistent storage of user-submitted project profiles (Name, Industry, Budget, Description).
- **Data Types**: Relational logs.

### Error Handling
- **Graceful Fallbacks**: If the Database connection fails, the dashboard automatically falls back to reading from local `st.session_state`.
- **Mock Data Injection**: If LLM API keys are missing, the system injects formatted mock JSON data to prevent UI crashes.

## 🔧 Core Components

### Risk Engine (`risk_engine.py`)

#### Key Methods
```python
def calculate_risk(market_comp, team_exp, resource_avail, innovation, market_res)
def get_risk_status(score)
def calculate_success_probability(score)
```

### LangGraph Agent (`recommendations_agent.py`)

#### Workflow Nodes
- `analyze_project`: Summarizes raw project text.
- `analyze_risks`: Contextualizes the numerical risk scores.
- `generate_recommendations`: Outputs high-priority Action Cards.
- `generate_mitigation`: Outputs granular preventive/contingency steps.

## 📈 Scoring & Statistical Methods

### Risk Calculation Formula
The Risk Engine assigns numerical weights to string categorizations (e.g., "High" = 5, "Low" = 1) across 5 primary vectors:
1. Market Risk
2. Financial Risk
3. Competition Risk
4. Technical Risk
5. Operational Risk

#### Overall Score Aggregation
```python
overall_score = (market_risk + financial_risk + comp_risk + tech_risk + op_risk) / 5.0
```

### Success Probability Calculation
An inverse relationship to the risk score, mapped to a 100% scale with a logarithmic penalty for extreme risk:
```python
success_probability = max(0, 100 - ((overall_score / 5.0) * 100) * penalty_modifier)
```

## ⚠️ Risk Classification

### Thresholds
```python
risk_thresholds = {
    'Low Risk': {'max_score': 2.0},
    'Moderate Risk': {'min_score': 2.1, 'max_score': 3.5},
    'High Risk': {'min_score': 3.6, 'max_score': 5.0}
}
```

### Dashboard Alerting
- **High Risk**: Triggers `st.error()` (Red UI indicators) and prioritizes "Critical" mitigation tags.
- **Moderate Risk**: Triggers `st.warning()` (Orange UI indicators).
- **Low Risk**: Triggers `st.success()` (Green UI indicators).

## ⚡ Performance Optimization

### Latency Reduction
- **Prompt Engineering constraints**: LLM responses are strictly constrained to raw JSON to eliminate parsing overhead and token waste.
- **Fast Inference**: Utilizing Groq's LPU infrastructure ensures the complex LangGraph multi-node workflow completes in < 5 seconds.

### State Management
- Utilizing Streamlit's `st.session_state` prevents re-triggering the LLM or Database API when the user switches tabs, caching the `agent_result` locally.

## 🔒 Security Considerations

### Environment Variables
```python
# .env file structure - NEVER committed to version control
GROQ_API_KEY="your_api_key_here"
SUPABASE_URL="your_supabase_url"
SUPABASE_KEY="your_supabase_key"
```

### Data Security
- **No PII Storage**: The system does not request or store Personally Identifiable Information.
- **Read/Write Limitations**: Database queries are limited strictly to `insert()` and `limit(1)` fetching to prevent scraping.
- **Sanitized Outputs**: LLM outputs are wrapped in secure HTML markdown rendering (`unsafe_allow_html=True` is only used for structural divs, not executing scripts).

## 🚀 Deployment Guide

### Requirements
- **Python**: 3.9+
- **Dependencies**: See `requirements.txt` (Streamlit, LangChain, LangGraph, Supabase)

### Environment Setup
```bash
# Clone repository
git clone <repo_url>
cd ML_Market_Intelligence_Project

# Install dependencies
pip install -r requirements.txt

# Create environment file
touch .env
# Add API keys to .env
```

### Deployment Options

#### Streamlit Cloud (Recommended)
1. Push code to a public/private GitHub repository.
2. Connect repository to Streamlit Community Cloud.
3. Add `GROQ_API_KEY`, `SUPABASE_URL`, and `SUPABASE_KEY` to the Streamlit Secrets manager.
4. Deploy.

#### Local Execution
```bash
streamlit run app.py
```

---

## 📞 Support

### Technical Maintenance
- **System Logs**: Checked via standard stdout Streamlit logs.
- **Database Administration**: Handled via the Supabase Web Console.
- **Model Upgrades**: Changing the LLM model requires updating the string literal inside `recommendations_agent.py` and `market_analysis.py`.
