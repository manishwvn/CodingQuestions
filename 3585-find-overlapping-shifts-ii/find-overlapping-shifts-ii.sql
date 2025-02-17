with cte as (select
    e1.employee_id,
    e2.start_time, 
    e2.end_time,
    count(e1.employee_id) as counts,
    sum(case
        when e1.start_time <> e2.start_time then
            timestampdiff(minute, e1.start_time, e2.end_time)
        else 0
    end) as duration
from
    employeeshifts e1
join
    employeeshifts e2
on
    e1.employee_id = e2.employee_id
    and
    e1.start_time between e2.start_time and e2.end_time
group by
    e1.employee_id, e1.start_time)

select
    employee_id,
    max(counts) as max_overlapping_shifts,
    sum(duration) as total_overlap_duration
from
    cte
group by
    employee_id