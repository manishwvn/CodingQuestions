with cte as (
select
    case
        when user1_id = 1 then user2_id
        when user2_id = 1 then user1_id
        end as friends
from
    friendship)

select
    distinct page_id as recommended_page
from
    likes
where
    user_id in (select friends from cte)
    and
    page_id not in (select page_id from likes where user_id = 1)