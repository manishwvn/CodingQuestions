with cte as (select
        *
    from
        schools s
    left join
        exam e
    on
        s.capacity >= e.student_count),

cte2 as (
select
    school_id,
    score,
    dense_rank() over(partition by school_id order by capacity desc, score) as rnk
from
    cte)

select
    school_id, coalesce(score,-1) as score from cte2 where rnk = 1;