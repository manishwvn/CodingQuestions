
with cte as (select *, row_number() over(partition by email order by id) as r from person)

delete from person where id not in (select id from cte where r=1);
