"""
Kurt Lewis
Reads information like likes, followers, subscribers, and etc from popular social media pages from inputted urls

Written for the specific use case of Ali needed to pull information from companies. This code is fragile, and not intended to be easily modifiable.
If it was, it wouldn't be in the https://github.com/kurtlewis/quickanddirty repo.

"""
import urllib.request
import csv
import re


"""
Get's HTML of page for parsing
"""
def getHtml(url):
    return str(urllib.request.urlopen(url).read())

"""
Searches string using the given compiled regex and str
Returns only the first matching group
"""
def searchStr(regex, string):
    try:
        return regex.search(string).group(1)
    except AttributeError:
        print("Could not find Regex!")
        return None


"""
Appends to CSV of data
"""
#def appendToCsv(csvFile):


def main():
    twitterFollowers = re.compile("title=\"([\d,]*) Followers")
    twitterTweets = re.compile("title=\"([\d,]*) Tweets")
    facebookLikes = re.compile(">([\d,]*) people like this<")
    facebookFollowers = re.compile("<div>([\d,]*) people follow this</div>")
    instagramFollowers = re.compile("([\d,km]*) Followers")
    instagramPosts = re.compile("Following, ([\d,k]*) Posts")
    youtubeSubscribers = re.compile("=\"([\d,]*) subscribers")
    pinterestFollowers = re.compile("name=\"pinterestapp:followers\" content=\"([\d,]*)\"")
    #pinterestFollowers = re.compile(">([\d,]*)</span> <span class='label '>Followers") # Doesn't work?
    with open('websites.csv', 'r') as csvfile:
        websiteReader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in websiteReader:
            for url in row:
                page = getHtml(url)
                if 'twitter' in url:
                    followers = searchStr(twitterFollowers, page)
                    tweets = searchStr(twitterTweets, page)
                    print(followers)
                    print(tweets)
                if 'facebook' in url:
                    likes = searchStr(facebookLikes, page)
                    followers = searchStr(facebookFollowers, page)
                    print(likes)
                    print(followers)
                if 'instagram' in url:
                    followers = searchStr(instagramFollowers, page)
                    posts = searchStr(instagramPosts, page)
                    print(followers)
                    print(posts)
                if 'youtube' in url:
                    subscribers = searchStr(youtubeSubscribers, page)
                    print(subscribers)
                if 'pinterest' in url:
                    followers = searchStr(pinterestFollowers, page)
                    print(followers)


if __name__ == "__main__":
    main()