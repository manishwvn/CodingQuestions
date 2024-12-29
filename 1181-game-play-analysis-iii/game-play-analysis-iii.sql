select
    a.player_id,
    a.event_date,
    sum(a.games_played) over(partition by (player_id) order by event_date)
        as games_played_so_far
from
    activity a
group by
    1, 2
order by
    1, 2;