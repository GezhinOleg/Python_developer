SELECT name, year
FROM Albums
WHERE year = 2018;

SELECT name, duration FROM Track
     ORDER BY duration DESC
	 LIMIT 1;

SELECT name
FROM Track
WHERE duration >= 210;

SELECT name, year
FROM Collection
WHERE year >= 2018 OR year >= 2020;

SELECT name
FROM Musician
WHERE name NOT LIKE '%% %%';

SELECT name
FROM Track
WHERE name LIKE '%% my%%';