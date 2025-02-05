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
        first_value(recipient_id) over(partition by caller_id, date(call_time) order by call_time asc) as first_call,
        first_value(recipient_id) over(partition by caller_id, date(call_time) order by call_time desc) as last_call
    from cte)

select
    distinct caller_id as user_id
from
    cte2
where
    first_call = last_call;

