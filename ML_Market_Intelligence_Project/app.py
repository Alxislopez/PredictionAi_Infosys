import streamlit as st
import matplotlib.pyplot as plt
from database import get_supabase_client
from market_analysis import get_market_summary
from risk_engine import calculate_risk, get_risk_status, calculate_success_probability
from swot_analysis import generate_swot
from feasibility import calculate_feasibility

# Page Configuration
st.set_page_config(page_title="Prediction Ai", layout="wide")

# Dashboard Header
st.title("Prediction Ai ")
st.subheader("Risk Assessment & SWOT Analysis")
st.write("AI-powered risk scoring and strategic evaluation")
st.divider()

# Tab Navigation
tab1, tab2, tab3, tab4 = st.tabs(["Project Input", "Risk Assessment", "Recommendations", "Dashboard"])

# ----------------- TAB 1: PROJECT INPUT -----------------
with tab1:
    st.header("Project Input")
    st.write("Enter the details of the startup project.")
    
    with st.form("project_form"):
        startup_name = st.text_input("Startup Name *")
        industry = st.text_input("Industry *")
        business_model = st.text_input("Business Model *")
        target_market = st.text_input("Target Market")
        budget = st.number_input("Budget ($)", min_value=0.0, step=1000.0)
        description = st.text_area("Project Description")
        
        submitted = st.form_submit_button("Submit Project")
        if submitted:
            if startup_name and industry and business_model:
                try:
                    supabase = get_supabase_client()
                    supabase.table("projects").insert({
                        "startup_name": startup_name,
                        "industry": industry,
                        "business_model": business_model,
                        "target_market": target_market,
                        "budget": budget,
                        "project_description": description
                    }).execute()
                    st.success("Project submitted successfully! Check the Dashboard tab.")
                except Exception as e:
                    st.error(f"Database error: {e}")
            else:
                st.warning("Please fill all required fields (Name, Industry, Business Model).")

# ----------------- TAB 2: RISK ASSESSMENT -----------------
with tab2:
    st.header("Risk Assessment Inputs")
    
    # 1. Inputs
    col1, col2 = st.columns(2)
    with col1:
        market_competition = st.selectbox("Market Competition", ["Low", "Medium", "High"])
        team_expertise = st.selectbox("Team Expertise", ["Low", "Medium", "High"])
        resource_availability = st.selectbox("Resource Availability", ["Limited", "Moderate", "Good"])
    
    with col2:
        innovation_level = st.selectbox("Innovation Level", ["Low", "Medium", "High"])
        market_research = st.selectbox("Market Research", ["Limited", "Moderate", "Strong"])

    st.divider()

    # 2. Calculate Risk
    risk_result = calculate_risk(market_competition, team_expertise, resource_availability, innovation_level, market_research)
    risk_score = risk_result["score"]
    five_risks = risk_result["details"]
    risk_status = get_risk_status(risk_score)
    success_probability = calculate_success_probability(risk_score)

    # 3. Display Risk
    st.subheader("Risk Score & Breakdown")
    
    # Show the 5 risks
    r1, r2, r3, r4, r5 = st.columns(5)
    r1.metric("Market Risk", f"{five_risks['Market Risk']}/5")
    r2.metric("Financial Risk", f"{five_risks['Financial Risk']}/5")
    r3.metric("Competition", f"{five_risks['Competition Risk']}/5")
    r4.metric("Technical", f"{five_risks['Technical Risk']}/5")
    r5.metric("Operational", f"{five_risks['Operational Risk']}/5")
    
    st.write("---")

    col_r1, col_r2 = st.columns(2)
    with col_r1:
        st.metric("Overall Risk Score", f"{risk_score:.1f}/5")
    with col_r2:
        if risk_status == "HIGH RISK":
            st.error(risk_status)
        elif risk_status == "MEDIUM RISK":
            st.warning(risk_status)
        else:
            st.success(risk_status)

    # 4. Display Success Probability
    st.subheader("Success Probability")
    st.progress(success_probability / 100)
    st.write(f"{success_probability}%")

    st.divider()

    # 5. Generate and Display SWOT
    swot = generate_swot(team_expertise, innovation_level, market_competition, resource_availability, market_research)
    
    st.header("SWOT Analysis")
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.success("### Strengths")
        for item in swot["Strengths"]:
            st.write("•", item)
    with col_s2:
        st.error("### Weaknesses")
        for item in swot["Weaknesses"]:
            st.write("•", item)

    col_s3, col_s4 = st.columns(2)
    with col_s3:
        st.info("### Opportunities")
        for item in swot["Opportunities"]:
            st.write("•", item)
    with col_s4:
        st.warning("### Threats")
        for item in swot["Threats"]:
            st.write("•", item)

    st.divider()

    # 6. Feasibility Assessment
    st.header("Project Feasibility")

    feasibility_score = calculate_feasibility(risk_score, swot)
    st.metric("Feasibility Score", f"{feasibility_score}%")
    st.write("Feasibility is calculated automatically based on the Overall Risk Score and the balance of SWOT factors.")

from recommendations_agent import run_agent
import time

# ----------------- TAB 3: RECOMMENDATIONS -----------------
with tab3:
    st.header("Recommendations & Strategic Reasoning")
    st.caption("AI-powered mitigation strategies and agent workflows")
    st.write("---")
    
    # We need a button or an automatic trigger to run the agent
    if "agent_result" not in st.session_state:
        st.session_state.agent_result = None

    if st.button("Generate Strategic Recommendations"):
        with st.spinner("LangGraph Agent is analyzing risks and generating recommendations..."):
            # Prepare inputs
            project_data = {} # In a real app, pull from Tab 1
            risk_data = five_risks
            swot_data = swot
            
            st.session_state.agent_result = run_agent(project_data, risk_data, swot_data)
            
    if st.session_state.agent_result:
        res = st.session_state.agent_result
        
        # Sub-tabs for the extensive data
        tab_rec, tab_mit, tab_imp, tab_rep, tab_flow = st.tabs([
            "Recommendations", "Mitigation Strategies", "Improvements", "Final Report", "Workflow"
        ])
        
        with tab_rec:
            st.subheader("Strategic Recommendations")
            for rec in res.get("recommendations", []):
                with st.expander(f"{rec.get('priority', '')} | {rec.get('title', '')}"):
                    st.caption(f"Category: {rec.get('category', '')}")
                    st.write(rec.get("description", ""))
                    
        with tab_mit:
            st.subheader("Risk Mitigations")
            for mit in res.get("mitigations", []):
                with st.expander(f"{mit.get('risk_name', 'Risk')} ({mit.get('impact', 'Medium Impact')})"):
                    st.write(f"**Category:** {mit.get('category', '')}")
                    st.write(f"**Problem:** {mit.get('description', '')}")
                    st.write(f"**Strategy:** {mit.get('mitigation_strategy', '')}")
                    st.info(f"Preventive: {mit.get('preventive_action', '')}")
                    st.warning(f"Contingency: {mit.get('contingency_action', '')}")
                    
        with tab_imp:
            st.subheader("Improvement Suggestions")
            for imp in res.get("improvements", []):
                with st.container(border=True):
                    st.write(f"**{imp.get('category', '')}**: {imp.get('improvement', '')}")
                    st.caption(f"Reason: {imp.get('reason', '')} | Benefit: {imp.get('expected_benefit', '')}")
                    
        with tab_rep:
            st.subheader("Final Strategic Assessment")
            st.write(res.get("final_response", ""))
            
        with tab_flow:
            st.subheader("LangGraph Execution Timeline")
            for step in res.get("workflow_steps", []):
                st.write(f"{step.get('icon', '')} **{step.get('name', '')}** - {step.get('desc', '')}")
                st.write("↓")


# ----------------- TAB 4: DASHBOARD -----------------
with tab4:
    # Use 3 columns to match the layout: Left (Project), Middle (Market), Right (Competitors)
    col_left, col_mid, col_right = st.columns([1.2, 2.5, 1.2], gap="large")
    
    # --- LEFT COLUMN: Project Submission ---
    with col_left:
        st.subheader("Project Submission")
        st.caption("Latest submitted project")
        st.write("---")
        
        try:
            supabase = get_supabase_client()
            response = supabase.table("projects").select("*").order("id", desc=True).limit(1).execute()
            
            if response.data:
                latest = response.data[0]
                st.caption("Startup / Project Name")
                st.write(f"**{latest.get('startup_name')}**")
                
                st.caption("Industry / Sector")
                st.write(f"**{latest.get('industry')}**")
                
                st.caption("Business Model")
                st.write(f"**{latest.get('business_model')}**")
                
                l_c1, l_c2 = st.columns(2)
                with l_c1:
                    st.caption("Target Market")
                    st.write(f"**{latest.get('target_market')}**")
                with l_c2:
                    st.caption("Budget (USD)")
                    budget_val = latest.get("budget")
                    st.write(f"**${budget_val:,.0f}**" if budget_val else "**$0**")
                
                st.caption("Project Description")
                st.write(latest.get('project_description') or "No description provided.")
            else:
                st.info("No projects found in the database.")
        except Exception as e:
            st.error("Database Connection Error")

    # --- MIDDLE COLUMN: Market Analysis ---
    with col_mid:
        st.subheader("Market Analysis")
        st.caption("Market size and growth indicators")
        st.write("---")
        
        market_data = get_market_summary()
        
        # Metrics Row
        m1, m2, m3 = st.columns(3)
        m1.metric("TAM", f"${market_data['tam']}B", f"+{market_data['market_growth']}%")
        m2.metric("SAM", f"${market_data['sam']}M", "+5.5%")
        m3.metric("SOM", f"${market_data['som']}M", "-2.1%")
        
        st.write("")
        st.write("**Market Trends (2020–2026)**")
        st.caption("Estimated market size trend")
        
        import pandas as pd
        # Create a dataframe for the area chart
        chart_df = pd.DataFrame(
            {"Market Size ($M)": market_data["market_values"]}, 
            index=[str(y) for y in market_data["years"]]
        )
        st.area_chart(chart_df, color="#73bdf7")

    # --- RIGHT COLUMN: Competitor Landscape ---
    with col_right:
        st.subheader("Competitor Landscape")
        st.caption("Key market competitors")
        st.write("---")
        
        competitors = market_data["competitors"]
        for comp in competitors:
            st.write(f"**{comp['company']}**")
            
            c1, c2, c3 = st.columns(3)
            c1.caption("Market Share")
            c1.write(f"**{comp['market_share']}%**")
            
            c2.caption("Revenue")
            c2.write(f"**${comp['revenue']}M**")
            
            c3.caption("Growth")
            growth_val = comp['growth']
            growth_str = f"**+{growth_val}%**" if growth_val > 0 else f"**{growth_val}%**"
            c3.write(growth_str)
            
            st.progress(comp['market_share'] / 100)
            st.write("") # Spacer
