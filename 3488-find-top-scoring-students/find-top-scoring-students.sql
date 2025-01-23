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
    count(distinct c.course_id) = sum(if(e.grade = 'A',1,0));