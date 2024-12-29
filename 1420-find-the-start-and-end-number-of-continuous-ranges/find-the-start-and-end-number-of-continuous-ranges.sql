with rnks as (
    select
        log_id,
        log_id - row_number() over(order by log_id) as rnk
    from
        logs)

select
    min(log_id) as start_id,
    max(log_id) as end_id
from
    rnks
group by
    rnk
order by
    start_id;