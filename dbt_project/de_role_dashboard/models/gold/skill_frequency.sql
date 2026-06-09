with skills as (

    select
        year(first_seen) as job_year,
        unnest(
            string_split(job_skills, ',')
        ) as skill

    from {{ ref('slv_jobs') }}

    where job_skills is not null

)

select
    job_year,
    trim(skill) as skill,
    count(*) as frequency

from skills

group by
    job_year,
    trim(skill)

order by
    job_year,
    frequency desc