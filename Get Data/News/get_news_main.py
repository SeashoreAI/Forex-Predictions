from get_news_history import Blocks
import time
search = Blocks()
days_back = 80
for i in range(0,days_back):
    search.search(2000,0)
    time.sleep(1.1)