select
    floor((day(purchase_date) - 1) / 7) + 1 as week_of_month,
    purchase_date,
    sum(amount_spend) as total_amount
from
    purchases
where
    dayofweek(purchase_date) = 6
    and
    month(purchase_date) = 11
    and
    year(purchase_date) = 2023
group by
    week_of_month
order by
    week_of_month