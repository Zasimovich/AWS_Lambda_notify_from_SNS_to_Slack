# AWS_Lambda_notify_from_SNS_to_Slack
In the beggining you need to create chaint AWS CloudTrail -> AWS CloudWatch -> AWS SNS -> AWS Lambda
part of tutorial from youtube video - https://www.youtube.com/watch?v=lD8tIkrJeZU
## Script has written for Python 2.7
Environment variables for AWS Lambda:

- SLACK_CHANNEL:	channel-name 
- SLACK_USER:	AWS
- SLACK_WEBHOOK_URL:	https://hooks.slack.com/services/XXX/XXX/XXX
