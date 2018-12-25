import argparse
import sys
import time
from selenium import webdriver
import random

parser = argparse.ArgumentParser(description='Set an alarm to open a URL')
parser.add_argument('-t', '--Time', type=str, required=True, dest="wake_time", help='Time to set alarm for')
parser.add_argument('-b', '--Browser', type=str, required=True, dest="web_browser",
                    help='Browser to open URL in. Choose either firefox or chrome')
parser.add_argument('-U', '--URL', type=str, required=False, dest="url_to_open", help='URL to open')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-r', '--openatandom', action='store_true', dest="random", help='Selects url at random')
group.add_argument('-u', '--openbyurl', action='store_true', dest="url", help='Selects url given as argument')

results = parser.parse_args()


# time convert to proper format (at least proper for the programmer who rote the code)
def process_time(wake_time):
    wake_time = results.wake_time.replace(" ", "").replace(":", "")

    try:
        return time.strftime("%H%M", time.strptime(wake_time, "%H%M"))
    except:
        pass
    try:
        return time.strftime("%H%M", time.strptime(wake_time, "%H%M%P"))
    except:
        raise Exception("You entered the time in wrong format")


# play video (like that wasn't obvious)
def play_video(url):
    user_browser = results.web_browser.lower()
    if user_browser == 'firefox':
        webdriver.Firefox().get(url)
    elif user_browser == 'chrome':
        webdriver.Chrome().get(url)
    else:
        raise Exception("Browser unidentified")


# returns random url from urls stored in file
def random_url(file_name):
    file = open(file_name, 'r')
    urls = file.readlines()
    print(urls)
    return random.choice(urls)


def get_url():
    if results.random:
        return random_url('links.txt')
    else:
        if results.url_to_open is None:
            raise Exception('URL must be provided if -r is specified')
        else:
            return results.url_to_open


url = get_url()

while True:
    current_time = time.strftime("%H%M")
    wake_time = process_time(results.wake_time)
    sys.stdout.write("Time right now is " + current_time + ". The time alarm is scheduled to go off is " + wake_time)
    if current_time == wake_time:
        play_video(url)
        break
    time.sleep(30)
