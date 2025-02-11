with id_comb as(
    select
        requester_id as id,
        accepter_id as friend_id
    from
        requestaccepted
    union all
    select
        accepter_id,
        requester_id
    from
        requestaccepted
),
cte2 as (
select
    id,
    count(friend_id) as num,
    dense_rank() over(order by count(friend_id) desc) as rnk
from
    id_comb
group by
    id)

select
    id, num
from
    cte2
where
    rnk = 1;