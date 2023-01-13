import requests
import json
import datetime
import pandas as pd
from textblob import TextBlob

# Your API key
api_key = "api"

# The API endpoint for searching news
url = "https://api.newscatcherapi.com/v2/search"

# The parameters for the API request
params = {
    "q": "USA economy",
    "lang": "en",
    "sort_by": "relevancy",
    "from": (datetime.datetime.now() - datetime.timedelta(days=365)).strftime("%Y-%m-%d"),
    "to": datetime.datetime.now().strftime("%Y-%m-%d"),
    "page": 1,
    "page_size": 100,
    "api_key": api_key
}

# Send the API request
response = requests.get(url, params=params)

# Get the JSON data from the response
data = json.loads(response.text)

# Dataframe to store the results
df = pd.DataFrame(columns=["date","title","score"])

# Iterate through the articles
for article in data["articles"]:
    # Get the title and date
    title = article["title"]
    date = article["published_at"]
    # Get the sentiment score using TextBlob
    sentiment = TextBlob(title).sentiment.polarity
    # Scale the score from -1 to 1 to 1 to 100
    score = (sentiment + 1) * 50
    # Append the results to the dataframe
    df = df.append({"date":date,"title":title,"score":score}, ignore_index=True)

# Save the dataframe to an excel file
df.to_excel("USA_economy_headlines.xlsx", index=False)

print("The data has been saved to an excel file")