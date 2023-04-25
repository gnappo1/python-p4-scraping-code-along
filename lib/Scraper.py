from bs4 import BeautifulSoup
import requests
from Course import Course
import ipdb


class Scraper:
    def get_page(self):
        headers = {'user-agent': 'my-app/0.0.1'}
        html = requests.get("http://flatironschool.com/", headers=headers)
        return BeautifulSoup(html.text, 'html.parser')
    
    def get_courses(self):
        doc = self.get_page()
        return doc.select(".row.bg-white.no-gutters.rounded-20.pad-10.panel-sticky")
    
    def make_courses(self):
        courses = self.get_courses()
        course_instances = []
        for course in courses:
            description = course.select("p")[0].text.strip()
            title = course.select("h3")[0].text.strip()
            schedule = "N/A"
            course_instances.append(Course(title=title, schedule=schedule, description=description))
        return course_instances
    
    def print_courses(self):
        for course in self.make_courses():
            print(course)

scraper = Scraper()
scraper.print_courses()