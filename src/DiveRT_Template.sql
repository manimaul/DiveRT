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


-- Table: settings
CREATE TABLE settings ( 
    setting CHAR,
    value   CHAR 
);



