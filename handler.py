# handler.py
import requests
import datetime

def main(event, context):

    print("event:", event, "context:", context)

    r = requests.get("http://www.google.com")

    print(r.status_code)

    print("Hello, if you see this, this means that you are done with ci-cd")
    print("Congratulations !")
    print("You did it")

    x = datetime.datetime.now()
    print("Current Date Time - " + x)