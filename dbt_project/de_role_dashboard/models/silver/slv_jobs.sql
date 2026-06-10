select
    lower(job_title) as job_title,
    company,
    job_location,
    first_seen,
    search_city,
    search_country,
    "job level" as job_level,
    job_type,
    job_summary,
    job_skills

from {{ ref('br_jobs') }}