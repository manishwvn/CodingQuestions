WITH Type0Customers AS (
    -- Step 1: Find all unique customers who have at least one 'type 0' order.
    SELECT DISTINCT
        CUSTOMER_ID
    FROM
        ORDERS
    WHERE
        ORDER_TYPE = 0
)
SELECT
    o.*
FROM
    ORDERS o
-- Step 2: LEFT JOIN the main orders table against our list of 'type 0' customers.
LEFT JOIN
    Type0Customers t0 ON o.CUSTOMER_ID = t0.CUSTOMER_ID
WHERE
    -- Condition 1: Keep the row if it's a 'type 0' order itself.
    o.ORDER_TYPE = 0
    OR
    -- Condition 2: Keep the row if the join failed (i.e., the customer
    -- never placed a 'type 0' order).
    t0.CUSTOMER_ID IS NULL;