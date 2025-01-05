select
    distinct 
    viewer_id as id
from
    views
group by
    view_date, viewer_id
having
    count(distinct article_id) > 1
order by
    id;


