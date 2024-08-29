with total_friend_requests as(
    select count(*) as total_count from(
        select distinct sender_id, send_to_id from FriendRequest
    ) 
),

total_accepted_requests as (
    select count(*) as accept_count from (
        select distinct requester_id, accepter_id from RequestAccepted
    )
)

select 
    case
        when total_count = 0 then 0.00
        else round((accept_count * 1.00 / total_count), 2) 
        end as accept_rate
from 
    total_accepted_requests, 
    total_friend_requests;