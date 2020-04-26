import tweepy
import time 
import json
import requests

consumerkey = ""
consumersecret = ""
accesstoken = ""
accesstokensecret = ""

auth = tweepy.OAuthHandler(consumerkey,consumersecret)
auth.set_access_token(accesstoken,accesstokensecret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
except:
    print("Invalid API!")
print('API Success')

def parseDate(RTDate):
    #print(date)
    d = str(RTDate)
    d=d[:-9]
    l= list(d.split("-"))
    day = int(l[2])
    day=day-1
    day=str(day)
    # print(day)
    monthDict={'01':'January', '02':'February ', '03':'March ', '04':'April ', '05':'May ', '06':'June ', '07':'July ', '08':'August ', '09':'September ', '10':'October ', '11':'November ', '12':'December '}
    month = monthDict.get(l[1])
    date=day+" " + month
    print(date)

    response = requests.get("https://api.covid19india.org/data.json")
    status=response.json()

    l1 = status['cases_time_series']
    final_dict = dict()
    for i in l1:
        if (i['date'] == date):
            final_dict = i

    confirmed=final_dict.get('totalconfirmed')
    deceased=final_dict.get('totaldeceased')
    recovered=final_dict.get('totalrecovered')
    message = "Current Status in India on "+ date + "\n C: " + confirmed + "\n D: " + deceased + "\n R: " + recovered + "\n"
    return message
    
for tweet in api.search(q='#COVIDIndiaStatus',rpp=1):
    RTDate = tweet.created_at
    username = tweet.user.screen_name
RTMessage = parseDate(RTDate)
print(RTMessage)
api.update_status(RTMessage + '@' + username)



