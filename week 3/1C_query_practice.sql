use northwind;

SELECT ProductID, ProductName, UnitPrice
FROM Products
ORDER BY UnitPrice ASC;

SELECT ProductID, ProductName, UnitPrice, UnitsInStock
FROM Products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC;
-- The products with at least 100 units on hand, ordered by price from highest to lowest, are Sirop d'rable ($28.50), Grandma's Boysenberry Spread ($25.00), Pt chinois ($24.00), Gustaf's Knckebrd ($21.00), Inlagd Sill ($19.00), Boston Crab Meat ($18.40), Rd Kaviar ($15.00), Sasquatch Ale ($14.00), Rhnbru Klosterbier ($7.75), and Geitost ($2.50).
-- The products with at least 100 units on hand, ordered by price from highest to lowest and alphabetically by product name when prices are tied, are Sirop d'rable ($28.50), Grandma's Boysenberry Spread ($25.00), Pt chinois ($24.00), Gustaf's Knckebrd ($21.00), Inlagd Sill ($19.00), Boston Crab Meat ($18.40), Rd Kaviar ($15.00), Sasquatch Ale ($14.00), Rhnbru Klosterbier ($7.75), and Geitost ($2.50).
-- There are 89 distinct customers who have placed orders, based on the CustomerID field in the Orders table.
-- USA (13), Germany (11), France (10), Brazil (9), UK (7), Austria (6), Spain (5), Sweden (5), Canada (4), Italy (4), Belgium (3), Denmark (3), Finland (3), Mexico (3), Portugal (3), Argentina (2), Ireland (2), Switzerland (2), Venezuela (2), Australia (1), and Norway (1).
-- The products are Louisiana Hot Spiced Okra (100), Wimmers gute Semmelknödel (80), Aniseed Syrup, Chocolade, Gorgonzola Telino, and Rogede sild (70 each), Maxilaku (60), Gravad lax (50), Chang, Mascarpone Fabioli, and Sir Rodney's Scones (40 each), Queso Cabrales (30), Longlife Tofu (20), and Gnocchi di nonna Alice, Ipoh Coffee, Outback Lager, and Scottish Longbreads (10 each). The numbers are units on order.
-- There are 4 job titles in the Employees table: Sales Representative (6 employees), Vice President, Sales (1 employee), Sales Manager (1 employee), and Inside Sales Coordinator (1 employee).
-- The employees earning between $2,000 and $2,500 per month, ordered by job title, are Laura Callahan (Inside Sales Coordinator, $2,100.50), Anne Dodsworth (Sales Representative, $2,333.33), Michael Suyama (Sales Representative, $2,004.07), and Andrew Fuller (Vice President, Sales, $2,254.49).
