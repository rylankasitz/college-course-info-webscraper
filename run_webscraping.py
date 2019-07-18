import webscrapers.ksu.course_scraper as ksu_course_scraper
import build_database as db_build

db_build.build()
ksu_course_scraper.run()