select
    s1.score,
    count(distinct s2.score) as 'rank'
from
    scores s1
join
    scores s2
on
    s1.score <= s2.score
group by
    s1.id,
    s1.score
order by
    s1.score desc;