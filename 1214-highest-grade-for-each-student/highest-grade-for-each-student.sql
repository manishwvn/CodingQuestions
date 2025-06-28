with cte as (select
    student_id, 
    max(grade) as max_grade
from
    Enrollments
group by
    1)

select
    e.student_id,
    min(e.course_id) as course_id,
    e.grade
from
    Enrollments e 
join
    cte c 
on
    e.student_id = c.student_id
    and
    e.grade = c.max_grade
group by
    e.student_id, e.grade
order by
    e.student_id