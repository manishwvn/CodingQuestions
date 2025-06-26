select
    r.contest_id,
    round((count(distinct r.user_id)*100/(select count(*) from Users)),2) as percentage
from
    register r 
join
    users u 
on
    r.user_id = u.user_id
group by
    r.contest_id
order by
    2 desc, 1 asc;