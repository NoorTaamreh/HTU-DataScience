SELECT * FROM Suppliers WHERE City IN (SELECT City FROM Customers);


