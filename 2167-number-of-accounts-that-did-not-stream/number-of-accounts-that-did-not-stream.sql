select
    count(distinct a.account_id) as accounts_count
from
    subscriptions a
left join
    streams s
on
    a.account_id = s.account_id
where
    year(end_date) >= 2021
    and
    year(stream_date) <> 2021