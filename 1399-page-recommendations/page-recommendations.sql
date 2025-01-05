select
    distinct page_id as recommended_page
from
    friendship f
join
    likes l
on
    (l.user_id = f.user2_id
    and
    f.user1_id = 1)
    or
    (l.user_id = f.user1_id
    and
    f.user2_id = 1)
where
    l.page_id not in (select distinct page_id from likes where user_id = 1)