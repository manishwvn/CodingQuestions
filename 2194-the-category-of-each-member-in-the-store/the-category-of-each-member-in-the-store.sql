with cte as (
    select
        m.member_id,
        m.name,
        count(v.visit_id) as visit_counts,
        count(p.visit_id) as purchase_counts
    from
        members m
    left join
        visits v
    on
        m.member_id = v.member_id
    left join
        purchases p
    on
        p.visit_id = v.visit_id
    group by
        1, 2)

select
    member_id,
    name,
    case
        when
            visit_counts = 0 then 'Bronze'
        when
            (purchase_counts  * 100) / visit_counts < 50 then 'Silver'
        when
            (purchase_counts  * 100) / visit_counts >= 50 and (purchase_counts  * 100) / visit_counts < 80 then 'Gold'
        else
            'Diamond'
    end as category
from
    cte;