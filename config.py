from environs import Env

env = Env()
env.read_env()

url = env("URL")
token = env("TOKEN")