with recursive cte as (
    select task_id, subtasks_count from tasks
    union
    select task_id, subtasks_count - 1 from cte where subtasks_count > 1

)

select
    task_id,
    subtasks_count as subtask_id
from
    cte
where
    (task_id, subtasks_count) not in (
        select * from executed
    )