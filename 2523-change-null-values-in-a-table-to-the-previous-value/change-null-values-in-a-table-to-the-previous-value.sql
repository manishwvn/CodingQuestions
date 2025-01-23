with cte as (select
    *,
    row_number() over() as row_num,
    (case when drink is null then 0 else 1 end) as assign
from
    coffeeshop),

cte2 as (
    select
        *,
        sum(assign) over(order by row_num rows between unbounded preceding and current row) as assign_sum
    from
        cte
),

cte3 as (
    select
        *,
        first_value(drink) over(partition by assign_sum order by row_num) as def_drnk
    from
        cte2)
select
    id, def_drnk as drink from cte3;