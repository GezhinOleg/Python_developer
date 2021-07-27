INSERT INTO Musician (name)
VALUES ('Pink Floyd'),
       ('Queen'),
	   ('Nirvana'),
	   ('Eric Clapton'),
	   ('AC/DC'),
	   ('Miles Davis'),
	   ('Norah Jones'),
	   ('ABBA'),
	   ('Boston'),
	   ('Enya');

INSERT INTO Genre (name)
VALUES ('Classical'),
       ('Jazz'),
	   ('Rap'),
	   ('Electronic'),
	   ('Rock'),
	   ('Disco'),
	   ('Fusion'),
	   ('Pop Music'),
	   ('Country'),
	   ('Reggae'),
	   ('Indie'),
	   ('Blues');
	   
INSERT INTO Albums (name, year)
VALUES ('Miami 1994', '1994'),
       ('Pulse', '1998'),
	   ('Greatest Hits II', '2020'),
	   ('Nevermind', '2019'),
	   ('Old Blue', '2018'),
	   ('74 Jailbreak', '2009'),
	   ('Miles Ahead', '2008'),
	   ('Til We Meet Again', '2018'),
	   ('GOLD', '1992'),
	   ('Storms In Africa', '1989');
	   
	   
INSERT INTO Collection (name, year)
VALUES ('Classical collection 1', '2018'),
       ('Classical collection 2', '2019'),
	   ('Classical rap', '2017'),
	   ('Rap collection', '2018'),
	   ('Rock collection', '2020'),
	   ('Disco dance', '2018'),
	   ('Fusion music', '2016'),
	   ('Pop art', '1998'),
	   ('Country home', '2014'),
	   ('Reggae and blues', '2000'),
	   ('Indie collection', '2015'),
	   ('Blues home', '2018');
	   
INSERT INTO Track (name, duration, albums_id)
VALUES ('Astronomy domine Barrett', '238', '1'),
       ('Learning to fly Gilmour ', '317', '1'),
	   ('What do you want from my Gilmour', '259', '1'),
	   ('Shine On You Crazy Diamond', '795', '2'),
	   ('What Do You Want From my', '250', '2'),
	   ('Learning To Fly', '316', '2'),
	   ('Keep Talking', '376', '2'),
	   ('One Vision', '267', '3'),
	   ('Tie Your Mother Down', '236', '3'),
	   ('Sappy', '209', '4'),
	   ('Stay away', '215', '4'),
	   ('Badge', '417', '5'),
	   ('Wonderful Tonight', '541', '5'),
	   ('Jailbreak', '285', '6'),
	   ('You Aint Got a Hold On my', '216', '6'),
	   ('Vierd Blues', '412', '7'),
	   ('Diane', '467', '7'),
	   ('Cold, Cold Heart', '325', '8'),
	   ('It Was You', '338', '8'),
	   ('Dancing Queen', '358', '9'),
	   ('Knowing Me, Knowing You', '123', '9'),
	   ('Blood For Blood', '159', '10'),
	   ('Tommy and The Terrors', '231', '10');
	  

INSERT INTO MusicianAlbums (musician_id, albums_id)
VALUES ('1', '1'),
       ('2', '2'),
	   ('3', '3'),
	   ('4', '4'),
	   ('5', '5'),
	   ('6', '6'),
	   ('7', '7'),
	   ('8', '8'),
	   ('9', '9'),
	   ('10', '10');
	   
INSERT INTO MusicianGenre (musician_id, genre_id)
VALUES ('1', '3'),
       ('2', '1'),
	   ('3', '3'),
	   ('4', '6'),
	   ('5', '5'),
	   ('6', '3'),
	   ('7', '4'),
	   ('8', '8'),
	   ('9', '10'),
	   ('10', '9'),
                       ('2', '3'),
                       ('2', '6'),
	   ('3', '4'),
	   ('4', '5');	

INSERT INTO CollectionTrack (collection_id, track_id)
VALUES ('1', '2'),
       ('1', '5'),
	   ('1', '3'),
	   ('2', '2'),
	   ('2', '10'),
	   ('2', '11'),
	   ('2', '6'),
	   ('3', '5'),
	   ('3', '7'),
	   ('4', '8'),
	   ('4', '7'),
	   ('5', '9'),
	   ('5', '10'),
	   ('6', '2'),
	   ('6', '3'),
	   ('7', '2'),
	   ('7', '1'),
	   ('8', '11'),
	   ('8', '5'),
	   ('9', '6'),
	   ('9', '7'),
	   ('10', '10'),
	   ('10', '11'),
	   ('11', '4'),
	   ('11', '2');