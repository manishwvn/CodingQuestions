with followers as(
    select
        followee,
        count(*) as follower_count
    from
        follow
    group by
        followee
    having follower_count >= 1
),

followees as(
    select
        follower,
        count(*) as followee_count
    from
        follow
    group by
        follower
    having followee_count >= 1
)

select
    fe.follower,
    fr.follower_count as num
from
    followers fr
join
    followees fe
on
    fr.followee = fe.follower
order by
    fe.follower;