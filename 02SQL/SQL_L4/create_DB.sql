create table if not exists Musician (
         id serial primary key,
         name varchar (40) not null
         );
create table if not exists Genre (
        id serial primary key,
        name varchar (40) not null unique
        );
create table if not exists Albums (
        id serial primary key,
        name varchar (40) not null,
        year integer
        );
create table if not exists MusicianGenre (
         constraint MusicianGenre_pkey primary key (musician_id, genre_id),
         musician_id integer references Musician (id),
         genre_id integer references Genre (id)
         );
create table if not exists MusicianAlbums (
         musician_id integer references Musician (id),
         albums_id integer references Albums (id),
         constraint MusicianAlbums_pkey primary key (musician_id, albums_id)
         );
create table if not exists Track (
        id serial primary key,
        name varchar (40) not null,
        duration integer,
        albums_id integer references Albums (id)
        );
create table if not exists Collection (
        id serial primary key,
        name varchar (40) not null,
        year integer
        );
create table if not exists CollectionTrack (
        collection_id integer references Collection (id),
        track_id integer references Track (id),
        constraint CollectionTrack_pkey primary key (collection_id, track_id)
        );