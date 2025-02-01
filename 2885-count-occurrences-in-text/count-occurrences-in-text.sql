select
    'bull' as word,
    sum(case
            when content like '% bull %' then 1
            else 0
        end) as count
from
    files
union
select
    'bear' as word,
    sum(case
            when content like '% bear %' then 1
            else 0
        end) as count
from
    files;
