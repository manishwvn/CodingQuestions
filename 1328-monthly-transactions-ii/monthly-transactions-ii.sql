with approvals as (
select
    date_format(t.trans_date, '%Y-%m') as month,
    t.country as country,
    sum(case when t.state = 'approved' then 1 else 0 end) as approved_count,
    sum(case when t.state = 'approved' then amount else 0 end) as approved_amount
from
    transactions t
group by
    month, country),

charges as (
    select
        date_format(c.trans_date, '%Y-%m') as month,
        t.country,
        count(*) as chargeback_count,
        sum(t.amount) as chargeback_amount
    from
        chargebacks c
    left join
        transactions t
    on
        c.trans_id = t.id
    group by
        month, country
),

result as (
    select
        a.month,
        a.country,
        a.approved_count,
        a.approved_amount,
        ifnull(c.chargeback_count, 0) as chargeback_count,
        ifnull(c.chargeback_amount, 0) as chargeback_amount
    from
        approvals a
    left join
        charges c
    on
        a.month = c.month and a.country = c.country
    union
    select
        c.month,
        c.country,
        ifnull(a.approved_count, 0) as approved_count,
        ifnull(a.approved_amount, 0) as approved_amount,
        ifnull(c.chargeback_count, 0) as chargeback_count,
        ifnull(c.chargeback_amount, 0) as chargeback_amount
    from
        approvals a
    right join
        charges c
    on
        a.month = c.month and a.country = c.country)

select * from result
    where approved_count+approved_amount+chargeback_count+chargeback_amount <> 0;