SELECT 
    NAME AS 'name',
    POPULATION AS 'population',
    AREA AS 'area'
FROM 
    WORLD
WHERE 
    AREA >= 3000000 OR 
    POPULATION >= 25000000;
