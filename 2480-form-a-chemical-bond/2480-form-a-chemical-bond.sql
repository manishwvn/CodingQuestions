select
    m.symbol as metal,
    nm.symbol as nonmetal
from
    elements m
cross join
    elements nm
where
    m.type = 'Metal' and nm.type = 'Nonmetal';