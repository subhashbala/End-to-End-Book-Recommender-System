# we have to go over constants now
# this is how we get the path for the config.yaml file
import os

ROOT_DIR = os.getcwd()
# main config file path
CONFIG_FOLDER_NAME = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_FOLDER_NAME, CONFIG_FILE_NAME)

# we always try to create a template,, we don't try to hard code much