SELECT
  c.customer_id
FROM
  Customer c
join
    product p
on
    c.product_key = p.product_key
GROUP BY
  customer_id
HAVING
  COUNT(DISTINCT c.product_key) = (
    SELECT
      COUNT(product_key)
    FROM
      Product
  );