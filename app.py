import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

# Load data
@st.cache_data
def load_data():
    return pd.read_csv(r"df_scores.csv")

df = load_data()
sectors = ['Economy', 'Education', 'Health', 'Infrastructure', 'Environment']

# Streamlit config
st.set_page_config(page_title="India Sectoral Dashboard", layout="wide")
st.title("📊 India Sectoral Development Dashboard")
st.markdown("Explore India's development across Economy, Education, Health, Infrastructure, and Environment (2000–2023).")

# Initialize session state
if "active_chart" not in st.session_state:
    st.session_state["active_chart"] = None

# Card component
def card(label, color):
    return f"""
    <div style="
        background-color: {color};
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 0.5rem;
        color: white;
        text-align: center;
        font-weight: bold;
        font-size: 1.1rem;
        cursor: pointer;
        transition: transform 0.2s ease;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        ">
        {label}
    </div>
    """

# Card layout
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.markdown(card("📈 Sector Score Over Time", "#1f77b4"), unsafe_allow_html=True)
    if st.button("Show Sector Line Chart", key="btn_line"):
        st.session_state["active_chart"] = "line"

with col2:
    st.markdown(card("🕸️ Snapshot for Selected Year", "#ff7f0e"), unsafe_allow_html=True)
    if st.button("Show Radar Snapshot", key="btn_radar"):
        st.session_state["active_chart"] = "radar"

col3, col4 = st.columns(2)

with col3:
    st.markdown(card("📊 Total Development Score", "#2ca02c"), unsafe_allow_html=True)
    if st.button("Show Total Score", key="btn_total"):
        st.session_state["active_chart"] = "total"

with col4:
    st.markdown(card("📉 Correlation Heatmap", "#d62728"), unsafe_allow_html=True)
    if st.button("Show Heatmap", key="btn_corr"):
        st.session_state["active_chart"] = "corr"

col5, _ = st.columns([1, 1])
with col5:
    st.markdown(card("🏆 Best Year per Sector", "#9467bd"), unsafe_allow_html=True)
    if st.button("Show Best Years", key="btn_best"):
        st.session_state["active_chart"] = "best"

st.markdown("---")

# ============== Render Chart Based on Active Selection ==============

# 1. Line Chart
if st.session_state["active_chart"] == "line":
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    for s in sectors:
        ax1.plot(df["Year"], df[s], label=s)
    ax1.set_title("Normalized Sector Scores Over Time")
    ax1.set_ylabel("Score")
    ax1.set_xlabel("Year")
    ax1.legend()
    ax1.grid(True)
    st.pyplot(fig1)
    with st.expander("🔍 Inference"):
        st.markdown("""
        - Economy and Infrastructure are rising steadily.
        - Health dropped slightly around 2020 (pandemic effect).
        - Infrastructure and Health are the best performing sectors (highest 2023 scores)
        - Environment is the weakest, needs policy focus
        - COVID-19 visibly impacted Health and Education after 2020
        - India’s development is not evenly distributed i.e. it is strong in tech & health, weaker in ecology
        """)

# 2. Radar Chart
if st.session_state["active_chart"] == "radar":
    selected_year = st.selectbox("Select Year", df["Year"].unique()[::-1], key="radar_year")
    radar_data = df[df["Year"] == selected_year].iloc[0][sectors]

    fig2 = go.Figure()
    fig2.add_trace(go.Scatterpolar(
        r=radar_data.values,
        theta=sectors,
        fill='toself',
        name=f"{selected_year}"
    ))
    fig2.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
        showlegend=False,
        title=f"Radar Chart - Sector Performance in {selected_year}"
    )
    st.plotly_chart(fig2)
    with st.expander("🔍 Inference"):
        st.markdown(f"""
        - {selected_year} snapshot helps spot sector strengths & weaknesses.
        - India’s Health, Education, and Economy sectors are nearing optimal normalized performance
        - If the other two (Infra, Environment) are low, it indicates a skewed development model
        - Very strong tertiary sector, but possibly lagging sustainability/infrastructure depth
        """)

# 3. Total Score Chart
if st.session_state["active_chart"] == "total":
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    ax3.plot(df["Year"], df["Total Development Score"], marker='o', color='green')
    ax3.set_title("Overall Development Score (YoY)")
    ax3.set_ylabel("Total Development Score")
    ax3.set_xlabel("Year")
    ax3.grid(True)
    st.pyplot(fig3)
    with st.expander("🔍 Inference"):
        st.markdown("""
        - Overall growth is evident across years.
        - Sharp dip during COVID (2020–21).
        
        India’s overall development score has increased by over 5.5X since 2000,
        with major leaps post-2015 and a dramatic surge after 2020.
        This reflects the compounding effects of investments in health, infrastructure, and education.
        Minor dips align with external shocks like the 2009 crisis and 2020 pandemic,
        but overall trajectory is clearly upward
        """)

# 4. Correlation Heatmap
if st.session_state["active_chart"] == "corr":
    fig4, ax4 = plt.subplots(figsize=(8, 5))
    corr = df[sectors].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax4)
    ax4.set_title("Correlation Between Sector Scores")
    st.pyplot(fig4)
    with st.expander("🔍 Inference"):
        st.markdown("""
        - Strong correlation between Economy & Infrastructure.
        - Education is moderately correlated with others.
        - Health and Infrastructure go hand-in-hand (r=0.91)
        - Balanced development means investing in Health, Infra, and Education
        - Environment is disconnected from other development goals

        "Why Environment lags?"
            → Possible reasons: urbanization, weak policy enforcement, lack of measurement
        """)

# 5. Best Year per Sector
if st.session_state["active_chart"] == "best":
    best_years = df.set_index("Year")[sectors].idxmax()
    baseline_year = 2000
    bar_heights = best_years - baseline_year

    color_map = {
        "Economy": "#9467bd",
        "Education": "#1f77b4",
        "Health": "#ff7f0e",
        "Infrastructure": "#d62728",
        "Environment": "#2ca02c"
    }

    fig5, ax5 = plt.subplots(figsize=(8, 5))
    for sector in sectors:
        ax5.bar(sector, bar_heights[sector], color=color_map[sector])
    ax5.set_title("Best Performing Year for Each Sector")
    ax5.set_ylabel("Year")
    ax5.set_ylim(0, 24)
    ax5.set_yticks(range(24))
    ax5.set_yticklabels([str(y) for y in range(2000, 2024)])
    for i, (sector, year) in enumerate(best_years.items()):
        ax5.text(i, year - baseline_year + 0.5, str(year), ha='center', va='bottom')
    st.pyplot(fig5)

    with st.expander("🔍 Inference"):
        st.markdown("""
        - Economy peaked in 2023.
        - Education peaked early in 2016, indicating stagnation.
        - Environment & Infrastructure peaked in 2022.
        """)

# Footer
st.markdown("---")
st.markdown("""
**📍 Dashboard by Vivek Joshi**  
_Data Source: World Bank, Sector Reports, India Indicators_
""")
