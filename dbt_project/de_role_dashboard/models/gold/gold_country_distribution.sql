select
    search_country,
    count(*) as jobs

from {{ ref('slv_jobs') }}

group by search_country

order by jobs desc