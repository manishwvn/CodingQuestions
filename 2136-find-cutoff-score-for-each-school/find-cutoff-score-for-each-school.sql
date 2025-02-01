select
    s.school_id,
    coalesce(min(e.score), -1) as score
from
    schools s
left join
    exam e
on
    s.capacity >= e.student_count
group by
    s.school_id

