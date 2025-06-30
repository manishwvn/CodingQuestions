--  for each task there is a subtasks (subtask 1, 2, 3 ... 20) such that each task has subtask count (2 ... 20)

--  from eg.
--  for task = 1, subtask count = 3 and subtask = 2 executed -> 1, 3 not executed so need to display these

-- key step -> convert tasks table in the form of (task_id, subtask_id) based on the number of counts.

with recursive cte as(
    select
        task_id,
        1 as subtask_id
    from
        tasks
    union all
    select
        c.task_id,
        c.subtask_id + 1
    from
        cte c
    join
        tasks t
    on
        c.task_id = t.task_id
    where
        c.subtask_id < t.subtasks_count
)

select
    c.task_id,
    c.subtask_id
from
    cte c 
left join
    executed e
on
    c.task_id = e.task_id
    and
    c.subtask_id = e.subtask_id
where
    e.subtask_id is null
order by
    1, 2
