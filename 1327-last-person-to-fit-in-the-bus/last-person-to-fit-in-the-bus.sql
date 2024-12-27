with cumulative_wts as (
select
    *,
    sum(weight) over(order by turn rows between unbounded preceding and current row) as cum_weight
from
    queue)

select person_name from cumulative_wts where cum_weight <= 1000 order by cum_weight desc limit 1;
    