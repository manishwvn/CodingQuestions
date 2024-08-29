select
    question_id as survey_log
from
    SurveyLog
group by 
    question_id
order by
    coalesce(sum(
        case when action = 'answer' then 1 else 0 end
    )::decimal / 
    nullif(sum(
        case when action = 'show' then 1 else 0 end
    ),0), 0) desc,
    question_id asc
limit 1;