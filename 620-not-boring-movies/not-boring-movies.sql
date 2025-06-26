SELECT
    *
FROM
    CINEMA
WHERE
    ID % 2 <> 0
AND lower(description) not like '%boring%'
ORDER BY RATING DESC;