-- CTE 1: Prepare the data by ranking reviews and getting the previous two ratings
WITH PreparedReviews AS (
    SELECT
        employee_id,
        rating AS latest_rating,
        -- Use LAG with ASC order to get the 2nd and 3rd latest ratings
        LAG(rating, 1) OVER (PARTITION BY employee_id ORDER BY review_date ASC) AS second_latest_rating,
        LAG(rating, 2) OVER (PARTITION BY employee_id ORDER BY review_date ASC) AS third_latest_rating,
        -- Use RANK with DESC order to identify the most recent review
        RANK() OVER (PARTITION BY employee_id ORDER BY review_date DESC) AS ranking
    FROM
        performance_reviews
),

-- CTE 2: Filter for the correct row and check the improvement condition
ImprovingEmployees AS (
    SELECT
        employee_id,
        latest_rating - third_latest_rating AS improvement_score
    FROM
        PreparedReviews
    WHERE
        -- Isolate the most recent review for each employee
        ranking = 1
        -- Check for strictly increasing ratings. This also implicitly handles cases with < 3 reviews,
        -- as the lagged values would be NULL and the comparison would fail.
        AND latest_rating > second_latest_rating
        AND second_latest_rating > third_latest_rating
)

-- Final SELECT: Join with the employees table to get names and apply ordering
SELECT
    i.employee_id,
    e.name,
    i.improvement_score
FROM
    ImprovingEmployees i
JOIN
    employees e ON i.employee_id = e.employee_id
ORDER BY
    i.improvement_score DESC,
    e.name ASC;