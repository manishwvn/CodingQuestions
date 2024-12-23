select
    distinct c.title as TITLE
from
    tvprogram t
join
    content c
on
    t.content_id = c.content_id
where
    month(t.program_date) = 6 
    and 
    year(t.program_date) = 2020
    and
    c.kids_content = 'Y'
    and
    c.content_type = 'Movies';
