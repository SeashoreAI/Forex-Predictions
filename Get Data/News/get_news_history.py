import requests
import json
import datetime
import pandas as pd
from textblob import TextBlob
import os
class Blocks:
    def search(self,torank,days_back):
        self.torank = torank
        self.days_back = days_back
        self.sum_socre = 0

        # Your API key
        api_key = os.environ["API_KEY"]
        # The API endpoint for searching news
        url = "https://api.newscatcherapi.com/v2/search"

        # The parameters for the API request
        params = {
            "q": "Dollar" or "Economy" or "Politics" or "Stock Market" or "Joe Bider" or "War" or ("Shops" and "America") or ("Trade" and "America"),
            "lang": "en",
            "sort_by": "date",
            "from": (datetime.datetime.now() - datetime.timedelta(days=self.days_back)).strftime("%Y-%m-%d"),
            "to": datetime.datetime.now().strftime("%Y-%m-%d"),
            "page": 1,
            "to_rank": self.torank,
            "page_size": 50,
        }
        headers = {"x-api-key": api_key}
        # Send the API request
        response = requests.get(url,headers = headers, params=params)

        # Get the JSON data from the response
        data = json.loads(response.text)

        # Dataframe to store the results
        df = pd.DataFrame(columns=["date","title","score"])

        # Iterate through the articles
        for article in data["articles"]:
            # Get the title and date
            title = article["title"]
            date = article["published_date"]
            summary = article["summary"]
            # Get the sentiment score using TextBlob
            sentiment = TextBlob(summary).sentiment.polarity
            # Scale the score from -1 to 1 to 1 to 100
            score = (sentiment + 1) * 50
            self.sum_socre += score
            # Append the results to the dataframe
            df = df.append({"date":date,"title":title,"score":score}, ignore_index=True)
        final_day_sc = (self.sum_socre/len(data["articles"]))
        return final_day_sc
        # Save the dataframe to an excel file
'''
        with pd.ExcelWriter('USA_economy_headlines.xlsx',mode='a') as writer:  
            df.to_excel(writer,index=False,)
        print("The data has been saved to an excel file")
'''