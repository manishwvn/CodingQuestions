with cte as (select
    r1.user_id as user1_id,
    r2.user_id as user2_id,
    r1.follower_id as follower,
    count(distinct r1.follower_id) as common
from
    relations r1
join
    relations r2
on
    r1.user_id < r2.user_id
    and
    r1.follower_id = r2.follower_id
group by
    r1.user_id, r2.user_id)

select
    user1_id, user2_id from (
    select
        user1_id,
        user2_id,
        rank() over(order by common desc) as rnk
    from
        cte) t
    where t.rnk = 1;
