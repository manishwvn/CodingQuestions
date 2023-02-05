SELECT c.`Name` as Customers FROM `Customers` c
    LEFT JOIN `Orders` o ON(o.`CustomerId` = c.`Id`)
        WHERE o.`Id` IS NULL