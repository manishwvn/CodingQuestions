with cte as (select
    *,
    rank() over(partition by department_id order by mark desc) as student_rank,
    count(student_id) over(partition by department_id) as student_count
from
    students)

select
    student_id,
    department_id,
    case
        when
            student_count = 1 then 0.00
        else
            round(((student_rank - 1) * 100) / (student_count - 1), 2) 
    end as percentage
from
    cte

-- select * from cte;