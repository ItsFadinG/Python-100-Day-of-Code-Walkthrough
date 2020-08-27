from datetime import datetime
import os
import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:
def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    log_text = ''.join(loglines)
    timestamp = re.findall(r"\d*-\d*-\d*\w\d*:\d*:\d*", line)
    timestamp_text = ''.join(timestamp)
    timestamp_object = datetime.strptime(timestamp_text, "%Y-%m-%dT%H:%M:%S")
    return timestamp_object

def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdown_list = []
    for i in loglines:
        if "Shutdown initiated" in i:
            shutdown_list.append(i)
    shutdown_text = ''.join(shutdown_list)
    shutdown_timestamp = re.findall(r"\d*-\d*-\d*\w\d*:\d*:\d*", shutdown_text)
    first_shutdown = datetime.strptime(shutdown_timestamp[0], "%Y-%m-%dT%H:%M:%S")
    second_shutdown = datetime.strptime(shutdown_timestamp[1], "%Y-%m-%dT%H:%M:%S")
    delta = second_shutdown - first_shutdown
    return delta
