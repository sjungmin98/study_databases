-- - Table : Customers, Orders
-- + 조건 : CustomerName별로 주문 갯수 표시
SELECT CustomerOrders.CustomerName, COUNT(CustomerOrders.OrderID) AS OrderCount
FROM ( SELECT Customers.CustomerName, Orders.OrderID
       FROM Customers 
       INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID ) AS CustomerOrders
GROUP BY CustomerOrders.CustomerName
;

-- - Table : OrderDetails 
-- + 조건 : 제품명,가격, 주문 갯수, 고객명 표시
SELECT Products.ProductName, Products.Price, COUNT(OrderDetails.OrderID) AS Quantity, Customers.CustomerName
FROM OrderDetails
    INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID
    INNER JOIN Orders ON OrderDetails.OrderID = Orders.OrderID
    INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID
GROUP BY Products.ProductName, Products.Price, Customers.CustomerName
;

-- - Table : Orders
-- + 조건 : 가장 많이 주문 받은 회사 직원명과 갯수
SELECT EmployeeOrders.FirstName, EmployeeOrders.LastName, EmployeeOrders.OrderCount
FROM ( SELECT Employees.FirstName, Employees.LastName, COUNT(Orders.OrderID) AS OrderCount
       FROM Orders 
       INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
       GROUP BY Employees.EmployeeID
       ORDER BY OrderCount DESC
       LIMIT 0, 1 ) AS EmployeeOrders
;
