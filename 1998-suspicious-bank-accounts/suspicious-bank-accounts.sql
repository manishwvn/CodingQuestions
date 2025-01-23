with cte as(
select
    t.account_id,
    sum(t.amount) as income,
    month(day) as month,
    row_number() over(partition by a.account_id order by month(t.day)) as row_num,
    a.max_income
from
    transactions t
left join
    accounts a
on
    t.account_id = a.account_id
where
    type = 'Creditor'
group by
    account_id, month
having
    income > max_income
order by
    account_id),

cte2 as (
    select
        c1.account_id,
        c1.income,
        c1.month,
        c2.month as next_month,
        c1.max_income
    from
        cte c1
    left join
        cte c2
    on
        c1.account_id = c2.account_id
        and
        c1.row_num + 1 = c2.row_num
)

select
    distinct account_id
from
    cte2
where
    next_month - month = 1;