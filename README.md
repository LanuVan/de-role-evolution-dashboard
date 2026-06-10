# de-role-evolution-dashboard
Global Data Engineering Job Market Analysis (2023) using publicly available job posting datasets on Kaggle.

## Inspiration

The initial idea for this project came from a Medium article by Author Name
https://medium.com/@iduryodhanrao/part-1-the-rise-of-the-modern-data-engineer-71aff25b5dd0

The design, implementation, and enhancements in this repository are my own.
**Project Overview**

Analyze 6,025 global Data Engineering job postings.

**Architecture:**
GitHub
│
├── data/bronze/jobs.csv
│
└── app.py
      ↓
Creates jobs.duckdb automatically
      ↓
Loads CSV
      ↓
Runs dashboard
****
**Technology Stack**
Python
DuckDB
dbt
Streamlit
GitHub
**Key Findings**
SQL appeared in 3,050 jobs
Python appeared in 2,937 jobs
AWS appeared in 1,286 jobs
**Dashboard Features**
Skill Frequency Analysis
Top Hiring Companies
Country Distribution
Skill Search
Cloud Platform Analysis

<img width="1295" height="648" alt="top-companies" src="https://github.com/user-attachments/assets/5fec1c79-1919-4062-a007-ef54881cf288" />
<img width="1378" height="721" alt="skill_search" src="https://github.com/user-attachments/assets/39176452-20ab-460b-bd56-9ff686f9ce8f" />
<img width="1348" height="803" alt="dashboard-overview" src="https://github.com/user-attachments/assets/7cd6dbcb-9e71-4a2f-9374-2731e8735e8d" />
