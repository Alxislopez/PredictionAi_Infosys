# Failure Prediction AI – Startup & Project Risk Analyzer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B.svg)](https://streamlit.io/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Agentic%20AI-blueviolet.svg)](https://github.com/langchain-ai/langgraph)

An intelligent decision-support platform designed to evaluate startup ideas, business plans, college hackathon projects, and innovative concepts. Powered by Large Language Models (LLMs), agentic AI workflows (LangGraph), strategic risk frameworks, and market intelligence.

---

## ⚡ Key Capabilities

* **Multi-Dimensional Risk Scoring**: Quantitative 1–5 scoring across Market, Financial, Competition, Technical, and Operational vectors.
* **Success Probability Estimation**: Mathematical inverse mapping yielding a 0–100% success probability rate.
* **Automated SWOT Analysis**: Contextual and rule-based derivation of Strengths, Weaknesses, Opportunities, and Threats.
* **Dynamic Market Sizing**: TAM, SAM, and SOM projections with 2020–2026 growth trajectory modeling.
* **Agentic Strategic Mitigations**: LangGraph 6-node reasoning pipeline generating prioritized Action Cards (`Critical`, `High`, `Medium`) and dual-layer mitigation playbooks (Preventive + Contingency).
* **Enterprise Reporting**: One-click export to publication-ready **PDF** (ReportLab) and editable **DOCX** (python-docx).

---

## 🚀 Quick Start

### 1. Prerequisites
* Python 3.9 or higher
* PostgreSQL or Supabase instance

### 2. Environment Setup
```bash
# Clone the repository
git clone https://github.com/Alxislopez/PredictionAi_Infosys.git
cd ML_Market_Intelligence_Project

# Create and activate virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure API Credentials
Create a `.env` file in `ML_Market_Intelligence_Project/`:
```env
GROQ_API_KEY="your_groq_api_key_here"
SUPABASE_URL="your_supabase_url_here"
SUPABASE_KEY="your_supabase_service_key_here"
```

### 4. Run the Streamlit Application
```bash
streamlit run app.py
```
Access the application at `http://localhost:8501`.

---

## 📄 License & MIT Compliance

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

```text
Copyright (c) 2026 Alxislopez
```

For a full compliance breakdown of third-party libraries and runtime dependencies, refer to [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md).
