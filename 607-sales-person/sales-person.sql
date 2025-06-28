SELECT
    s.name
FROM
    salesperson s
LEFT JOIN
    orders o ON s.sales_id = o.sales_id
LEFT JOIN
    company c ON o.com_id = c.com_id AND c.name = 'RED'
group by
    s.sales_id, s.name
HAVING
    COUNT(c.com_id) = 0;