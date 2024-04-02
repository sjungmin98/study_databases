-- 조건 : 비 진성고객 리스트 필요(주문 1건 이하 포함)
SELECT Customers.CustomerID, Customers.CustomerName, 
       COUNT(Orders.OrderID) AS NumberOfOrders,
    CASE 
        WHEN COUNT(Orders.OrderID) > 0 THEN '주문O'
        ELSE '주문X'
    END AS OrderStatus
FROM Customers
    LEFT JOIN Orders 
    ON Customers.CustomerID = Orders.CustomerID
GROUP BY Customers.CustomerID, Customers.CustomerName
HAVING COUNT(Orders.OrderID) <= 1
;


-- 조건 : 판매자 중 수익 낮은 순위자 3명 정보, 총 판매액
SELECT Employees.EmployeeID, Employees.LastName, Employees.FirstName, 
       SUM(Products.Price * OrderDetails.Quantity) AS TotalSales
FROM Employees
    INNER JOIN Orders 
    ON Employees.EmployeeID = Orders.EmployeeID
    INNER JOIN OrderDetails 
    ON Orders.OrderID = OrderDetails.OrderID
    INNER JOIN Products 
    ON OrderDetails.ProductID = Products.ProductID
GROUP BY Employees.EmployeeID
ORDER BY TotalSales ASC
LIMIT 0, 3
;

-- 조건 : 배송 회사별 총 배송 건수와 총 제품 금액 정보
SELECT Shippers.ShipperID, Shippers.ShipperName, COUNT(Orders.OrderID) AS TotalShipments, 
       SUM(Products.Price * OrderDetails.Quantity) AS TotalPrices
FROM Shippers
    INNER JOIN Orders 
    ON Shippers.ShipperID = Orders.ShipperID
    INNER JOIN OrderDetails 
    ON Orders.OrderID = OrderDetails.OrderID
    INNER JOIN Products 
    ON OrderDetails.ProductID = Products.ProductID
GROUP BY Shippers.ShipperID
ORDER BY TotalPrices DESC
;

-- 조건 : 제품 회사별 총 판매액과 정보
SELECT Suppliers.SupplierID, Suppliers.SupplierName, Suppliers.ContactName, 
       Suppliers.Address, Suppliers.City, Suppliers.PostalCode, Suppliers.Country,
       Suppliers.Phone AS SupplierPhone, 
       SUM(Products.Price * OrderDetails.Quantity) AS TotalPrices
FROM Suppliers
    INNER JOIN Products 
    ON Suppliers.SupplierID = Products.SupplierID
    INNER JOIN OrderDetails 
    ON Products.ProductID = OrderDetails.ProductID
    INNER JOIN Orders 
    ON OrderDetails.OrderID = Orders.OrderID
GROUP BY Suppliers.SupplierName, Suppliers.ContactName, Suppliers.Address,
         Suppliers.City, Suppliers.PostalCode, Suppliers.Country, Suppliers.Phone
ORDER BY SupplierName ASC
;

-- 조건 : 카테고리별 판매 합계 정보
SELECT Categories.CategoryID, Categories.CategoryName, 
       SUM(Products.Price * OrderDetails.Quantity) AS TotalPrices
FROM Categories
    INNER JOIN Products 
    ON Categories.CategoryID = Products.CategoryID
    INNER JOIN OrderDetails 
    ON Products.ProductID = OrderDetails.ProductID
    INNER JOIN Orders 
    ON OrderDetails.OrderID = Orders.OrderID
GROUP BY Categories.CategoryID;
