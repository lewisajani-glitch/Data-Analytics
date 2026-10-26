-- a) The products table holds the items Northwind sells.
-- b) The Categories table holds the types or categories of items Northwind sells.
Select * From employees;
-- Margaret is the Northwind employee whose name makes her look like a bird since her last name is peacock. 

Select * From products;
-- a) The quary returns 77 records. In the toolbar, change the row limit to 10 to retrieve only 10 rows.

Select * from categories;
-- c) The category ID of Seafood is 8. 

Select OrderID, OrderDate, ShipName, ShipCountry
From orders 
limit 50; 