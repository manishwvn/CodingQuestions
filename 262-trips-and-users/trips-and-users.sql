-- select
--     *
-- from
--     users u
-- where
--     u.banned = 'No';

select
    request_at as Day,
    round(sum(case when status <> 'completed' then 1 else 0 end) / count(*), 2) as 'Cancellation Rate'
from
    trips t
where
    client_id in (
        select
            users_id
        from
            users
        where
            role = 'client' and banned = 'No')
    and
    driver_id in (
        select
            driver_id
        from
            users
        where
            role = 'driver' and banned = 'No')
    and
        date(request_at) between date('2013-10-01') and date('2013-10-03')
group by
    Day;