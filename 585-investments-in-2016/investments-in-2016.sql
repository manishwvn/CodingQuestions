WITH SharedTivPolicies AS (
    -- CTE to get a distinct list of policies that share a tiv_2015 value
    -- with at least one other policy.
    SELECT DISTINCT
        p1.pid
    FROM
        Insurance p1
    JOIN
        Insurance p2 ON p1.tiv_2015 = p2.tiv_2015 AND p1.pid <> p2.pid

), UniqueLocationPolicies AS (
    -- CTE to get a list of policies that have a unique geo-location.
    -- This is done by finding policies that have no "other" partner in the same location.
    SELECT
        p1.pid
    FROM
        Insurance p1
    LEFT JOIN
        Insurance p2 ON p1.lat = p2.lat AND p1.lon = p2.lon AND p1.pid <> p2.pid
    WHERE
        p2.pid IS NULL
)
-- Final query to sum the tiv_2016 for policies that meet BOTH criteria
SELECT
    ROUND(SUM(i.tiv_2016), 2) AS tiv_2016
FROM
    Insurance i
-- Use INNER JOINs to find the intersection of policies that are in both our CTEs
JOIN
    SharedTivPolicies stp ON i.pid = stp.pid
JOIN
    UniqueLocationPolicies ulp ON i.pid = ulp.pid;