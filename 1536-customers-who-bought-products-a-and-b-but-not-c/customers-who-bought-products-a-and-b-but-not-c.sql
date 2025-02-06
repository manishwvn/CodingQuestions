SELECT c.customer_id, c.customer_name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
HAVING SUM(CASE WHEN product_name = 'A' THEN 1 ELSE 0 END) > 0
    AND SUM(CASE WHEN product_name = 'B' THEN 1 ELSE 0 END) > 0
    AND SUM(CASE WHEN product_name = 'C' THEN 1 ELSE 0 END) = 0
ORDER BY c.customer_id;