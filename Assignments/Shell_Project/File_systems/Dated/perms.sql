querys = [
"""
CREATE TABLE permissions (
    perm_id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER,
    dir_id INTEGER,
    user_id INTEGER,
    read_permission BOOLEAN DEFAULT 0,
    write_permission BOOLEAN DEFAULT 0,
    execute_permission BOOLEAN DEFAULT 0,
    FOREIGN KEY (file_id) REFERENCES files(file_id),
    FOREIGN KEY (dir_id) REFERENCES directories(dir_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id);
""",
"""
INSERT INTO permissions (file_id, dir_id, user_id, read_permission, write_permission, execute_permission) VALUES
    (NULL, 1, 1, 1, 1, 1),  -- Full access to 'linux' directory
    (NULL, 2, 1, 1, 1, 1),  -- Full access to 'drivers' directory
    (4, NULL, 1, 1, 1, 0),  -- Read/write access to 'global.c'
    (5, NULL, 1, 1, 1, 0);  -- Read/write access to 'init.c'
""",
"""
INSERT INTO permissions (file_id, dir_id, user_id, read_permission, write_permission, execute_permission) VALUES
    (NULL, 4, 2, 1, 1, 1),  -- Full access to 'win2k' directory
    (NULL, 5, 2, 1, 1, 1),  -- Full access to 'shell' directory
    (12, NULL, 2, 1, 1, 0);  -- Read/write access to 'PAPI_Errors.c'
"""
"""
INSERT INTO permissions (file_id, dir_id, user_id, read_permission, write_permission, execute_permission) VALUES
    (NULL, 7, 3, 1, 1, 1),  -- Full access to 'winpmc' directory
    (44, NULL, 3, 1, 1, 0); -- Read/write access to 'pmclib.c'
""",]

if __name__ == "__main__":
    import sqlite3

    # Connect to the SQLite database
    conn = sqlite3.connect("filesystem.db")

    # Create a cursor object
    cursor = conn.cursor()

    for query in querys:
        cursor.execute(query)

    conn.commit()
    conn.close()