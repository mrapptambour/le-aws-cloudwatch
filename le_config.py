import os

# Logentries tokens
# This token is used to associate AWS CloudWatch logs to a log in your Logentries account.
log_token = os.environ['YOUR_LOG_TOKEN']

# You can supply an optional token to log activity to a log on Logentries and any errors from this script.
# This is optional, it is recommended you use one log file/token for all your Lambda scripts. If you do not
# wish to use this, just leave the value blank.
debug_token = os.environ.get('YOUR_DEBUG_TOKEN', '')

# Log to generic activity from this script to our support logging system for Lambda scripts
# this is optional, but helps us improve our service nad can be hand for us helping you debug any issues
# just remove this token if you wish (leave variable in place)
lambda_token = os.environ.get('LE_SUPPORT_TOKEN', '')

username = os.environ.get('YOUR_USERNAME', '')