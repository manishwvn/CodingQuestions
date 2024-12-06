select
    artist,
    count(artist) as occurrences
from
    spotify
group by
    artist
order by
    2 desc, 1 asc;