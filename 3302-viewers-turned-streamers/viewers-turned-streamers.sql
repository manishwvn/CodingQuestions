# Write your MySQL query statement below
with data as (select *,
rank() over(partition by user_id order by session_start) as rnk
from sessions),

data2 as (select a.*
    from data a join data b
    on a.user_id=b.user_id
    and a.rnk=1
    -- and b.rnk <> 1
    and a.session_type='Viewer'
    and b.session_type='Streamer')
select user_id, count(*) as sessions_count from data2
group by 1
order by 2 desc,1 desc