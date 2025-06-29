with cte as (select
    p.player_id, p.player_name, sum(c.wimbledon = p.player_id) as wim_wins,
    sum(c.fr_open = p.player_id) as fr_wins,
    sum(c.us_open = p.player_id) as us_wins,
    sum(c.au_open = p.player_id) as au_wins
from
    players p 
cross join
    championships as c
group by
    1,2)

select
    player_id,
    player_name,
    (wim_wins + fr_wins + us_wins + au_wins) as grand_slams_count
from
    cte
where
    wim_wins + fr_wins + us_wins + au_wins > 0;