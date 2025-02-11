with voted as (
    select
        candidateId,
        count(candidateId) as votes
    from
        vote
    group by
        candidateId),

results as (
    select
        name,
        dense_rank() over(order by votes desc) as rnk
    from
        candidate c
    join
        voted v
    on
        c.id = v.candidateId
)
select
    name
from
    results
where
    rnk = 1;