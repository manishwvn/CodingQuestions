SELECT
    sp.salesperson_id,
    sp.name,
    coalesce(SUM(s.price), 0) AS total
FROM
    salesperson sp
LEFT JOIN
    customer c ON sp.salesperson_id = c.salesperson_id
LEFT JOIN
    sales s ON c.customer_id = s.customer_id
GROUP BY
    sp.salesperson_id;