with cte as (select
    first_player as player_id,
    first_score as score
from
    matches
union all
select
    second_player as player_id,
    second_score as score
from
    matches),

cte2 as (
    select
        player_id,
        sum(score) as total_score
    from
        cte
    group by
        player_id
),

cte3 as (
select 
    c.*,
    p.group_id,
    dense_rank() over(partition by group_id order by c.total_score desc, c.player_id asc) as rnk
from 
    cte2 c
join
    players p
on
    c.player_id = p.player_id)

select
    group_id,
    player_id
from
    cte3
where
    rnk = 1