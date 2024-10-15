CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

INSERT INTO users (username, password) VALUES
    ('brett', 'password1'),
    ('sly', 'password2'),
    ('cassie', 'password3');