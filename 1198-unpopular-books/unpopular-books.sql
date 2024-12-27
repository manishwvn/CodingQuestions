WITH MonthlyAvailableBooks AS (
    SELECT book_id
    FROM Books
    WHERE available_from >= DATE_SUB('2019-06-23', INTERVAL 1 MONTH)
),
OrdersInLastYear AS (
    SELECT book_id, SUM(quantity) AS total_quantity
    FROM Orders
    WHERE dispatch_date BETWEEN '2018-06-23' AND '2019-06-23'
    GROUP BY book_id
)
SELECT b.book_id, b.name
FROM Books b
LEFT JOIN OrdersInLastYear o ON b.book_id = o.book_id
WHERE b.book_id NOT IN (SELECT book_id FROM MonthlyAvailableBooks)
  AND (o.total_quantity IS NULL OR o.total_quantity < 10);