
# Neblio Stake Checker for Slack

This project allows you to know get notified via a Slack notification when your [Neblio](https://nebl.io) Wallet installed on a Raspberry Pi 
has earned a new stake.

<table width="60%" align="center" padding=0 margin=0>
    <tr>
        <td style="padding:0">
            <img src="https://github.com/mouserd/neblio-stake-checker-slack/blob/master/assets/neblio-stake-checker-example-nofication.png" 
                title="Neblio Stake Checker" alt="Neblio Stake Checker" width="520" />
        </td>
    </tr>
</table>


## Pre-requisites

### Slack

This project requires that you setup a Slack WebHook that the script will send details to when it detects you've earned a new stake.  To setup
a Slack WebHook, simply:

1. Create a new incoming WebHook here: [https://my.slack.com/services/new/incoming-webhook/](https://my.slack.com/services/new/incoming-webhook/)
2. Choose the slack channel that you wish the notifications to be published to
3. Click the "Add Incoming WebHooks integration" button and copy the subsequent "Webhook URL", we'll need that later

### Raspberry Pi
This project uses Python, so you will need to ensure that this is available on your Raspberry Pi.  This was 
tested on a Raspberry Pi Zero W running Raspbian Stretch which came pre-installed with Python 2.7.

In addition to Python, we will also need the Python PIP package manager so that we can install some required libraries:

```
sudo apt-get install python-pip
```

Once PIP is installed, install the following required Python libraries:

```
sudo pip install slackweb
```

We also need a utility called [jq](https://stedolan.github.io/jq/) which is command-line tool for parsing and querying json:

```
sudo apt-get install jq
```


## Installation 

### Basic Setup

Once you have satisfied all of the [pre-requisites](#pre-requisites), simply copy both the `neb-stake-checker.py` and `config.py` scripts
to your `pi` users home directory (`/home/pi`).  Edit the `config.py` python script and replace the `<<ADD YOUR SLACK WEBHOOK URL HERE>>` 
with the webhook you created for your Slack workspace.  You can also update the other properties in the `config.py` such as the channel, 
username, and emoji that the notification will be posted as.

To test that your Neblio Stake Checker is working, start the main python script by running the Python script from your Raspberry Pi 
terminal/ssh session:

```
python /home/pi/neb-stake-checker.py
```

The first time this runs, if everything is setup correctly, you should receive a slack notification to demonstrate that it has been configured correctly:

<table width="60%" align="center" padding=0 margin=0>
    <tr>
        <td style="padding:0">
            <img src="https://github.com/mouserd/neblio-stake-checker-slack/blob/master/assets/neblio-stake-checker-setup-success.png" 
                title="Neblio Stake Checker" alt="Neblio Stake Checker" width="520" />
        </td>
    </tr>
</table>

### Automatic Scheduling

Once the Basic Setup is complete you can setup your Raspberry Pi to run automatically on a regular interval.  To do this we use a tool 
pre-installed on all Raspberry Pi's called cron and I have mine setup to check for new neblio stakes every 10 minutes.  
To setup cron run the following command in your Raspberry Pi terminal/ssh session:

```crontab -e```

In the resulting file, add the following to the bottom:
```
*/10 * * * * /usr/bin/python /home/pi/neb-stake-checker.py >> /var/log/neb-stake-checker.log 2>&1
```

Save and exit your cron.

Now all you need to do is sit back and wait to be notified of your next stake! :rocket:

## Donate / Tip :dollar:

:thumbsup: I hope you've found the **Neblio Stake Checker** useful!  If you'd like to donate or tip me to assist with the cost of building and maintaining 
this project then it would be much appreciated.

Neblio Address: ﻿`NbmG8tDpXVvjjac4UAmtsuitFAHf9YHcD3`

Ethereum Address: `0x6E644b360f314a50A8684a9E6676E13CbB702d1d` 

