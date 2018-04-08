import filecmp
import json
import logging
import os
import subprocess

import slackweb

import config

NEB_MOST_RECENT_TRANSACTION_CMD = \
    "/home/pi/nebliod listtransactions | jq 'map(select(.category==\"generate\")) | sort_by(.time) | last(.[].amount)'"

logging.basicConfig(filename='%s/slack-bot.log' % config.LOG_PATH,
                    format='%(asctime)s: [%(levelname)s] %(message)s',
                    level=config.LOG_LEVEL)


class NeblioStakeChecker:

    def __fetch_most_recent_stake(self):
        return json.loads(subprocess.check_output(NEB_MOST_RECENT_TRANSACTION_CMD, shell=True).strip())

    def __write_most_recent_stake(self, filename, stake_amount):
        f = open(filename, 'w')
        f.write("%s" % stake_amount)
        f.close()

    def check(self):
        last_stake_amount = self.__fetch_most_recent_stake()
        logging.info('Last stake amount: %s' % last_stake_amount)
        self.__write_most_recent_stake(config.NEB_CURRENT_STAKE_FILE, last_stake_amount)

        if not os.path.exists(config.NEB_PREVIOUS_STAKE_FILE):
            print('No previous neblio stake file found - first run?')
            slack = slackweb.Slack(config.SLACK_WEB_HOOK_URL)
            slack.notify(text='*Neblio Stake Checker* has been successfully configured :tada:',
                         channel=config.SLACK_CHANNEL,
                         username=config.SLACK_USERNAME,
                         icon_emoji=config.SLACK_ICON_EMOJI)
        else:
            if filecmp.cmp(config.NEB_CURRENT_STAKE_FILE, config.NEB_PREVIOUS_STAKE_FILE, False):
                print('No new stake')
            else:
                print('New stake received: %s (NEBL)' % last_stake_amount)
                slack_message = ":+1: You just received a new NEBL stake of: *%s*" % last_stake_amount

                slack = slackweb.Slack(config.SLACK_WEB_HOOK_URL)
                slack.notify(text=slack_message,
                             channel=config.SLACK_CHANNEL,
                             username=config.SLACK_USERNAME,
                             icon_emoji=config.SLACK_ICON_EMOJI)

        self.__write_most_recent_stake(config.NEB_PREVIOUS_STAKE_FILE, last_stake_amount)


neblio_stake_checker = NeblioStakeChecker()
neblio_stake_checker.check()
