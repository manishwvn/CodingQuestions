-- select
--     sum(select count(distinct session_id from activity)) / count(user_id)
-- from
--     activity
-- where
--     activity_date between date('2019-07-27') - INTERVAL 29 DAY and date('2019-07-27')
-- group by
--     user_id
-- having
--     count(activity_type) >= 1;

with user_sessions as(
select
    user_id,
    count(distinct session_id) unique_sessions
from
    activity
where
    activity_date between date('2019-07-27') - INTERVAL 29 DAY and date('2019-07-27')
group by
    user_id
having count(activity_type) >= 1)

select
    round(ifnull(sum(unique_sessions) / count(user_id), 0), 2) as average_sessions_per_user
from
    user_sessions;
