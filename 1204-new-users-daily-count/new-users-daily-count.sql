with cte as(
    select
        user_id,
        activity_date,
        row_number() over(partition by user_id order by activity_date) as rnk
    from
        traffic
    where
        activity = 'login')

select
    activity_date as login_date,
    count(user_id) as user_count
from
    cte
where
    rnk = 1
and
    activity_date between date_sub('2019-06-30', interval 90 day) and date('2019-06-30')
group by
    login_date;