select
    t1.n as N,
    case
        when
            t1.p is null then 'Root'
        when
            not exists (select 1 from tree t2 where t2.p = t1.n) then 'Leaf'
        else
            'Inner'
    end as Type
from
    tree t1
order by
    1;