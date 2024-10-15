CREATE TABLE directories (
    dir_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    parent_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_id) REFERENCES directories(dir_id);

INSERT INTO directories (name, parent_id, created_at, modified_at) VALUES
    ('linux', NULL, '2018-06-23 19:15:35', '2018-08-18 09:05:02'),
    ('drivers', 1, '2017-06-27 01:02:44', '2017-10-05 06:02:11'),
    ('perfctr', 2, '2021-10-19 15:58:04', '2021-11-13 10:21:53'),
    ('win2k', NULL, '2016-08-30 04:50:39', '2017-04-19 10:10:58'),
    ('shell', 4, '2020-08-13 21:18:45', '2021-07-04 22:32:53'),
    ('substrate', 4, '2020-11-18 16:16:19', '2021-03-16 15:28:57'),
    ('winpmc', NULL, '2015-10-11 05:21:17', '2017-01-30 15:14:55'),
    ('tools', 4, '2020-06-05 21:51:50', '2021-02-04 08:24:36'),
    ('papiex', 8, '2017-08-28 01:25:12', '2018-08-16 21:59:00'),
    ('src', 9, '2019-04-26 20:57:26', '2020-06-23 04:33:27'),
    ('tests', 8, '2022-11-16 14:46:10', '2023-10-07 20:57:47'),
    ('trapper', 8, '2015-02-14 20:25:29', '2016-02-06 19:51:11');