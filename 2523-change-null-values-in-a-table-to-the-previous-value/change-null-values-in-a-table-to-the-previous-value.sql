-- Step 1: Capture the original row order and create groups
WITH OrderedCoffeeShop AS (
    SELECT
        id,
        drink,
        -- Create a sequential number to represent the original, stable row order
        ROW_NUMBER() OVER() AS rn
    FROM
        CoffeeShop
),
GroupedDrinks AS (
    SELECT
        id,
        drink,
        rn,
        -- Create a running count that only increments for non-NULL drinks.
        -- IMPORTANT: This must be ordered by the original sequence (rn).
        COUNT(drink) OVER (ORDER BY rn) AS drink_group
    FROM
        OrderedCoffeeShop
)
-- Step 2: Fill the NULLs by taking the first value from each group
SELECT
    id,
    -- For each row, find the first 'drink' value within its calculated 'drink_group'
    FIRST_VALUE(drink) OVER (PARTITION BY drink_group ORDER BY rn) AS drink
FROM
    GroupedDrinks
ORDER BY
    rn; -- The final output must be sorted by the original sequence