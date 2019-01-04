-- go into terminal
-- sqlite3 zoo.db

CREATE TABLE cats (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  age INTEGER,
  color TEXT
);

INSERT INTO cats (name, age, color) VALUES
  ('fluffy', 2, 'brown'),
  ('garfield', 2, 'orange'),
  ('marshmallow', 2, 'brown');

-- name = 'fluffy'
SELECT name, age FROM cats WHERE id = name;
