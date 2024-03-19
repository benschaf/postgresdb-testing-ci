from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

db = create_engine("postgresql:///chinook")

meta = MetaData(db)

artist_table = Table(
    "artist", meta,
    Column("artist_id", Integer, primary_key = True),
    Column("name", String)
)

album_table = Table(
    "album", meta,
    Column("album_id", Integer, primary_key = True),
    Column("title", String),
    Column("artist_id", Integer, ForeignKey("artist_table.artist_id"))
)

track_table = Table(
    "track", meta,
    Column("track_id", Integer, primary_key = True),
    Column("name", String),
    Column("album_id", Integer, ForeignKey("album_table.album_id")),
    Column("media_type_id", Integer, primary_key = False),
    Column("genre_id", Integer, primary_key = False),
    Column("composer", String),
    Column("milliseconds", Integer),
    Column("unit_price", Float),
)

with db.connect() as connection:
    select_query = track_table.select().where(track_table.c.composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)