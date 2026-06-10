select *
from skill_frequency

where skill in (
    'aws',
    'azure',
    'gcp'
)