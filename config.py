import logging

SLACK_WEB_HOOK_URL = '<<ADD YOUR SLACK WEBHOOK URL HERE>>'
SLACK_CHANNEL = "#general"
SLACK_USERNAME = "Admin"
SLACK_ICON_EMOJI = ":neblio:"

NEB_PREVIOUS_STAKE_FILE = "/home/pi/neb-stake-previous.json"
NEB_CURRENT_STAKE_FILE = "/home/pi/neb-stake-current.json"

LOG_PATH = '/home/pi'  # default path where logs are written, path needs to be writable by the 'pi' user
LOG_LEVEL = logging.INFO
