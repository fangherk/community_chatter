-- Schema Namespace
CREATE SCHEMA IF NOT EXISTS comchatter;

-- Registration Tables
CREATE TABLE comchatter.registration
(
    telegram_id   INTEGER  UNIQUE,
    first_name    TEXT,
    last_name     TEXT,
    email         TEXT,
    mobile        TEXT,
    grade         INTEGER,
    teacher       TEXT
)


