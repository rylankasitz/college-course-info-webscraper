import lib.db.builder as db_builder

DATABASE_NAME = 'ksucourses.db'
TYPE_TABLE = 'tables'
COURSES_TABLE = 'Courses'

def build():
    db_builder.run_sqlfile(DATABASE_NAME, COURSES_TABLE + '.sql', TYPE_TABLE)
    db_builder.print_table(DATABASE_NAME, COURSES_TABLE)

def add_course(pre_req_id, prof_id, number, department, department_abbr, name, description, semester, year, 
               start_time, end_time, online, location, url):
    contents = [(pre_req_id, prof_id, number, department, department_abbr, name, description, semester, 
                 year, start_time, end_time, online, location, url)]
    db_builder.insert_into_table(DATABASE_NAME, COURSES_TABLE, contents)