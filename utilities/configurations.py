import configparser

# Constants
endpoints = ['endpoint_usa','endpoint_ind']

def get_config():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config