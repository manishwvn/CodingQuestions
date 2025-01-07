with apples as (select
    sum(case
        when 
            b.chest_id is null then apple_count
        else
            b.apple_count + (select c.apple_count from chests c where c.chest_id = b.chest_id)
    end) as apple_count
from
    boxes b),

oranges as (
    select
        sum(case
            when 
                b.chest_id is null then orange_count
            else
                b.orange_count + (select c.orange_count from chests c where c.chest_id = b.chest_id)
        end) as orange_count
    from
        boxes b
)

select
    apple_count,
    orange_count
from
    apples, oranges;