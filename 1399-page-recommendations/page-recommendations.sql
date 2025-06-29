select
    distinct l.page_id as recommended_page
from
    likes l 
join
    friendship f
on
    (l.user_id = f.user1_id and f.user2_id = 1)
    or
    (l.user_id = f.user2_id and f.user1_id = 1)
left join
    likes l1
on
    l1.page_id = l.page_id
    and
    l1.user_id = 1
where
    l1.user_id is null