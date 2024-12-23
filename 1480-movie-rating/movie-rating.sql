with user_ratings as (
    select
        u.name as name
    from
        users u
    join
        MovieRating mr
    on
        u.user_id = mr.user_id
    group by
        1
    order by
        count(*) desc, name asc
    limit 1
    ),

rating_avgs as (
    select
        m.title as title
    from
        movies m
    join
        MovieRating mr
    on
        m.movie_id = mr.movie_id
    where
        month(created_at) = 2 and year(created_at) = 2020
    group by
        title
    order by
        avg(rating) desc, title asc
    limit 1
    )

select
    name as results
from
    user_ratings
union all
select
    title as results
from
    rating_avgs;
