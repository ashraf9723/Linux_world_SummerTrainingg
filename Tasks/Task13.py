from googlesearch import search

def fetch_top_search(query):
    search_results = list(search(query, num=1, stop=1, pause=2))
    if search_results:
        return search_results[0]
    return None

query = "Linux World Pvt Ltd."
top_result = fetch_top_search(query)

if top_result:
    print("Top search result:", top_result)
else:
    print("No results found.")
