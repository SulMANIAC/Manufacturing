-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS Alarm;

-- Use the created database
USE Alarm;

-- Drop existing tables if they exist
DROP TABLE IF EXISTS AcknowledgeHistory;
DROP TABLE IF EXISTS AlarmReports;
DROP TABLE IF EXISTS OperatorActions;
DROP TABLE IF EXISTS AlarmHistory;

-- Create the AlarmHistory table
CREATE TABLE AlarmHistory (
    ID INTEGER PRIMARY KEY AUTO_INCREMENT,
    AlarmName TEXT NOT NULL,
    AlarmTime DATETIME NOT NULL,
    AlarmLocation TEXT NOT NULL
);

-- Create the OperatorActions table
CREATE TABLE OperatorActions (
    ID INTEGER PRIMARY KEY AUTO_INCREMENT,
    OperatorName TEXT NOT NULL,
    ActionTime DATETIME NOT NULL,
    ActionDetails TEXT NOT NULL
);

-- Create the AcknowledgeHistory table
CREATE TABLE AcknowledgeHistory (
    ID INTEGER PRIMARY KEY AUTO_INCREMENT,
    OperatorName TEXT NOT NULL,
    AcknowledgeTime DATETIME NOT NULL,
    AlarmID INTEGER,
    FOREIGN KEY (AlarmID) REFERENCES AlarmHistory(ID)
);

-- Create the AlarmReports table
CREATE TABLE AlarmReports (
    ID INTEGER PRIMARY KEY AUTO_INCREMENT,
    ReportTime DATETIME NOT NULL,
    ReportDetails TEXT NOT NULL,
    AlarmID INTEGER,
    FOREIGN KEY (AlarmID) REFERENCES AlarmHistory(ID)
);

-- Insert sample data into the AlarmHistory table
INSERT INTO AlarmHistory (AlarmName, AlarmTime, AlarmLocation) VALUES
('Overheat', '2022-01-01 10:00:00', 'Factory 1'),
('Power Loss', '2022-01-02 15:30:00', 'Factory 2'),
('Network Disconnection', '2022-01-03 20:45:00', 'Factory 1');

-- Insert sample data into the OperatorActions table
INSERT INTO OperatorActions (OperatorName, ActionTime, ActionDetails) VALUES
('Operator 1', '2022-01-01 10:05:00', 'Acknowledged Overheat Alarm'),
('Operator 2', '2022-01-02 15:35:00', 'Acknowledged Power Loss Alarm'),
('Operator 1', '2022-01-03 20:50:00', 'Acknowledged Network Disconnection Alarm');

-- Insert sample data into the AcknowledgeHistory table
INSERT INTO AcknowledgeHistory (OperatorName, AcknowledgeTime, AlarmID) VALUES
('Operator 1', '2022-01-01 10:05:00', 1),
('Operator 2', '2022-01-02 15:35:00', 2),
('Operator 1', '2022-01-03 20:50:00', 3);

-- Insert sample data into the AlarmReports table
INSERT INTO AlarmReports (ReportTime, ReportDetails, AlarmID) VALUES
('2022-01-01 11:00:00', 'Overheat Alarm was acknowledged by Operator 1', 1),
('2022-01-02 16:00:00', 'Power Loss Alarm was acknowledged by Operator 2', 2),
('2022-01-03 21:00:00', 'Network Disconnection Alarm was acknowledged by Operator 1', 3);
