with cte as (
    select
        caller_id,
        recipient_id,
        call_time
    from
        calls
    union
    select
        recipient_id,
        caller_id,
        call_time
    from
        calls
),
cte2 as (
    select 
        *,
        dense_rank() over(partition by caller_id, date(call_time) order by call_time asc) as first_rnk,
        dense_rank() over(partition by caller_id, date(call_time) order by call_time desc) as last_rnk
    from cte)

select
    distinct caller_id as user_id
from
    cte2
where
    first_rnk = 1
    or last_rnk = 1
group by
    user_id, date(call_time)
having
    count(distinct recipient_id) = 1

