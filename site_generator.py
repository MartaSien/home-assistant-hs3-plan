import os, shutil
from jinja2 import Template, Environment, FileSystemLoader
import home_assistant
import datetime

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
        with open("index.html", "w+", encoding='utf-8') as file:
            html = template.render(
                title="HS3 Home Assistant",
                termostat_warsztat=home_assistant.get_entity_state("sensor.termostat_warsztatowy_cnc_air_temperature_2")["state"],
                termostat_cowork=home_assistant.get_entity_state("sensor.termostat_cowork_air_temperature")["state"],
                people_hackerspace=home_assistant.get_entity_state("sensor.people_in_hackerspace")["state"],
                report_date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            )
            file.write(html)


if __name__ == "__main__":
    SiteGenerator()