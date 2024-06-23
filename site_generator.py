import os, shutil
from jinja2 import Template, Environment, FileSystemLoader
import home_assistant
import datetime
from zoneinfo import ZoneInfo

class SiteGenerator(object):
    def __init__(self):
        self.env = Environment(loader=FileSystemLoader("template"))
        self.empty_public()
        self.copy_static()
        self.render_mainpage()

    def empty_public(self):
        """Ensure the public directory is empty before generating."""
        try:
            shutil.rmtree("./public")
            os.mkdir("./public")
        except:
            print("Error cleaning up old files.")

    def copy_static(self):
        """Copy static assets to the public directory"""
        try:
            shutil.copytree("template/static", "public/static")
        except:
            print("Error copying static files.")

    def render_mainpage(self):
        """Render the main webpage."""
        print("Rendering page to static file.")
        template = self.env.get_template("_layout.html")
        space_state = home_assistant.get_entity_state("binary_sensor.space")
        if (space_state):
            plan_source = "public/static/hs3-widok-z-gory.png"
        else:
            plan_source = "public/static/hs3-widok-z-gory-off.png"
        with open("index.html", "w+", encoding='utf-8') as file:
            html = template.render(
                plan = plan_source,
                entities=home_assistant.get_entity_state_list(),
                report_date=datetime.datetime.now(ZoneInfo('Europe/Warsaw')).strftime('%Y-%m-%d %H:%M:%S')
            )
            file.write(html)