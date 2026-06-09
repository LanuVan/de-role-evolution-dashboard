select
 lower(job_title) as job_title,
 description
from {{ ref('br_jobs') }}