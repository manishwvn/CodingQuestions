select results from (select
    u.name as results
from
    users u
join
    movierating mr 
on
    u.user_id = mr.user_id
group by
    u.name
order by
    count(distinct mr.movie_id) desc, u.name asc
limit
    1) as t1
union all
select results from (select
    m.title as results
from
    movies m 
join
    movierating mr
on
    m.movie_id = mr.movie_id
where
    month(mr.created_at) = 2 and year(created_at) = 2020
group by
    m.title
order by
    avg(mr.rating) desc, m.title asc
limit 1) as t2;