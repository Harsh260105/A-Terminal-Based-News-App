from asyncio.windows_events import NULL
import requests

def get_news(category):

    url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey=e5bb044d942e47e3b61af46084512d57"

    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to get news. Please check your given category.")
        return

    data = response.json()

    print("status :", data["status"])

    for article in data["articles"]:
        print("\nTitle : ", article["title"])
        print("\nDescription : ", article["description"])
        print("\n------------------------------------------------------------------\n")

for i in range(100):
    print("These are the categories you can get news of : ")
    print("And exit to exit the application.")
    print(  "1. Business\n"
            "2. Entertainment\n"
            "3. General\n"
            "4. Health\n"
            "5. Science\n"
            "6. Sports\n"
            "7. Technology")

    category = input("\nEnter the Category of news you wanna read : ")
       
    if category == "exit":
        break

    get_news(category)
