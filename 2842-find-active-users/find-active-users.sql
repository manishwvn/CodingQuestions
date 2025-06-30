with cte as (
    select
        *,
        count(user_id) over(partition by user_id order by created_at range between interval 7 day preceding and current row) as roll_cnt
    from
        users
)

select distinct user_id from cte where roll_cnt > 1;