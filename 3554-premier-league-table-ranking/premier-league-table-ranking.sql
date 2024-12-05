with team_points as(
select
    team_id,
    team_name,
    (wins * 3) + (draws * 1) + (losses * 0) as points
from
    teamstats)

select
    *,
    rank() over(order by points desc) as position
from
    team_points
order by
    points desc, team_name asc;