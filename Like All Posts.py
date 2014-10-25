import requests
import json
import time
print "Welcome to Like All Posts"
Token = raw_input("\nGo to https://developers.facebook.com/tools/explorer ,\nclick on get access token,\ncheck on all the permissions in basic and extended permissions \nand paste the access token here\n")
PAGEID = raw_input("\nEnter the numeric page_id/user_id, you can get it in the URL of the page/user.Ex:www.facebook.com/pageid\n")
print "\nPlease wait while all the posts by " + PAGEID + " are being liked\n"

def like():
    r = requests.get("https://graph.facebook.com/" + PAGEID + "/posts?access_token=" + Token)
    result = json.loads(r.text)
    for wallpost in result['data']:
        requests.post("https://graph.facebook.com/" + str(wallpost['id']) + "/likes/?access_token=" + Token + "&method=POST")
    print "\nAll posts liked!\n"

if __name__ == '__main__':
    like()
