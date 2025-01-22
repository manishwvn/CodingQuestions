with friendships as (
    select
        *
    from
        friendship
    union
    select
        user2_id as user1_id,
        user1_id as user2_id
    from
        friendship
),

common_friendships as( 
    select
        c1.user1_id as user1_id,
        c2.user1_id as user2_id,
        count(c2.user2_id) as common_friend
    from
        friendships c1
    left join
        friendships c2
    on
        c1.user2_id = c2.user2_id
    and
        c1.user1_id < c2.user1_id
    group by
        c1.user1_id, c2.user1_id
    having
        count(c2.user2_id) >= 3)

select
    *
from
    common_friendships
where
    (user1_id, user2_id) in (select * from friendship);
    