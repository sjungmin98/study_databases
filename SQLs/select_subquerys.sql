SELECT *
FROM Customers
WHERE CustomerID IN (
    SELECT CustomerID
    FROM Orders
    GROUP BY CustomerID
    HAVING COUNT(OrderID) >= 5
)
;
-- Number of Records: 72

SELECT *
FROM (
    SELECT EmployeeID, COUNT(OrderID) AS OrderCount
    FROM Orders
    GROUP BY EmployeeID
    HAVING COUNT(OrderID) >= 20
) AS SubQuery
;
-- Number of Records: 9

SELECT *
FROM Suppliers
WHERE SupplierID IN (
    SELECT SupplierID
    FROM (
        SELECT SupplierID
        FROM Products
        GROUP BY SupplierID
        ORDER BY COUNT(DISTINCT CategoryID) DESC
        LIMIT 2
    ) AS SubQuery
)
;
-- Number of Records: 2