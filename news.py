import requests

API_KEY = "769658cba67942b29efe8ce0e6573022"

def construct_request(keywords, fromDate, sort_by, api_key):
    endpoint = "https://newsapi.org/v2/everything?"

    search_words = ""
    if isinstance(keywords, list):
        for k in keywords:
            search_words += f"{k}%20"
    else:
        search_words = keywords
    keyword = f"q={search_words}&"

    date_from = f"from={fromDate}&"
    sort = f"sortBy={sort_by}&"
    api = f"apiKey={api_key}"

    result = endpoint + keyword + date_from + sort + api

    return result

def request_data(url):
    request = requests.get(url)
    content = request.json()

    return content

def main():
    url = construct_request(["nintendo", "games", "announce"], "2024-02-18", "relevancy", API_KEY)
    data = request_data(url)
    # print(data["totalResults"])
    for article in data["articles"]:
        print(article["title"])

if __name__ == "__main__":
    main()
