with cancelled_trips as (
    select
        t.request_at as day,
        case when t.status <> 'completed' then 1 else 0 end as cancelled
    from
        trips t
    join
        users u1
    on
        t.client_id = u1.users_id
        and
        u1.banned = 'No'
    join
        users u2
    on
        t.driver_id = u2.users_id
        and
        u2.banned = 'No'
    where
        date(request_at) between date('2013-10-01') and date('2013-10-03'))

select
    day,
    round(sum(cancelled) / count(cancelled), 2) as 'Cancellation Rate'
from
    cancelled_trips
group by day;