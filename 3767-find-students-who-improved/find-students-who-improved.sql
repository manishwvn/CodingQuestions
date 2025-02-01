with cte as (select
    *,
    dense_rank() over(partition by student_id, subject order by exam_date asc) as first_rnk,
    dense_rank() over(partition by student_id, subject order by exam_date desc) as latest_rnk
from
    scores),

first as (
select
    student_id,
    subject,
    score as first_score
from
    cte
where
    first_rnk = 1),

latest as (
    select
        student_id,
        subject,
        score as latest_score
    from
        cte
    where
        latest_rnk = 1
)

select
    f.student_id, f.subject, f.first_score, l.latest_score
from
    first f
join
    latest l
on
    f.student_id = l.student_id and f.subject = l.subject
where
    l.latest_score > f.first_score
order by
    1, 2;

