WITH invoice_totals AS (
    SELECT
        o.invoice_id,
        SUM(p.price * o.quantity) AS total_price
    FROM purchases o
    JOIN products p ON o.product_id = p.product_id
    GROUP BY o.invoice_id
),
ranked_invoices AS (
    SELECT 
        invoice_id,
        total_price,
        RANK() OVER (ORDER BY total_price DESC, invoice_id ASC) AS rnk
    FROM invoice_totals
)
SELECT 
    o.product_id,
    o.quantity,
    (p.price * o.quantity) AS price
FROM purchases o
JOIN products p ON o.product_id = p.product_id
WHERE o.invoice_id = (
    SELECT invoice_id FROM ranked_invoices WHERE rnk = 1
);