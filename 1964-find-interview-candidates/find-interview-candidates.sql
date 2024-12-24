with condition_2 as (
select
    gold_medal as user_id
from
    contests
group by
    gold_medal
having
    count(*) >= 3),

condition_1_a as(
    select
        gold_medal as user_id,
        contest_id
    from
        contests
    union
    select
        silver_medal as user_id,
        contest_id
    from
        contests
    union
    select
        bronze_medal as user_id,
        contest_id
    from
        contests
),

condition_1_b as (
    select
        *,
        row_number() over(partition by user_id order by contest_id) as rnk
    from
        condition_1_a
),

condition_1 as (
    select 
        distinct user_id
    from 
        condition_1_b
    group by 
        user_id, contest_id - rnk
    having
        count(*) >= 3
)

select
    u.name,
    u.mail
from
    users u
join
    condition_1 c1
on
    u.user_id = c1.user_id
union
select
    u.name,
    u.mail
from
    users u
join
    condition_2 c2
on
    u.user_id = c2.user_id;




