with points_order as (
    select
        *,
        row_number() over() as pt_order
    from
        point2d
)

select
    min(round(sqrt(pow((o1.x - o2.x),2) + pow((o1.y - o2.y), 2)), 2)) as shortest
from
    points_order o1
join
    points_order o2
on
    o1.pt_order < o2.pt_order