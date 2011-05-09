-- Table: dives
CREATE TABLE dives ( 
    recordID      INTEGER PRIMARY KEY AUTOINCREMENT
                          UNIQUE,
    cleanupNumber INTEGER,
    diveDate      DATE,
    diverName     CHAR,
    start         CHAR,
    stop          CHAR,
    latitude      CHAR,
    longitude     CHAR,
    bearing       CHAR,
    notes         CHAR,
    tenderName    CHAR 
);


-- Table: crew
CREATE TABLE crew ( 
    idnum    INTEGER PRIMARY KEY
                     UNIQUE,
    name     CHAR,
    duty     CHAR,
    diverate CHAR,
    tendrate CHAR 
);

INSERT INTO [crew] ([idnum], [name], [duty], [diverate], [tendrate]) VALUES (1, 'Demo Diver', 'Diver and Tender', 45, 20);
INSERT INTO [crew] ([idnum], [name], [duty], [diverate], [tendrate]) VALUES (2, 'Demo Tender', 'Tender', 45, 20);


-- Table: settings
CREATE TABLE settings ( 
    setting CHAR,
    value   CHAR 
);


-- Table: cleanups
CREATE TABLE cleanups ( 
    number     INT,
    grams      CHAR,
    londonspot CHAR,
    loss       CHAR 
);


-- Table: cleanupsub
CREATE TABLE cleanupsub ( 
    number  INT,
    name    CHAR,
    percent CHAR 
);



