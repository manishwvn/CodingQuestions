select
    s.id, s.name
from
    departments d
right join
    students s
on
    d.id = s.department_id
where
    d.id is null