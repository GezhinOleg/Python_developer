SELECT Genre.name, COUNT(*) FROM MusicianGenre
    INNER JOIN Genre ON Genre.ID = MusicianGenre.Genre_ID
	GROUP BY genre_ID, Genre.name;
   

SELECT Albums.name, year, COUNT(Track.name)
FROM Albums
LEFT JOIN Track
ON Albums.ID = Track.albums_ID
WHERE year >= 2018 AND year <=2020
GROUP BY Albums.name, year; 

SELECT Albums.name, AVG(Track.duration)
FROM Albums
LEFT JOIN Track
ON Albums.ID = Track.albums_ID
GROUP BY Albums.name;

SELECT Musician.name AS NOT_albums_2020, Albums.year FROM MusicianAlbums
INNER JOIN Musician ON Musician.ID = MusicianAlbums.musician_ID
INNER JOIN Albums ON Albums.ID = MusicianAlbums.albums_ID
WHERE year <> 2020
	GROUP BY Musician.name, musician_ID, Albums.year;


SELECT Musician.name AS Musician_name, Collection.name AS Collection_name FROM MusicianAlbums
INNER JOIN Musician ON Musician.ID = MusicianAlbums.musician_ID
INNER JOIN Albums ON Albums.ID = MusicianAlbums.albums_ID
INNER JOIN Track ON Albums.ID = Track.albums_ID
INNER JOIN CollectionTrack ON Track.ID = CollectionTrack.Track_ID
INNER JOIN Collection ON CollectionTrack.Track_ID = Collection.ID
    WHERE Musician.name = 'Queen'
	GROUP BY Musician.name, Collection.name;

SELECT Albums.name FROM Albums
INNER JOIN MusicianAlbums ON Albums.ID = MusicianAlbums.albums_ID
INNER JOIN Musician ON MusicianAlbums.musician_ID = Musician.ID
INNER JOIN (
       SELECT Musician.name, COUNT(*) FROM MusicianGenre
                  INNER JOIN Musician ON Musician.ID = MusicianGenre.musician_ID
	GROUP BY Musician.name
	HAVING COUNT(*) > 1
        ) dz ON dz.name = Musician.name
ORDER BY Albums.name;


SELECT Track.name FROM Track
LEFT JOIN CollectionTrack ON Track.Id = CollectionTrack.track_ID
WHERE CollectionTrack.track_ID IS NULL;


SELECT Musician.name AS Musician_name, Track.duration FROM Musician
INNER JOIN MusicianAlbums ON Musician.ID = MusicianAlbums.musician_ID
INNER JOIN Albums ON MusicianAlbums.albums_ID = Albums.ID
INNER JOIN Track ON Albums.ID = Track.albums_ID
WHERE Track.duration = (SELECT MIN(duration) FROM Track )


SELECT Albums.name
FROM Albums
INNER JOIN Track
ON Albums.ID = Track.albums_ID
GROUP BY Albums.name, Track.albums_ID
HAVING COUNT(Track.albums_ID) = (  
	SELECT COUNT(Track.albums_ID) FROM Albums
	JOIN Track ON Albums.ID = Track.albums_ID
	GROUP BY Albums.name
	ORDER BY COUNT(Track.albums_ID)
	LIMIT 1);  