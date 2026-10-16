# Failure Prediction AI – Startup & Project Risk Analyzer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B.svg)](https://streamlit.io/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Agentic%20AI-blueviolet.svg)](https://github.com/langchain-ai/langgraph)

An intelligent decision-support platform designed to evaluate startup ideas, business plans, college hackathon projects, and innovative concepts. Powered by Large Language Models (LLMs), agentic AI workflows (LangGraph), strategic risk frameworks, and market intelligence.

---

## ⚡ Project Structure

```text
├── ML_Market_Intelligence_Project/
│   ├── app.py                            # Main Streamlit Cyberpunk Dashboard
│   ├── risk_engine.py                    # 5-Vector Risk Scoring & Success Probability
│   ├── swot_analysis.py                  # Automated SWOT Matrix Generator
│   ├── feasibility.py                    # Project Feasibility Scoring
│   ├── market_analysis.py                # TAM / SAM / SOM Market Modeling
│   ├── recommendations_agent.py          # 6-Node LangGraph Agent Pipeline
│   ├── report_generator.py               # Unicode PDF (ReportLab) & DOCX Generators
│   ├── database.py                       # Supabase PostgreSQL Integration
│   ├── requirements.txt                  # Application Dependencies
│   ├── technical_documentation.md        # Full 9-Section Milestone Specification
│   ├── LICENSE                           # MIT License
│   └── THIRD_PARTY_LICENSES.md           # OSS License Matrix & Compliance
├── LICENSE                               # Root MIT License
├── THIRD_PARTY_LICENSES.md               # Root Open Source Compliance Statement
├── requirements.txt                      # Root Deployment Requirements
└── README.md                             # Repository Overview
```

---

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Navigate to project directory
cd ML_Market_Intelligence_Project

# 3. Launch application
streamlit run app.py
```

---

## 📄 License & MIT Compliance

This project is open-source software licensed under the **[MIT License](LICENSE)**.

```text
Copyright (c) 2026 Alxislopez
```

All third-party dependencies are permissive and verified for MIT compatibility. See **[THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md)** for details.
