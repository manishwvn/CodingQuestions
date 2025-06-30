WITH StadiumGroups AS (
    -- Step 1: Filter for valid days and create the grouping key 'diff'
    SELECT
        id,
        visit_date,
        people,
        -- This identifies each group of consecutive days
        id - ROW_NUMBER() OVER(ORDER BY id) AS diff
    FROM
        Stadium
    WHERE
        people >= 100
)
-- Step 2 & 3: Count the size of each group and filter
SELECT
    id,
    visit_date,
    people
FROM (
    -- Add a count of how many rows are in each 'diff' group
    SELECT
        *,
        COUNT(*) OVER(PARTITION BY diff) AS consecutive_days
    FROM
        StadiumGroups
) AS FinalCounts
WHERE
    consecutive_days >= 3
ORDER BY
    visit_date;