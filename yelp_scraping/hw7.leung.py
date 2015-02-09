import sys
import urllib
from bs4 import BeautifulSoup
import re

def preprocess_yelp_page(content):
    ''' Remove extra spaces between HTML tags. '''
    content = ''.join([line.strip() for line in content.split('\n')])
    return content

#################################################################################
# Example code to illustrate the use of preprocess_yelp_page
# You may change these four lines of code
def main():
	url1 = 'http://www.yelp.com/search?find_desc=restaurants&find_loc=San%20Francisco%2C+CA&sortby=rating&start=0#'
	url2 = 'http://www.yelp.com/search?find_desc=restaurants&find_loc=San%20Francisco%2C+CA&sortby=rating&start=10#'
	url3 = 'http://www.yelp.com/search?find_desc=restaurants&find_loc=San%20Francisco%2C+CA&sortby=rating&start=20#'
	url4 = 'http://www.yelp.com/search?find_desc=restaurants&find_loc=San%20Francisco%2C+CA&sortby=rating&start=30#'
	url5 = 'http://www.yelp.com/search?find_desc=restaurants&find_loc=San%20Francisco%2C+CA&sortby=rating&start=40#'
	urls = [url1, url2, url3, url4, url5]
	resto_name_list = []
	reviews_list = []
	count = 0 
	
	for url in urls:
		try:
			content = urllib.urlopen(url).read()
			content = preprocess_yelp_page(content) # Now *content* is a string containing the first page of search results, ready for processing with BeautifulSoup
			soup = BeautifulSoup(content)
			#print soup.prettify()
			results = soup.find_all('a',class_="biz-name",attrs={'href': re.compile("^/biz/")})
			#print results	
		
			for match in results:
				resto_name = match.string
				resto_name_list.append(resto_name)
				reviews = match.find_next(class_="review-count rating-qualifier").string
				reviews_split = reviews.split(' ')
				reviews_list.append(reviews_split)
					
		except Exception, e:
			print 'Bad URL'
			continue

	Restaurants = dict([(k, v) for k,v in zip (resto_name_list, reviews_list)])
	for key,value in Restaurants.items():
		value[0] = int(value[0]) #convert number of reviews to integer so can be sorted

	#print top 40	
	with open ('restaurants.leung.txt', 'w') as fo:
		for key,value in reversed(sorted(Restaurants.items(), key=lambda x: x[1])):
			string = "%s, %s\n" % (key,value[0])
			fo.write(string.encode("utf-8"))
			count += 1
			if count >= 40:
				break

	print 'Restaurant file complete!'

if __name__ == "__main__":
	main()

