"""Common configuration module"""
from environs import Env

env = Env()
env.read_env()

url = env("URL")
token = env("TOKEN")

# List of entities to put on the plan with coordinates
entities = [
    ["bottom:270px;left:330px", "climate.termostat_cowork_2_lan_zone_thermostat"],
    ["bottom:270px;left:600px", "climate.termostat_cowork_thermostat"],
    ["bottom:290px;left:1110px", "sensor.people_in_hackerspace"],
]
