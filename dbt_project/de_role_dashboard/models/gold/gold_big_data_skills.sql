select *
from skill_frequency

where skill in (
    'spark',
    'pyspark',
    'kafka',
    'airflow',
    'snowflake'
)