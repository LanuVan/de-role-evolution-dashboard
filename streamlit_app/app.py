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

st.markdown("""
Analyze 6,000+ Data Engineering job postings using
**DuckDB + dbt + Streamlit**
""")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.header("Filters")

countries_df = con.execute("""
select distinct search_country
from raw_jobs
where search_country is not null
order by search_country
""").fetchdf()

country_list = ["All"] + countries_df["search_country"].tolist()

selected_country = st.sidebar.selectbox(
    "Country",
    country_list
)

# --------------------------------------------------
# FILTER CLAUSE
# --------------------------------------------------

if selected_country == "All":
    filter_clause = ""
else:
    filter_clause = f"""
    where search_country = '{selected_country}'
    """

# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------

total_jobs = con.execute(f"""
select count(*)
from raw_jobs
{filter_clause}
""").fetchone()[0]

total_companies = con.execute(f"""
select count(distinct company)
from raw_jobs
{filter_clause}
""").fetchone()[0]

total_cities = con.execute(f"""
select count(distinct search_city)
from raw_jobs
{filter_clause}
""").fetchone()[0]

total_countries = con.execute("""
select count(distinct search_country)
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

st.subheader("🔥 Top Skills")

skill_df = con.execute("""
select *
from skill_frequency
limit 20
""").fetchdf()

st.bar_chart(
    skill_df.set_index("skill")
)

# --------------------------------------------------
# CLOUD DEMAND
# --------------------------------------------------

st.subheader("☁️ Cloud Platform Demand")

cloud_df = con.execute("""
select *
from skill_frequency
where skill in (
    'aws',
    'azure',
    'gcp'
)
order by frequency desc
""").fetchdf()

st.bar_chart(
    cloud_df.set_index("skill")
)

# --------------------------------------------------
# TOP COMPANIES
# --------------------------------------------------

st.subheader("🏢 Top Hiring Companies")

company_df = con.execute(f"""
select
    company,
    count(*) as jobs

from raw_jobs

{filter_clause}

group by company

order by jobs desc

limit 15
""").fetchdf()

st.bar_chart(
    company_df.set_index("company")
)

# --------------------------------------------------
# COUNTRY DISTRIBUTION
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
# SKILL SEARCH
# --------------------------------------------------

st.subheader("🔍 Search Jobs by Skill")

search_skill = st.text_input(
    "Enter a skill (Python, SQL, AWS, Snowflake, Kafka...)"
)

if search_skill:

    jobs_df = con.execute(f"""
    select
        company,
        job_title,
        search_country,
        search_city

    from raw_jobs

    where lower(job_skills)
    like '%{search_skill.lower()}%'

    limit 100
    """).fetchdf()

    st.write(
        f"Found {len(jobs_df)} jobs containing '{search_skill}'"
    )

    st.dataframe(
        jobs_df,
        use_container_width=True
    )

# --------------------------------------------------
# SAMPLE DATA
# --------------------------------------------------

with st.expander("📄 View Sample Dataset"):

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
    "Built using Python • DuckDB • dbt • Streamlit • GitHub"
)