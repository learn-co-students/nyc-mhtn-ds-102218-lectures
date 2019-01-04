CREATE TABLE posts (
  Id Integer Primary Key Autoincrement,
  Title TEXT,
  Content TEXT,
  author_id INTEGER
);

CREATE TABLE authors (
  Id Integer Primary Key Autoincrement,
  Name TEXT,
  Country_id INTEGER
);

INSERT INTO posts (title, content, author_id) VALUES
  ('my special post', 'something special', 1),
  ('my post', 'something not special', 2),
  ('my other post', 'something kinda special', 2),
  ('my post again', 'something super special', 3),
  ('my postiness', 'something also special', null);



  INSERT INTO authors (name, country_id) VALUES
    ('mark twain', 1),
    ('ee cummings', 1),
    ('roahl dahl', 2),
    ('jhumpa lahiri', 3),
    ('jonathan franzen', 1);


    CREATE TABLE countries (
      Id Integer Primary Key Autoincrement,
      Name TEXT
    );

    INSERT INTO countries (name) VALUES
      ('United States'),
      ('England'),
      ('India');


      select countries.name from posts join authors on posts.author_id = authors.id join countries on authors.country_id = countries.id where title = 'my special post';
