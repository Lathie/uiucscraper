
import requests
import xml.etree.ElementTree as ET
from twilio.rest import Client

account_sid = "" #fill this later
auth_token = "" #fill this later

url_425 = "https://courses.illinois.edu/cisapp/explorer/schedule/2017/fall/CS/425/36091.xml"

def do_shit(url):

    r = requests.get(url)
    tree = ET.fromstring(r.text)
    cur_status = tree[7].text.strip()
    print(cur_status)
    if cur_status == "Closed":
        print("Fuck")
    else:
        send_shit()


def send_shit():
    client = Client(account_sid, auth_token)
    # fill this in after


if __name__ == "__main__":
    do_shit(url_425)
