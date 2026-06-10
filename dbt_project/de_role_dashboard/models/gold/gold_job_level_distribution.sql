select
    job_level,
    count(*) as job_count

from {{ ref('slv_jobs') }}

group by job_level