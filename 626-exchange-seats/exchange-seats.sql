-- if id is even then decrease by 1
-- if id is odd 
    -- and id = max then keep as it is
    -- else:
    --     id + 1
with cte as (select
    *,
    case
        when id % 2 = 0 then id - 1
        when id % 2 = 1 and id = (select max(id) from seat) then id
        else id + 1
    end as new_id
from
    seat)

select
    new_id as id,
    student
from
    cte
order by
    new_id;