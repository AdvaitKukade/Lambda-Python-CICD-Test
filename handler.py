# handler.py
import requests

def main(event, context):

    print("event:", event, "context:", context)

    r = requests.get("http://www.google.com")

    print(r.status_code)