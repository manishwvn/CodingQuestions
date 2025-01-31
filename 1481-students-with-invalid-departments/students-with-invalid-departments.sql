select
    s.id, s.name
from
    students s
left join
    departments d
on
    d.id = s.department_id
where
    d.id is null