WITH CTE AS (
SELECT seller_id, SUM(price) AS total_price
  FROM Sales
 GROUP BY 1)
SELECT DISTINCT seller_id
  FROM CTE
 WHERE total_price = (SELECT MAX(total_price) FROM CTE) 