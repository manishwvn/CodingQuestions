with trials as (select
    user_id,
    round(avg(activity_duration), 2) as trial_avg_duration
from
    useractivity
where
    activity_type = 'free_trial'
group by
    user_id),

subscribes as (
    select
    user_id,
    round(avg(activity_duration), 2) as paid_avg_duration
from
    useractivity
where
    activity_type = 'paid'
group by
    user_id
)

select
    t.user_id,
    t.trial_avg_duration,
    s.paid_avg_duration
from
    trials t
join
    subscribes s
on
    t.user_id = s.user_id
order by 1;