DROP TABLE IF EXISTS posts;
CREATE TABLE posts (
    pid INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
