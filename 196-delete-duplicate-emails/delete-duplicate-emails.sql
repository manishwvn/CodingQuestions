DELETE FROM Person
WHERE id NOT IN (
    SELECT id -- Select the IDs that should be KEPT
    FROM (
        SELECT MIN(id) AS id -- This identifies the min ID for each email group
        FROM Person
        GROUP BY email
    ) AS temp_min_ids -- Crucial: This derived table bypasses the MySQL restriction
);