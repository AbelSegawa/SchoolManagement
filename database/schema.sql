CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
);

CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    grade TEXT
);

CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    subject TEXT
);

CREATE TABLE IF NOT EXISTS fees (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    amount REAL,
    status TEXT
);

CREATE TABLE IF NOT EXISTS exams (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject TEXT,
    marks REAL
);
