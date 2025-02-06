with shown as (
    select
        id,
        question_id,
        count(*) as num_shown
    from
        surveylog
    where
        action = 'show'
    group by
        id, question_id
),

answered as (
    select
        id, question_id, answer_id, count(*) as num_ans
    from
        surveylog
    where
        action = 'answer'
    group by
        id, question_id
)


select
    s.question_id as survey_log
from
    shown s
left join
    answered a
on
    s.id = a.id
    and
    s.question_id = a.question_id
order by
    coalesce(a.num_ans, 0) / s.num_shown desc, s.question_id asc
limit
    1;