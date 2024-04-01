-- - Table : Customers, Orders
-- + 조건 : CustomerName별로 주문 갯수 표시
SELECT CustomerOrders.CustomerName, COUNT(CustomerOrders.OrderID) AS OrderCount
FROM ( SELECT Customers.CustomerName, Orders.OrderID
       FROM Customers 
       INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID ) AS CustomerOrders
GROUP BY CustomerOrders.CustomerName
;

-- Number of Records: 89

-- - Table : OrderDetails 
-- + 조건 : 제품명,가격, 주문 갯수, 고객명 표시
SELECT ProductName, Price, COUNT(OrderID) AS Quantity, CustomerName
FROM ( SELECT Products.ProductName, Products.Price, Orders.OrderID, Customers.CustomerName 
       FROM OrderDetails 
       INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID 
       INNER JOIN Orders ON OrderDetails.OrderID = Orders.OrderID 
       INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID ) AS DetailedOrders
GROUP BY ProductName, Price, CustomerName
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
