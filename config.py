from environs import Env

env = Env()
env.read_env()

url = env("URL")
token = env("TOKEN")

# List of entities to put on the plan with coordinates
entities = [
            ["bottom:270px;left:330px",
             "sensor.termostat_warsztatowy_cnc_air_temperature_2"],
            ["bottom:270px;left:600px",
             "sensor.termostat_cowork_air_temperature"],
            ["bottom:290px;left:1110px", 
             "sensor.people_in_hackerspace"]
        ]