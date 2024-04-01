SELECT *
FROM Customers
WHERE CustomerID IN (
    SELECT CustomerID
    FROM Orders
    GROUP BY CustomerID
    HAVING COUNT(OrderID) >= 5
)
;

SELECT *
FROM (
    SELECT CustomerID, COUNT(OrderID) AS OrderCount
    FROM Orders
    GROUP BY CustomerID
    HAVING COUNT(OrderID) >= 20
)
;

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
    ) AS Subquery
);