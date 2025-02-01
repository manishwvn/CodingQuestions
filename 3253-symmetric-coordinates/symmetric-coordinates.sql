# Write your MySQL query statement below
with c as(select *, 
row_number() over(order by x) as rn
from coordinates)


select distinct  c1.x,c1.y 
from c as c1 
join c as c2
on c1.x=c2.y 
and c1.y=c2.x
and c1.x<=c1.y
and c1.rn!=c2.rn
order by c1.x,c1.y




