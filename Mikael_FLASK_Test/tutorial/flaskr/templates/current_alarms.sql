CREATE TABLE current_alarms (
    id INTEGER PRIMARY KEY,
    alarm_type TEXT NOT NULL,
    date TEXT NOT NULL,
    priority TEXT NOT NULL,
    plant TEXT NOT NULL
);

INSERT INTO current_alarms (alarm_type, date, priority, plant)
VALUES ('Overheat', '2022-01-02', 'High', 'Plant 2'),
       ('Leak', '2022-01-03', 'Medium', 'Plant 3'),
       ('Overload', '2022-01-04', 'Low', 'Plant 4'),
       ('Underload', '2022-01-05', 'Medium', 'Plant 5'),
       ('Vibration', '2022-01-06', 'High', 'Plant 6'),
       ('Overheat', '2022-01-07', 'Low', 'Plant 7'),
       ('Leak', '2022-01-08', 'High', 'Plant 8'),
       ('Overload', '2022-01-09', 'Medium', 'Plant 9'),
       ('Underload', '2022-01-10', 'High', 'Plant 10'),
       ('Vibration', '2022-01-11', 'Low', 'Plant 1');