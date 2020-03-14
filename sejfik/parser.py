import configparser
import os

config_dir = os.path.dirname(os.path.abspath(__file__)) + '/config'

if not os.listdir(config_dir):
    print("Didn't found any config files. Creating one...")
    os.chdir(config_dir)

    with open(input('Enter username: ') + '.cfg'):
        pass
