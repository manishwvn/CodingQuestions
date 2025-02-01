with cte as (select user_id1, user_id2
from friends 
union 
select user_id2 as user_id1, user_id1 as user_id2
from friends)

select user_id1, user_id2
from friends
where (user_id1, user_id2) not in (
    select f1.user_id1, f1.user_id2
    from friends f1 join cte c1 
    on f1.user_id1 = c1.user_id1 join cte c2 on f1.user_id2 = c2.user_id1
    where c1.user_id2 = c2.user_id2)
order by user_id1, user_id2