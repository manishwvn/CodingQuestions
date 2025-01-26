with recursive cte as (select
    v.*,
    t.amount
from
    visits v
left join
    transactions t
on
    v.user_id = t.user_id
    and
    v.visit_date = t.transaction_date),

cte2 as (
    select
        visit_date,
        user_id,
        sum(case when amount is null then 0 else 1 end) as trans
    from
        cte
    group by
        visit_date, user_id),

cte3 as (
    select 0 as trans
    union
    select trans + 1
    from
        cte3
    where
        trans < (select max(trans) from cte2))

select
    c3.trans as transactions_count,
    count(c2.user_id) as visits_count
from
    cte3 c3
left join
    cte2 c2
on
    c3.trans = c2.trans
group by
    c3.trans
order by
    1; 