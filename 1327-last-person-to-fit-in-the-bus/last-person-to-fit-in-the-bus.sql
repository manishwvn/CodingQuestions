with cumulative_wts as (
select
    *,
    sum(weight) over(order by turn ) as cum_weight
from
    queue)

select person_name from cumulative_wts where cum_weight <= 1000 order by cum_weight desc limit 1;
    