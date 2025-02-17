with cte as (select
    *
from
    friends
union
select
    user2 as user1,
    user1 as user2
from
    friends)

select
    user1,
    round(count(distinct user2) * 100.00 / (select count(distinct user1) from cte), 2)
        as percentage_popularity
from
    cte
group by
    user1