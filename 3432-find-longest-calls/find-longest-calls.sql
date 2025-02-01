with cte as (select
    c2.first_name,
    c1.type,
    c1.duration,
    dense_rank() over(partition by type order by duration desc) as rnk
from
    calls c1
join
    contacts c2
on
    c1.contact_id = c2.id)

select
    first_name,
    type,
    CONCAT(lpad(cast(floor(duration / 3600) as char(2)), 2, '0'), ':',
    lpad(cast(mod(floor(duration / 60), 60) as char(2)), 2, '0'), ':', 
    lpad(cast(mod(duration, 60) as char(2)), 2, '0')) as duration_formatted
from
    cte where rnk <= 3
order by
    type desc,
    duration_formatted desc,
    first_name desc;