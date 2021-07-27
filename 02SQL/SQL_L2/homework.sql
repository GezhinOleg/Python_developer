create table if not exists Musician (
         id serial primary key,
         name varchar (40) not null unique
         musician_id integer references Genre (id)
         );
create table if not exists Albums (
        id serial primary key,
        name varchar (40) not null,
        year integer,
        musician_id integer references Musician (id)
        );
create table if not exists Track (
        id serial primary key,
        name varchar (40) not null,
        duration integer (5),
        albums_id integer references Albums (id)
        );
create table if not exists Genre (
        id serial primary key,
        name varchar (40) not null unique,
        );