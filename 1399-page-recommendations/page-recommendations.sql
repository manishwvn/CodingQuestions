with cte as (
    select
        *
    from
        friendship
    where
        user1_id = 1
        or
        user2_id = 1
)

select
    distinct l.page_id as recommended_page
from
    likes l 
join
    cte c 
on
    l.user_id = c.user1_id
    or
    l.user_id = c.user2_id
where
    l.page_id not in (select distinct page_id from likes where user_id = 1)
    