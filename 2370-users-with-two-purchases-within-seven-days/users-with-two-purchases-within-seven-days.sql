select 
    distinct p1.user_id
from 
    purchases p1
inner join
    purchases p2
on 
    p1.user_id=p2.user_id 
    and p1.purchase_id<>p2.purchase_id
    and abs(datediff(p1.purchase_date, p2.purchase_date))<=7
order by 
    p1.user_id