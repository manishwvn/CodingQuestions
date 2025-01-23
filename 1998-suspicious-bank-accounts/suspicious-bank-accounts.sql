-- total income > max_income for two or 3 consecutive months
-- total income  = deposit type = creditor
with cte as(
select
    t.account_id,
    sum(t.amount) as income,
    month(day) as month,
    lead(month(t.day)) over(partition by a.account_id order by month(t.day)) as next_month,
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
    account_id)

select
    distinct account_id
from
    cte
where
    next_month - month = 1;

-- select
--     account_id,
--     amount,
--     month - rnk,
--     max_income
-- from
--     cte
-- group by
--     month - rnk