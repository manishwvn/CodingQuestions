with cte as (select
    fail_date as date,
    'failed' as state
from
    failed
union
select
    success_date as date,
    'succeeded' as state
from
    succeeded),

cte2 as (
select
    *,
    row_number() over(partition by state order by date) as rnk
from
    cte),

cte3 as (
    select
        *,
        date_sub(date, interval rnk day) as grp
    from
        cte2
)

select
    state as period_state,
    min(date) as start_date,
    max(date) as end_date
from
    cte3
where
    year(date) = 2019
group by
    grp, state
order by
    start_date;