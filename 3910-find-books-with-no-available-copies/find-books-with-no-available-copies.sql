with borrowed_counts as (
    select
        book_id,
        count(*) as borrowed_copies
    from
        borrowing_records
    where
        return_date is NULL
    group by
        book_id
)

select
    l.book_id,
    l.title,
    l.author,
    l.genre,
    l.publication_year,
    b.borrowed_copies as current_borrowers
from
    library_books l 
join
    borrowed_counts b
on
    l.book_id = b.book_id
where
    l.total_copies = b.borrowed_copies
order by
    current_borrowers DESC,
    l.title ASC;
