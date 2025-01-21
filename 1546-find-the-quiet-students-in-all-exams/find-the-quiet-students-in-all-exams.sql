with cte as (select
    exam_id,
    min(score) as min_score,
    max(score) as max_score
from
    exam
group by
    exam_id),

cte2 as (select
    distinct student_id
from
    exam e
join
    cte c
on
    e.exam_id = c.exam_id
    and (
    e.score = c.min_score
    or
    e.score = c.max_score))

select
    student_id, student_name
from
    student
where
    student_id in (select distinct student_id from exam)
    and
    student_id not in (select student_id from cte2)
order by 1;

-- select
--     *
-- from
--     exam e
-- join
--     cte c
-- on
--     e.exam_id = c.exam_id
-- where
--     e.score <> c.min_score 
--     and 
--     e.score <> c.max_score
