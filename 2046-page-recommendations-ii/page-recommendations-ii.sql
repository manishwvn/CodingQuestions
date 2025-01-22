with cte as (
    select
        user1_id,
        user2_id
    from
        friendship
    union
    select
        user2_id,
        user1_id
    from
        friendship
),

cte2 as (
    select
        c.user1_id,
        c.user2_id,
        l.page_id
    from
        cte c
    left join
        likes l
    on
        c.user2_id = l.user_id),

cte3 as (
    select
        user1_id as user_id,
        page_id,
        count(user2_id) as friends_likes
    from
        cte2
    group by
        user1_id,
        page_id)

select
    c.*
from
    cte3 c
left join
    likes l
on
    c.user_id = l.user_id
    and
    c.page_id = l.page_id
where
    l.page_id is null;