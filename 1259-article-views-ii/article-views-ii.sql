select
    distinct v1.viewer_id as id
from
    views v1
join
    views v2
on
    v1.viewer_id = v2.viewer_id
and
    v1.view_date = v2.view_date
and
    v1.article_id < v2.article_id
order by
    v1.viewer_id