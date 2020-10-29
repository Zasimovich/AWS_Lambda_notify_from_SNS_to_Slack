#from __future__ import print_function
#import boto3

import json
import logging
import os
import re
from urllib2 import Request, urlopen, URLError, HTTPError

# Read all the environment variables
SLACK_WEBHOOK_URL = os.environ['SLACK_WEBHOOK_URL']
SLACK_USER = os.environ['SLACK_USER']
SLACK_CHANNEL = os.environ['SLACK_CHANNEL']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Event: " + json.dumps(event))
    # Read message posted on SNS Topic
    message = json.loads(event['Records'][0]['Sns']['Message'])
    logger.info("Message: " + json.dumps(message))

        
# Construct a new slack message
    time_t = message["time"]
    userName = message["detail"]["userIdentity"]["userName"]
    sourceIP = message["detail"]["sourceIPAddress"]
    groupId = message["detail"]["requestParameters"]["groupId"]
    eventName = message["detail"]["eventName"]
    fromPort = message["detail"]["requestParameters"]["ipPermissions"]["items"][0]["fromPort"]
    toPort = message["detail"]["requestParameters"]["ipPermissions"]["items"][0]["toPort"]
    ipProtocol = message["detail"]["requestParameters"]["ipPermissions"]["items"][0]["ipProtocol"]
    cidr = message["detail"]["requestParameters"]["ipPermissions"]["items"][0]["ipRanges"]["items"][0]["cidrIp"]
    
    slack_message = {
        'channel': SLACK_CHANNEL,
        'username': SLACK_USER,
        'text': "time: %s\n userName: %s\n sourceIP: %s\n SecGroupid: %s\n eventName: %s\n fromPort: %s\n toPort: %s\n ipProtocol: %s\n cidrIP: %s\n" % (time_t, userName, sourceIP, groupId, eventName, fromPort, toPort, ipProtocol, cidr)
##        'text': "%s" % json.dumps(message.)
    }

# Post message on SLACK_WEBHOOK_URL
    req = Request(SLACK_WEBHOOK_URL, json.dumps(slack_message))
    try:
        response = urlopen(req)
        response.read()
        logger.info("Message posted to %s", slack_message['channel'])
    except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)
    except URLError as e:
        logger.error("Server connection failed: %s", e.reason)
