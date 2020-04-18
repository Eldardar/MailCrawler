from googlesearch import search

def google_search_1(query):
	my_results_list = []
	for i in search(query,        # The query you want to run
	                tld = 'com',  # The top level domain
	                lang = 'en',  # The language
	                num = 10,     # Number of results per page
	                start = 0,    # First result to retrieve
	                stop = 10,  # Last result to retrieve
	                pause = 2.0,  # Lapse between HTTP requests
	               ):
	    my_results_list.append(i)
	    print(i)