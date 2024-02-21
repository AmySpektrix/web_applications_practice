_Copy this recipe template to design and create a database table from a specification._

## 1. Extract nouns from the user stories or specification

```
As a music lover,
So I can organize my records,
I want to keep a list of albums' titles.

As a music lover,
So I can organize my records,
I want to keep a list of albums' release years.

As a music lover,
So I can find out what artist created the album
I want to be able to reference the artist ID

As a music lover
So I can find out what my favorite artists are
I want to be able to keep a list of artist names

As a music lover
So I can categorize my music 
I want to be able to keep a list of artist genres
```

```
Nouns:

album, title, release year,artist, artist_name, genre, id
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties                     |
| --------------------- | ------------------------------ |
| album                 | title, release year, artist_id |
| artist                | artist_name, genre             |


Name of table 1: `albums`

Column names: `id`(PK), `title`, `release_year`, `artist_id`(FK)

Name of table 2: `artists`

Column names: `id` (PK), `artist_name`, `genre`

## 3. Decide the column types

```
Albums: 
    id: SERIAL
    title: VARCHAR (255)
    release_year: int
    artist_id: int

Artists:
    id: SERIAL
    artist_name: VARCHAR (255)
    genre: VARCHAR (255)


```

## 4. Write the SQL

```sql
-- file: music_library_tables.sql

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    artist_name VARCHAR(255),
    genre VARCHAR(255)
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR (255),
    release_year int,
    artist_id int,
    constraint fk_artist foreign key(artist_id)
        references artists(id)
        on delete cascade
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 database_name < albums_table.sql
```