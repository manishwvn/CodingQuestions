with recursive cte as (
    select
        *, 0 as hierarchy_level
    from
        employees
    where
        manager_id is null

    union all

    select
        e.*,
        c.hierarchy_level + 1
    from
        employees e
    join
        cte c
    on
        e.manager_id = c.employee_id
)

select
    employee_id as subordinate_id,
    employee_name as subordinate_name,
    hierarchy_level,
    salary - (select salary from employees where manager_id is null) as salary_difference
from
    cte
where
    hierarchy_level > 0
order by
    hierarchy_level, subordinate_id;