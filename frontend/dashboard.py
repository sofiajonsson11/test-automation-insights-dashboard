import os
import streamlit as st
import requests
import plotly.express as px

st.set_page_config(page_title="Test Automation Insights", layout="wide")
st.title("Test Automation Insights Dashboard")

BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:8000").rstrip("/")

st.sidebar.markdown("### Controls")
source_filter = st.sidebar.selectbox("Source", ["all", "pytest", "cypress", "postman"])
fetch = st.sidebar.button("Refresh")


@st.cache_data(ttl=30)
def fetch_results():
    try:
        r = requests.get(f"{BACKEND_URL}/results")
        r.raise_for_status()
        return r.json()
    except Exception as e:
        st.error(f"Error fetching results: {e}")
        return []


if fetch or True:
    data = fetch_results()
else:
    data = []

if not data:
    st.info("No test results — try posting a sample result to the backend.")
else:
    # filter
    if source_filter != "all":
        data = [d for d in data if d.get("source") == source_filter]

    # status counts
    df_status = {}
    for d in data:
        df_status[d["status"]] = df_status.get(d["status"], 0) + 1

    fig = px.bar(
        x=list(df_status.keys()),
        y=list(df_status.values()),
        labels={"x": "status", "y": "count"},
        title="Status counts",
    )
    st.plotly_chart(fig, use_container_width=True)

    # show raw table
    st.subheader("Recent results (top 50)")
    import pandas as pd

    df = pd.DataFrame(data)
    if not df.empty:
        st.dataframe(df.head(50))
