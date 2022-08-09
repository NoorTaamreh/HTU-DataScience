SELECT * FROM [Employees]
WHERE FirstName LIKE '_a%' AND LastName LIKE '%n%' ;

WHERE City LIKE '[C]____%';

SELECT * FROM Customers
WHERE CustomerName LIKE 'a__ %';

SELECT FirstName + LastName AS EmployeeName
FROM [Employees]

SELECT ProductID, ProductName + ', ' + str(SupplierID) +', ' + str(Price) AS ProductInfo
FROM Products;
