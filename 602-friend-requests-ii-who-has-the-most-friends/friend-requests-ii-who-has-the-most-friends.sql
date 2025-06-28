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
)

select
    id,
    count(distinct friend_id) as num
from
    id_comb
group by
    id
order by
    num desc
limit 1;