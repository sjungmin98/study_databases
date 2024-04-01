-- - Table : Customers, Orders
SELECT Customers.CustomerName, COUNT(Orders.OrderID) AS OrderCount
FROM Customers 
       INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID
GROUP BY Customers.CustomerName;


-- + 조건 : CustomerName별로 주문 갯수 표시

-- 이 쿼리는 고객별 주문 횟수를 계산하기 위해 Customers와 Orders 테이블을 INNER JOIN함

-- Customers 테이블의 CustomerID, Orders 테이블의 CustomerID를 비교하여, 
-- 두 테이블 간에 일치하는 CustomerID 값을 갖는 행만 선택함

-- INNER JOIN하여 Customers 테이블과 Orders 테이블을 결합했기 때문에 Customers.CustomerID와 Orders.CustomerID가 동일한 값을 가짐

-- Orders 테이블의 CustomerID가 Customers 테이블의 CustomerID와 동일한 값을 가져야 하는 것은 각 주문이 어떤 고객에게 속하는지를 정확하게 추적하기 위한 필수적인 조건

-- 주문을 개별적으로 추적하기 위해 CustomerName값으로 그룹화하여, 같은 고객에 대한 주문들을 한 그룹으로 합침

-- COUNT(Orders.OrderID)를 통해 각 고객이 몇 번의 주문을 했는지를 계산함 


-- - Table : OrderDetails 
SELECT Products.ProductName, Products.Price, SUM(OrderDetails.Quantity) AS TotalQuantity, Customers.CustomerName
FROM Products
       INNER JOIN OrderDetails ON Products.ProductID = OrderDetails.ProductID
       INNER JOIN Orders ON OrderDetails.OrderID = Orders.OrderID
       INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID
GROUP BY Products.ProductName, Products.Price, Customers.CustomerName
ORDER BY Products.ProductName, Customers.CustomerName
;

-- + 조건 : 제품명, 가격, 주문 갯수, 고객명 표시

-- 이 쿼리는 Products, OrderDetails, Orders, Customers 테이블을 INNER JOIN함.

-- Products 테이블은 제품 정보를, OrderDetails 테이블은 상세 주문 정보를, 
-- Orders 테이블은 주문에 대한 일반적인 정보를, Customers 테이블은 고객 정보를 담고 있음

-- 각 제품의 주문 정보를 가져오기 위해 Products 테이블과 OrderDetails 테이블을 조인. 

-- 그 후, 주문 정보와 주문한 고객 정보를 가져오기 위해 Orders 테이블과 Customers 테이블도 조인

-- 그 결과로 ProductName, Price, TotalQuantity, CustomerName을 표시

-- 보기 편하게 ORDER BY로 ProductName과 CustomerName을 오름차순으로 정렬

-- 하나의 고객이 여러 주문을 할 수 있기 때문에 중복 고객이름값을 피하기 위해,
-- OrderDetails.Quantity에 SUM 함수를 사용해서 각 제품에 대한 총 주문 수량을 계산

-- - Table : Orders
SELECT Employees.FirstName, Employees.LastName, COUNT(Orders.OrderID) AS OrderCount
FROM Orders 
       INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
       GROUP BY Employees.EmployeeID
       ORDER BY OrderCount DESC
LIMIT 0, 1
;

-- + 조건 : 가장 많이 주문 받은 회사 직원명과 갯수

-- 이 쿼리는 먼저 주문 데이터와 직원 데이터를 함께 가져와야 하기 떄문에,
-- Orders 테이블과 Employees 테이블을 조인하여 각 주문에 대한 직원의 정보를 가져옴

-- 가져온 데이터를 직원별로 그룹화 (GROUP BY Employees.EmployeeID) 하고,
-- 각 직원이 받은 주문의 수를 계산하기 위해 COUNT(Orders.OrderID)를 사용하여 직원별 주문 갯수를 계산함

-- 이 후, 주문 수에 따라 내림차순으로 정렬하여 주문을 가장 많이 처리한 직원이 상위에 오도록 함

-- LIMIT 0, 1을 사용해 첫 번째 결과만 선택하여 가장 많은 주문을 받은 직원에 대한 정보만 선택함 