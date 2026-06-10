select
    company,
    count(*) as jobs_posted

from {{ ref('slv_jobs') }}

group by company

order by jobs_posted desc