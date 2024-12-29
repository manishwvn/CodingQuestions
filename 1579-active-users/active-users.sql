with cte as (select
    distinct
        l.*,
        a.name
from
    logins l
left join
    accounts a
on
    l.id = a.id
order by 
    l.id, l.login_date),

cte2 as (
    select
        *,
        row_number() over(partition by id order by login_date) as rnk
    from
        cte)

select distinct id, name from (
select
    id,
    name,
    date_sub(login_date, interval rnk day) as diff
from
    cte2
group by
    id, name, diff
having count(*) >= 5) t ;