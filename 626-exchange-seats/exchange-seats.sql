-- if id is even then decrease by 1
-- if id is odd 
    -- and id = max then keep as it is
    -- else:
    --     id + 1

with cte2 as (
    select
        *,
        max(id) over() as max_id
    from
        seat
)
select
    case
        when id % 2 = 0 then id - 1
        when id % 2 = 1 and id = max_id then id
        else id + 1
    end as id,
    student
from
    cte2
order by
    1;
