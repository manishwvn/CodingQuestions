with cte as (select
    l.book_id,
    l.title,
    l.author,
    l.genre,
    l.publication_year,
    l.total_copies,
    count(b.record_id) as current_borrowers
from
    library_books l
join
    borrowing_records b
on
    l.book_id = b.book_id
where
    return_date is NULL
group by
    1,2,3,4,5)

select
    book_id,
    title,
    author,
    genre,
    publication_year,
    current_borrowers
from
    cte
where
    total_copies - current_borrowers = 0
order by
    current_borrowers desc, title asc;

