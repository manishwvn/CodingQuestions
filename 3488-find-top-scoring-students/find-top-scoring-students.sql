with cte as (select
    s.*,
    c.course_id
from
    students s
join
    courses c
on
    s.major = c.major)

select
    c.student_id
from
    cte c
left join
    enrollments e
on
    c.student_id = e.student_id
    and
    c.course_id = e.course_id
group by
    c.student_id
having
    count(distinct c.course_id) = sum(case when e.grade = 'A' then 1 else 0 end);