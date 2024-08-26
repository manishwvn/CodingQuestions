SELECT DISTINCT v1.author_id AS id
FROM views v1
JOIN views v2
ON v1.author_id = v2.viewer_id
WHERE v1.author_id = v2.author_id
ORDER BY 1;