import streamlit as st
import duckdb
import pandas as pd

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Global Data Engineering Jobs Dashboard",
    page_icon="🌍",
    layout="wide"
)

# --------------------------------------------------
# DATABASE CONNECTION
# --------------------------------------------------

con = duckdb.connect("duckdb/jobs.duckdb")

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🌍 Global Data Engineering Jobs Dashboard")
st.markdown("Analysis of 6,000+ Data Engineering job postings using DuckDB, dbt and Streamlit")

# --------------------------------------------------
# KPI METRICS
# --------------------------------------------------

total_jobs = con.execute("""
select count(*)
from raw_jobs
""").fetchone()[0]

total_companies = con.execute("""
select count(distinct company)
from raw_jobs
""").fetchone()[0]

total_countries = con.execute("""
select count(distinct search_country)
from raw_jobs
""").fetchone()[0]

total_cities = con.execute("""
select count(distinct search_city)
from raw_jobs
""").fetchone()[0]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Jobs", f"{total_jobs:,}")
col2.metric("Companies", f"{total_companies:,}")
col3.metric("Countries", total_countries)
col4.metric("Cities", total_cities)

st.divider()

# --------------------------------------------------
# TOP SKILLS
# --------------------------------------------------

st.subheader("🔥 Most Requested Skills")

skill_df = con.execute("""
select *
from skill_frequency
limit 20
""").fetchdf()

st.bar_chart(
    skill_df.set_index("skill")
)

# --------------------------------------------------
# CLOUD PLATFORM DEMAND
# --------------------------------------------------

st.subheader("☁️ Cloud Platform Demand")

cloud_df = con.execute("""
select *
from skill_frequency
where skill in ('aws','azure','gcp')
order by frequency desc
""").fetchdf()

st.bar_chart(
    cloud_df.set_index("skill")
)

# --------------------------------------------------
# TOP HIRING COMPANIES
# --------------------------------------------------

st.subheader("🏢 Top Hiring Companies")

company_df = con.execute("""
select
    company,
    count(*) as jobs
from raw_jobs
group by company
order by jobs desc
limit 15
""").fetchdf()

st.bar_chart(
    company_df.set_index("company")
)

# --------------------------------------------------
# JOBS BY COUNTRY
# --------------------------------------------------

st.subheader("🌎 Jobs by Country")

country_df = con.execute("""
select
    search_country,
    count(*) as jobs
from raw_jobs
group by search_country
order by jobs desc
""").fetchdf()

st.bar_chart(
    country_df.set_index("search_country")
)

# --------------------------------------------------
# COUNTRY FILTER
# --------------------------------------------------

st.subheader("🔍 Explore Jobs by Country")

countries = con.execute("""
select distinct search_country
from raw_jobs
order by search_country
""").fetchdf()

selected_country = st.selectbox(
    "Select Country",
    countries["search_country"]
)

country_jobs = con.execute(f"""
select
    company,
    job_title,
    search_city,
    job_type
from raw_jobs
where search_country = '{selected_country}'
limit 100
""").fetchdf()

st.dataframe(
    country_jobs,
    use_container_width=True
)

# --------------------------------------------------
# RAW DATA EXPLORER
# --------------------------------------------------

with st.expander("📄 View Sample Data"):

    sample_df = con.execute("""
    select *
    from raw_jobs
    limit 25
    """).fetchdf()

    st.dataframe(
        sample_df,
        use_container_width=True
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Built using DuckDB • dbt • Streamlit • GitHub"
)