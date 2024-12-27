with id_comb as (
    select
        requester_id as id,
        accepter_id
    from
        requestaccepted
    union
    select
        accepter_id as id,
        requester_id
    from
        requestaccepted)

select
    id,
    count(distinct accepter_id) as num
from
    id_comb
group by id
order by num desc
limit 1