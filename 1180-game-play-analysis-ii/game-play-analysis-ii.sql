with first_logins as (
    select
        player_id,
        min(event_date) as min_date
    from
        activity
    group by
        1)

select
    f.player_id,
    a.device_id
from
    first_logins f
join
    activity a
on
    f.player_id = a.player_id
where
    f.min_date = a.event_date;