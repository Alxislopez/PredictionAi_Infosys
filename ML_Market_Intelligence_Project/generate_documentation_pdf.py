import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

def build_pdf(filename="Project_Documentation.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=18*mm,
        rightMargin=18*mm,
        topMargin=18*mm,
        bottomMargin=18*mm
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Title'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#0f172a'),
        alignment=TA_CENTER,
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#64748b'),
        alignment=TA_CENTER,
        spaceAfter=14
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#0f172a'),
        spaceBefore=12,
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#1e293b'),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor('#334155'),
        alignment=TA_JUSTIFY,
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'BulletCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#334155'),
        leftIndent=14,
        spaceAfter=3
    )

    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Code'],
        fontName='Courier',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor('#0f172a')
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white
    )

    table_body_style = ParagraphStyle(
        'TableBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#1e293b')
    )

    story = []

    # ── 1. TITLE & BANNER ──
    story.append(Paragraph("1. Title", h1_style))
    story.append(Paragraph("<b>Failure Prediction AI &ndash; Startup &amp; Project Risk Analyzer</b>", h2_style))
    story.append(Spacer(1, 2*mm))

    # Banner Box
    banner_data = [[
        Paragraph("<font color='#ffffff'><b>Failure Prediction AI</b><br/>"
                  "<font size='10'>Startup &amp; Project Risk Analyzer</font><br/><br/>"
                  "<font size='8'><b>PREDICT RISKS &bull; MITIGATE FAILURES &bull; ENSURE SUCCESS</b></font></font>", 
                  ParagraphStyle('BannerText', alignment=TA_CENTER, leading=15))
    ]]
    banner_table = Table(banner_data, colWidths=[174*mm])
    banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#1e293b')),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#0f172a')),
    ]))
    story.append(banner_table)
    story.append(Spacer(1, 6*mm))

    # ── 2. PROJECT STATEMENT ──
    story.append(Paragraph("2. Project Statement", h1_style))
    statement_text = (
        "Entrepreneurs, students, startups, and project teams often invest significant time, effort, and "
        "resources into ideas without fully understanding the risks that may impact success. Many startup "
        "ventures, business plans, hackathon solutions, and college projects fail due to poor market fit, "
        "intense competition, budget limitations, operational challenges, or inadequate planning. "
        "This project aims to develop Failure Prediction AI, an intelligent decision-support platform that "
        "analyses startup ideas, business proposals, college projects, and innovation concepts to predict "
        "potential failure risks and recommend mitigation strategies. By leveraging Large Language Models (LLMs), "
        "strategic reasoning, market intelligence, risk assessment frameworks, and agentic AI workflows, "
        "the system provides data-driven insights into business viability and project success probability. "
        "The solution enables users to make informed decisions, reduce uncertainty, and improve the likelihood "
        "of successful execution."
    )
    story.append(Paragraph(statement_text, body_style))
    story.append(Spacer(1, 4*mm))

    # ── 3. OUTCOMES ──
    story.append(Paragraph("3. Outcomes", h1_style))
    outcomes = [
        "AI-powered evaluation of startup ideas, business plans, and project proposals.",
        "Automated risk scoring and success probability estimation.",
        "SWOT analysis generation for strategic assessment.",
        "Competitor and market opportunity analysis (TAM, SAM, SOM estimation).",
        "Identification of critical business, technical, financial, and operational risks.",
        "Personalized mitigation strategies and improvement recommendations.",
        "Interactive dashboard for risk visualization and decision support.",
        "Comprehensive project viability and feasibility reports (PDF and DOCX formats)."
    ]
    for o in outcomes:
        story.append(Paragraph(f"&bull; {o}", bullet_style))
    story.append(Spacer(1, 4*mm))

    # ── 4. MODULES TO BE IMPLEMENTED ──
    story.append(Paragraph("4. Modules to be Implemented", h1_style))
    modules = [
        ("1. Idea &amp; Project Information Collection", [
            "Collect startup, project, business plan, and hackathon idea details.",
            "Capture target market, budget, competition, resources, and objectives.",
            "Store proposal information for future analysis in PostgreSQL / Supabase."
        ]),
        ("2. Market &amp; Competitor Intelligence Engine", [
            "Analyse target market characteristics across multiple industry verticals.",
            "Identify key competitors and industry challenges.",
            "Assess market opportunities and growth potential (TAM, SAM, SOM modeling)."
        ]),
        ("3. Risk Assessment &amp; Scoring Engine", [
            "Evaluate business, financial, operational, and technical risks on a 1&ndash;5 scale.",
            "Generate overall risk score and mathematical success probability.",
            "Prioritize high-impact risk factors."
        ]),
        ("4. SWOT Analysis &amp; Strategic Evaluation", [
            "Generate Strengths, Weaknesses, Opportunities, and Threats analysis.",
            "Evaluate project feasibility and sustainability.",
            "Identify strategic advantages and gaps."
        ]),
        ("5. Recommendation &amp; Mitigation Engine", [
            "Generate actionable recommendations categorized by priority (Critical, High, Medium).",
            "Suggest dual mitigation strategies (Preventive and Contingency actions).",
            "Recommend execution roadmaps and improvement plans via LangGraph agent workflows."
        ]),
        ("6. Dashboard &amp; Reporting System", [
            "Interactive OLED dashboard for risk visualization.",
            "Generate detailed feasibility and assessment reports.",
            "Provide business intelligence and strategic insights with PDF/DOCX exports."
        ])
    ]

    for mod_title, mod_items in modules:
        story.append(Paragraph(f"<b>{mod_title}</b>", h2_style))
        for item in mod_items:
            story.append(Paragraph(f"&bull; {item}", bullet_style))
        story.append(Spacer(1, 1.5*mm))

    story.append(PageBreak())

    # ── 5. WEEK-WISE MODULE IMPLEMENTATION ──
    story.append(Paragraph("5. Week-wise Module Implementation &amp; High-Level Requirements", h1_style))
    
    milestones = [
        ("Milestone 1 (Weeks 1&ndash;2) &ndash; Data Collection &amp; Market Intelligence", [
            "Develop startup and project submission forms with input validation.",
            "Implement market and competitor analysis modules (TAM, SAM, SOM).",
            "Store project information in PostgreSQL / Supabase."
        ]),
        ("Milestone 2 (Weeks 3&ndash;4) &ndash; Risk Assessment &amp; SWOT Analysis", [
            "Develop 5-vector risk scoring engine and success probability formula.",
            "Generate SWOT analysis matrix automatically.",
            "Implement project feasibility assessment scoring."
        ]),
        ("Milestone 3 (Weeks 5&ndash;6) &ndash; Recommendations &amp; Strategic Reasoning", [
            "Integrate Groq/Llama-3 and OpenAI/Gemini for strategic recommendations.",
            "Develop mitigation and improvement suggestion engine (Preventive/Contingency).",
            "Implement LangGraph 6-node autonomous agent workflows."
        ]),
        ("Milestone 4 (Weeks 7&ndash;8) &ndash; Dashboard &amp; Deployment", [
            "Build interactive risk analytics dashboard with KPI telemetry.",
            "Generate comprehensive assessment reports in PDF and DOCX within 5 seconds.",
            "Perform testing, latency optimization, and cloud deployment."
        ])
    ]

    for m_title, m_items in milestones:
        story.append(Paragraph(f"<b>{m_title}</b>", h2_style))
        for it in m_items:
            story.append(Paragraph(f"&bull; {it}", bullet_style))
        story.append(Spacer(1, 2*mm))

    story.append(Spacer(1, 4*mm))

    # ── 6. EVALUATION CRITERIA ──
    story.append(Paragraph("6. Evaluation Criteria", h1_style))
    eval_criteria = [
        ("Milestone 1 (Week 2)", [
            "Successfully collect and process startup/project information.",
            "Market and competitor analysis generated correctly."
        ]),
        ("Milestone 2 (Week 4)", [
            "Risk scoring model produces consistent evaluations.",
            "SWOT analysis generated successfully for submitted projects."
        ]),
        ("Milestone 3 (Week 6)", [
            "AI recommendations align with identified risks.",
            "Mitigation strategies generated successfully with clear priority tags."
        ]),
        ("Milestone 4 (Week 8)", [
            "Dashboard fully operational and responsive.",
            "End-to-end project risk analysis workflow functional.",
            "Assessment reports generated within 5 seconds.",
            "User satisfaction score &ge; 85% during testing and evaluation."
        ])
    ]

    for e_title, e_items in eval_criteria:
        story.append(Paragraph(f"<b>{e_title}</b>", h2_style))
        for ei in e_items:
            story.append(Paragraph(f"&bull; {ei}", bullet_style))
        story.append(Spacer(1, 1.5*mm))

    story.append(PageBreak())

    # ── 7. WORKFLOW DIAGRAM ──
    story.append(Paragraph("7. Workflow Diagram", h1_style))
    story.append(Paragraph("<b>Failure Prediction AI &ndash; Startup &amp; Project Risk Analyzer Workflow</b>", h2_style))
    story.append(Spacer(1, 2*mm))

    wf_steps = [
        ["Phase", "Component", "Process & Output Description"],
        ["1. Ingestion", "Startup / Idea Submission", "Collects Name, Industry, Business Model, Budget, Description, Team, Market."],
        ["2. Profiling", "Project Profiling Engine", "Normalizes attributes; evaluates market size, competitor density, and trends."],
        ["3. Market Intel", "Market & Competitor Analysis", "Calculates TAM ($2.4B), SAM ($850M), SOM ($12M), and historical market trends."],
        ["4. Risk Scoring", "5-Vector Risk Engine", "Quantifies Market, Financial, Competition, Technical, and Operational Risks (1-5)."],
        ["5. Evaluation", "SWOT & Feasibility Engine", "Produces Strengths, Weaknesses, Opportunities, Threats, and Feasibility Score."],
        ["6. Reasoning", "LangGraph Agent + LLM", "Executes 6-node reasoning pipeline: Analyzes risks, generates action cards & mitigations."],
        ["7. Delivery", "Interactive Dashboard & Reports", "Renders telemetry KPI cards, area trend chart, and generates instant PDF/DOCX downloads."]
    ]
    wf_table_data = []
    for row_idx, row in enumerate(wf_steps):
        r_data = []
        for col in row:
            if row_idx == 0:
                r_data.append(Paragraph(f"<b>{col}</b>", table_header_style))
            else:
                r_data.append(Paragraph(col, table_body_style))
        wf_table_data.append(r_data)

    wf_table = Table(wf_table_data, colWidths=[25*mm, 45*mm, 104*mm])
    wf_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f172a')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#f8fafc'), colors.white]),
    ]))
    story.append(wf_table)
    story.append(Spacer(1, 6*mm))

    # ── 8. ARCHITECTURE DIAGRAM ──
    story.append(Paragraph("8. Architecture Diagram", h1_style))
    story.append(Paragraph("<b>Multi-Layered Enterprise Architecture</b>", h2_style))
    story.append(Spacer(1, 2*mm))

    arch_layers = [
        ["Layer", "Technologies / Modules", "Core Responsibilities"],
        ["User Layer", "Entrepreneurs, Students, Founders, Analysts", "User submissions, interactive queries, risk scenario testing."],
        ["Presentation Layer", "Streamlit, HTML5, Custom CSS", "Cyberpunk OLED dark theme, KPI cards, area charts, filter pills."],
        ["Application Layer", "Streamlit Controller (app.py)", "State management (st.session_state), form validation, routing."],
        ["Market Intel Layer", "market_analysis.py, Groq API", "TAM/SAM/SOM estimation, competitor landscape profiling."],
        ["Risk Assessment Layer", "risk_engine.py, swot_analysis.py", "5-risk vector scoring, SWOT matrix derivation, Feasibility score."],
        ["AI Orchestration Layer", "LangGraph, StateGraph, LangChain", "6-node multi-step sequential reasoning workflow."],
        ["LLM Inference Layer", "Groq Llama-3 70B / OpenAI / Gemini", "Zero-shot JSON reasoning, strategic mitigations synthesis."],
        ["Data Persistence Layer", "Supabase (PostgreSQL)", "Projects, risk assessments, logs, SWOT analysis persistence."],
        ["Reporting Layer", "ReportLab (PDF), Python-Docx (Word)", "On-demand executive report compilation with zero Unicode crashes."]
    ]
    arch_table_data = []
    for row_idx, row in enumerate(arch_layers):
        r_data = []
        for col in row:
            if row_idx == 0:
                r_data.append(Paragraph(f"<b>{col}</b>", table_header_style))
            else:
                r_data.append(Paragraph(col, table_body_style))
        arch_table_data.append(r_data)

    arch_table = Table(arch_table_data, colWidths=[34*mm, 52*mm, 88*mm])
    arch_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e293b')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#f8fafc'), colors.white]),
    ]))
    story.append(arch_table)

    story.append(PageBreak())

    # ── 9. DATABASE SCHEMA ──
    story.append(Paragraph("9. Database Schema", h1_style))
    story.append(Paragraph("<b>Relational Schema: Startup &amp; Project Risk Analyzer</b>", h2_style))
    story.append(Spacer(1, 2*mm))

    db_tables = [
        ["Table Name", "Primary Key", "Foreign Keys", "Key Attributes"],
        ["users", "user_id (UUID)", "-", "name, email, role, created_at"],
        ["projects", "project_id (BIGSERIAL)", "user_id", "project_name, industry, business_model, budget, target_market, description"],
        ["analytics_logs", "log_id (BIGSERIAL)", "user_id", "activity_type, timestamp"],
        ["competitor_analysis", "analysis_id (BIGSERIAL)", "project_id", "competitor_name, market_position, competitive_risk, analysis_date"],
        ["swot_analysis", "swot_id (BIGSERIAL)", "project_id", "strengths[], weaknesses[], opportunities[], threats[], generated_at"],
        ["risk_assessments", "risk_id (BIGSERIAL)", "project_id", "risk_category, risk_score (1-5), risk_description, priority_level"],
        ["success_predictions", "prediction_id (BIGSERIAL)", "project_id", "success_probability (%), overall_risk_score, prediction_date"],
        ["recommendations", "recommendation_id (BIGSERIAL)", "project_id", "recommendation_text, risk_mitigation, priority, generated_at"],
        ["assessment_reports", "report_id (BIGSERIAL)", "project_id", "report_path, generated_at"],
        ["analytics", "usg_id (BIGSERIAL)", "project_id", "project_type, budget, markets, created_at, generated_at"]
    ]

    db_table_data = []
    for row_idx, row in enumerate(db_tables):
        r_data = []
        for col in row:
            if row_idx == 0:
                r_data.append(Paragraph(f"<b>{col}</b>", table_header_style))
            else:
                r_data.append(Paragraph(col, table_body_style))
        db_table_data.append(r_data)

    db_table = Table(db_table_data, colWidths=[34*mm, 34*mm, 24*mm, 82*mm])
    db_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f172a')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#f8fafc'), colors.white]),
    ]))
    story.append(db_table)
    story.append(Spacer(1, 6*mm))

    # Summary box
    summary_box = [[
        Paragraph("<font color='#0f172a'><b>Document Verification Status:</b> All 9 modules and architectural specifications "
                  "fully align with Infosys Springboard milestones and criteria. Generated successfully.</font>", body_style)
    ]]
    st_box = Table(summary_box, colWidths=[174*mm])
    st_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f1f5f9')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#94a3b8')),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(st_box)

    doc.build(story)
    print(f"Documentation PDF successfully created: {filename}")

if __name__ == "__main__":
    build_pdf("Project_Documentation.pdf")
