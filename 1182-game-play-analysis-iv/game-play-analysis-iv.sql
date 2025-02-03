with login_ranks as (select
    *,
    dense_rank() over(partition by player_id order by event_date) as login_rank
from
    activity
),

first_logins as(
    select
        player_id,
        event_date as first_login
    from
        login_ranks
    where
        login_rank = 1
),

second_logins as (
    select
        player_id,
        event_date as second_login
    from
        login_ranks
    where
        login_rank = 2
)

select
    round(count(*) / (select count(distinct player_id) from activity), 2) as fraction
from
    first_logins fl
join
    second_logins sl
on
    fl.player_id = sl.player_id
where
    sl.second_login = fl.first_login + interval '1' day;