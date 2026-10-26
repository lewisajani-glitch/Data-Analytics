Use northwind;

Select ProductID, ProductName, UnitPrice
From products
Where UnitPrice <= 7.50;

Select ProductID, ProductName, UnitsInStock, UnitsOnOrder
From products
Where UnitsInStock = 0
	And UnitsOnOrder >= 1;
-- There are no products currently listed to have zero units in stock and one or more units on backorder. 
    
Select SupplierID, CompanyName
From suppliers 
Where CompanyName = 'Tokyo Traders';

Select ProductID, ProductName, SupplierID
From products
Where SupplierID = 4


-- 9 employees work at northwind. 
-- Steven Buchanan has the manager included in his job time. 


