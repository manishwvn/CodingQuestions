with cte as(    select
        *,
        id - row_number() over(order by id) as diff
    from
        stadium
    where
        people >= 100),

cte2 as(
    select
        diff
    from
        cte
    group by
        diff
    having
        count(*) >= 3)

select
    id, visit_date, people
from
    cte
where
    diff in (select * from cte2)
order by
    visit_date