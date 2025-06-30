/*
1. cte union all departure_airport ,arrival_airport flights 
similar to friend request problem make it together
2. id, sum(flight count), rank and order by desc
3. come out and make rnk=1
*/
with cte as(
    select departure_airport id, flights_count from Flights 
    union all
    select arrival_airport  id, flights_count from Flights
),
cta as(
    select id ,sum(flights_count ) ,rank() over(order by sum(flights_count )desc)rnk
    from cte
    group by 1
)
select id airport_id 
from cta
where rnk=1