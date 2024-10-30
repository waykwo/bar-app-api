import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# def initial_setup():
#     conn = connect_to_db()
#     conn.execute(
#         """
#         DROP TABLE IF EXISTS photos;
#         """
#     )
#     conn.execute(
#         """
#         CREATE TABLE photos (
#           id INTEGER PRIMARY KEY NOT NULL,
#           name TEXT,
#           width INTEGER,
#           height INTEGER
#         );
#         """
#     )
#     conn.commit()
#     print("Table created successfully")

#     photos_seed_data = [
#         ("1st photo", 800, 400),
#         ("2nd photo", 1024, 768),
#         ("3rd photo", 200, 150),
#     ]
#     conn.executemany(
#         """
#         INSERT INTO photos (name, width, height)
#         VALUES (?,?,?)
#         """,
#         photos_seed_data,
#     )
#     conn.commit()
#     print("Seed data created successfully")

#     conn.close()


def products_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS products;
        """
    )
    conn.execute(
        """
        CREATE TABLE products (
          id INTEGER PRIMARY KEY NOT NULL,
          name TEXT,
          category TEXT,
          price DECIMAL
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    products_seed_data = [
        ("Lagavulin", "Scotch", 80),
        ("Pappy", "Bourbon", 5499),
        ("Tito's", "Vodka", 20),
    ]
    conn.executemany(
        """
        INSERT INTO products (name, category, price)
        VALUES (?,?,?)
        """,
        products_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    products_setup()


def photos_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM photos
        """
    ).fetchall()
    return [dict(row) for row in rows]

def products_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM products
        """
    ).fetchall()
    return [dict(row) for row in rows]

def products_create(name, category, price):
    conn = connect_to_db()
    row = conn.execute(
        """
        INSERT INTO products (name, category, price)
        VALUES (?, ?, ?)
        RETURNING *
        """,
        (name, category, price),
    ).fetchone()
    conn.commit()
    return dict(row)