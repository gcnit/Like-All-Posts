import requests
import json
import time
print "Welcome to Like All Posts"
Token = raw_input("\nGo to https://developers.facebook.com/tools/explorer ,\nclick on get access token,\ncheck on all the permissions in basic and extended permissions \nand paste the access token here\n")
PAGEID = raw_input("\nEnter the numeric page_id/user_id, you can get it in the URL of the page/user.Ex:www.facebook.com/pageid\n")
print "\nPlease wait while all the posts by " + PAGEID + " are being liked\n"

def like():
    query = ("SELECT post_id FROM stream WHERE "
            "source_id ="+PAGEID+"  AND actor_id="+PAGEID+" LIMIT 200")
    payload = {'q': query, 'access_token': Token}
    r = requests.get('https://graph.facebook.com/fql', params=payload)
    result = json.loads(r.text)
    for wallpost in result['data']:
        requests.post("https://graph.facebook.com/" + str(wallpost['post_id'])
                      + "/likes/?access_token=" + Token
                      + "&method=POST")        
    print "\nAll posts liked!"

if __name__ == '__main__':
    like()
