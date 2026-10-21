/*
a)The info included in the actor section is Columns, indexes, foreign Keys, triggers.
b)The info that's included are things like film_id, tiles, description, release_year, etc.
c) film_actor has both actor_id and film_id. 
d)it includes rental_id, customer and staff id, inventory id, and lastly when it was rented, returned and then updated. The table is easy to read but i think that rearranging the order would make it more easier to read. 
e)this include inventory id, store id, film id and updated dates. 
f)I would say that rental, inventory and film is where you would find all that information. These tables are related with the ids allowing you to find the names of all flims and what specific day it's rented. 
*/

USE sakila;
SELECT rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film; 
