from twython import Twython
from .recognizer import Processor

APP_KEY = 'ZpNbu2Hak8S1P6OsYALWQWMSi'
APP_SECRET = '0GG0p3UNAHO4FsbB2InQ5l7pHyi8WNpXZQw0W8WwSgkhOIppWU'
OAUTH_TOKEN = '880413860708012033-5gnESkPKZMXGrAXZOV3iRUIVCfKPFOf'
OAUTH_TOKEN_SECRET = 'vGnJKwILxTuze8fCeL78ysSyoZuZWnKtlpl07UM6kE9c0'


twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN,
    OAUTH_TOKEN_SECRET)

class Tweet:

    def __init__(self):
        self.data_list_number = []
        self.tweets = []
        self.dataset = {}

    def Search(self, query, searchnum):

        for qu in query:
            pos_num = 0
            neg_num = 0
            results = twitter.cursor(twitter.search, q=qu, lang='en')

            for result in results:
                text = result["text"]
                if len(self.tweets) == int(searchnum):
                    break
                self.tweets.append(text)
                status = Processor(text)
                if status == "Positive":
                    pos_num += 1
                elif status == "Negative":
                    neg_num += 1
                else:
                    print("Error...")
                    pass
            self.data_list_number.append(pos_num)
            self.data_list_number.append(neg_num)
            self.dataset[qu] = [i for i in self.data_list_number]
            self.data_list_number.clear()
            self.tweets.clear()

