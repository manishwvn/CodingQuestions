-- Step 1: We must first create a stable, sequential row number.
WITH recursive OrderedCoffeeShop AS (
    SELECT
        id,
        drink,
        ROW_NUMBER() OVER() AS rn
    FROM
        CoffeeShop
),

-- Step 2: Use a recursive CTE to carry the value forward row by row.
RecursiveFill AS (
    -- Anchor Member: Start with the very first row.
    SELECT
        id,
        drink,
        rn
    FROM
        OrderedCoffeeShop
    WHERE
        rn = 1

    UNION ALL

    -- Recursive Member: Join the next row and fill the NULL if needed.
    SELECT
        curr.id,
        -- If the current drink is NULL, use the previous row's drink.
        COALESCE(curr.drink, prev.drink) AS drink,
        curr.rn
    FROM
        OrderedCoffeeShop curr
    JOIN
        RecursiveFill prev ON curr.rn = prev.rn + 1
)
SELECT
    id,
    drink
FROM
    RecursiveFill
ORDER BY
    rn;