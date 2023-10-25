from googlesearch import search

def perform_google_search(query):
    results = []
    # Perform the search
    for result in search(query, tld="co.in", num=10, stop=10, pause=2):
        results.append(result)
    return results

def main():
    # Get the search query from the user
    query = input("Enter your search query: ")

    # Perform the Google search
    search_results = perform_google_search(query)

    # Display the results
    print("Search Results:")
    for result in search_results:
        print(result)

if __name__ == "__main__":
    main()
