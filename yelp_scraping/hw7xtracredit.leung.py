import urllib2
import json
import oauth2
from pprint import pprint as pp 

# Please assign following values with the credentials found in your Yelp account, 
# you can find them here: http://www.yelp.com/developers/manage_api_keys 
CONSUMER_KEY = 'FLY7u79YEuEcKCOrAafh8Q'
CONSUMER_SECRET = '8DWivQGhfly4gGB8_FnyVWSeJBw'
TOKEN = 'vMyohm2bwe2aKdDTkg21K1vk9XVvjOPo'
TOKEN_SECRET = 'NXQCS8o2Ez9smm_UmAm8ljp2-H4'

def main():
    url = 'http://api.yelp.com/v2/search?term=restaurants&location=San+Francisco&sort=2&offset=0&limit=20'
    url2 ='http://api.yelp.com/v2/search?term=restaurants&location=San+Francisco&sort=2&offset=20&limit=20'
    #pp(yelp_req(url))
    resto_dict = yelp_req(url)
    resto_dict2 = yelp_req(url2)
    resto_name = []
    resto_reviews = []
    for dict_item in resto_dict['businesses']:
        resto_name.append(dict_item['name'])
        resto_reviews.append(dict_item['review_count'])
    for dict_item in resto_dict2['businesses']:
        resto_name.append(dict_item['name'])
        resto_reviews.append(dict_item['review_count'])

    Restaurants = dict([(k, v) for k,v in zip (resto_name, resto_reviews)])

    for key,value in Restaurants.items():
        value = int(value) #convert number of reviews to integer so can be sorted

    # print Restaurants
    with open ('restaurants2.leung.txt', 'w') as fo:
        for key,value in reversed(sorted(Restaurants.items(), key=lambda x: x[1])):
            string = "%s, %s\n" % (key,value)
            fo.write(string.encode("utf-8"))

# yelp_req() function description:
# The input is a url link, which you use to make request to Yelp API, and the 
# return of this function is a JSON object or error messages, including the information 
# returned from Yelp API.
# For example, when url is 'http://api.yelp.com/v2/search?term=food&location=San+Francisco'
# yelp_req(url) will return a JSON object from the Search API

def yelp_req(url):
    """ Pass in a url that follows the format of Yelp API,
        and this function will return either a JSON object or error messages.
    """
   
    oauth_request = oauth2.Request('GET', url, {})
    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': TOKEN,
            'oauth_consumer_key': CONSUMER_KEY
        }
    )
    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    token = oauth2.Token(TOKEN, TOKEN_SECRET)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()

    conn = urllib2.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()
    
    return response
   

#################################################################################
# Your code goes here

if __name__ == "__main__":
    main()


