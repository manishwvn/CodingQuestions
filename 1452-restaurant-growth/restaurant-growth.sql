with cte as (
    select
        visited_on,
        sum(amount) as amount
    from
        customer
    group by
        visited_on)


select
    c1.visited_on,
    sum(c2.amount) as amount,
    round(avg(c2.amount), 2) as average_amount
from
    cte c1
join
    cte c2
on
    c1.visited_on >= c2.visited_on
where
    datediff(c1.visited_on, c2.visited_on) between 0 and 6
and
    c1.visited_on >= (select min(visited_on) + interval 6 day from customer)
group by
    c1.visited_on
order by
    c1.visited_on;