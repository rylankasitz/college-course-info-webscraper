CREATE TABLE IF NOT EXISTS Course (
    CourseID integer PRIMARY KEY AUTOINCREMENT,
    PrerequisitesID, FOREIGN KEY,
    ProfessorID, FOREIGN KEY NOT NULL,
    Name text NOT NULL,
    Number text NOT NULL,
    Department text NOT NULL,
    DepartmentAbbreviation text NOT NULL,
    Description text,
    Semester text NOT NULL,
    Year integer NOT NULL,
    StartTime integer,
    EndTime integer,
    Online bit DEFAULT (0),
    Location text,
    URL text,

    UNIQUE(Year, Semester, Time, Department, Number),
    UNIQUE(Year, Semester, Time, DepartmentAbbreviation, Number),
    UNIQUE(Year, Semester, Time, ProfessorID)
);