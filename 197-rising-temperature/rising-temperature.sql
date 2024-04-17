SELECT w1.Id AS Id
FROM Weather w1
JOIN Weather w2 ON w1.RecordDate = w2.RecordDate + 1
WHERE w1.Temperature > w2.Temperature;
