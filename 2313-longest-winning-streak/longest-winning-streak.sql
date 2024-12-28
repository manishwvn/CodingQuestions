with cte as(
    select
        *,
        row_number() over(partition by player_id order by match_day) as match_seq,
        row_number() over(partition by player_id, result order by match_day) as result_seq
    from
        matches),

cte2 as (
    select
        *,
        match_seq - result_seq as diff,
        count(*) as streak,
        row_number() over(partition by player_id order by count(*) desc) as rnk
    from
        cte
    where
        result = 'Win'
    group by
        player_id, match_seq - result_seq)


select
    distinct
        m.player_id,
        ifnull(c.streak, 0) as longest_streak
from
    matches m
left join
    (
        select
            player_id, streak
        from
            cte2
        where rnk = 1
    ) c
on
    m.player_id = c.player_id
