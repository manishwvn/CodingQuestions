select
    r.contest_id,
    round(count(distinct u.user_id) / (select count(1) from users) * 100, 2) as percentage
from
    register r
left join
    users u
on
    r.user_id = u.user_id
group by
    r.contest_id
order by
    percentage desc, r.contest_id asc;
    