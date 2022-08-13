import requests
from iterfzf import iterfzf


def search(query: str):
    r = requests.get(f"https://hn.algolia.com/api/v1/search?query={query}").json()['hits']
    r_dict = {}
    for result in r:
        r_dict.update({result["title"]: result["url"]})
    return r_dict

query = input("query > ")
search_result = search(query)
print(search_result[iterfzf(search_result)])
