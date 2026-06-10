with exploded_skills as (

    select
        trim(
            unnest(
                string_split(job_skills, ',')
            )
        ) as skill

    from {{ ref('slv_jobs') }}

    where job_skills is not null

)

select
    lower(skill) as skill,
    count(*) as frequency

from exploded_skills

where skill <> ''

group by lower(skill)

order by frequency desc