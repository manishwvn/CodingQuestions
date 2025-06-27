with cte as (select
    q1.*,
    sum(q2.weight) as cum_sum
from
    queue q1
left join
    queue q2
on
    q1.turn >= q2.turn
group by
    q1.person_id, q1.turn
having
    cum_sum <= 1000
order by
    cum_sum desc
limit 1)

select
    person_name from cte;