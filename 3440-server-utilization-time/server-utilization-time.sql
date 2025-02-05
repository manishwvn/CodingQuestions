with starts as (select
    server_id,
    status_time as start_time,
    row_number() over (partition by server_id order by status_time) as start
from servers
where 
    session_status = "start"
order by 1, 2),

ends as (select
    server_id,
    status_time as end_time,
    row_number() over (partition by server_id order by status_time) as end
from servers
where 
    session_status = "stop"
order by 1, 2
),

total_time as (
select
    s.server_id,
    sum(timestampdiff(second, s.start_time, e.end_time)) as run_time
from
    starts s
join
    ends e
on
    s.server_id = e.server_id
    and
    s.start = e.end
group by
    s.server_id)

select
    floor((sum(run_time)/3600)/24) as total_uptime_days
from
    total_time;