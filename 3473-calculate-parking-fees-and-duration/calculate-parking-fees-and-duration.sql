with cte as (select
    car_id,
    sum(fee_paid) as total_fee_paid,
    round(sum(fee_paid) / 
    (sum(timestampdiff(second,entry_time,exit_time))/3600),2) as avg_hourly_fee
from
    ParkingTransactions
group by
    car_id),

cte2 as(
    select
        car_id,
        lot_id,
        dense_rank() over(partition by car_id order by sum(timestampdiff(second,entry_time,exit_time))/3600 desc) as rnk
    from
        ParkingTransactions
    group by
        car_id, lot_id
),

cte3 as(
    select
        car_id,
        lot_id as most_time_lot
    from
        cte2
    where rnk = 1
)

select
    c1.car_id,
    c1.total_fee_paid,
    c1.avg_hourly_fee,
    c2.most_time_lot
from
    cte c1
join
    cte3 c2
on
    c1.car_id = c2.car_id
group by
    c1.car_id;