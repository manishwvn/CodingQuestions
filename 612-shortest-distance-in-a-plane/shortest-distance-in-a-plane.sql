with distinct_points as(
    select
        p1.x as x1,
        p1.y as y1,
        p2.x as x2,
        p2.y as y2
    from
        point2d p1
    join
        point2d p2
    where
        p1.x < p2.x OR (p1.x = p2.x AND p1.y < p2.y)
)

select
    round(min(sqrt(pow((x1-x2), 2) + pow((y1-y2),2))), 2) as shortest
from
    distinct_points;

