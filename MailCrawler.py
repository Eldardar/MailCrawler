###########
# Imports #
###########
import argparse
import logging
import re
import requests
from googlesearch import search

##########
# Consts #
##########
NUMBER_OF_RESULTS		= 2
CRAWLING_DEPTH			= 2
EMAIL_REGEX				= b'\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+'

#############
# Functions #
#############
def google_search(query, only_root=False):
	"""
	:query: 			- The string for the Google query
	:only_root:			- NOT SUPPORTED!
	"""
	query_results = []
	print("[*] Googling - {query}".format(query=query, ))
	for url in search(query, stop=NUMBER_OF_RESULTS, pause=0):
		query_results.append(url)

	print("[*] Found {amount} urls".format(amount=len(query_results), ))
	return query_results

def crawl_for_addresses(url, crawl_depth=0):
	mail_addresses = []
	print("[*] Requesting - {url}".format(url=url, ))
	try:
		response = requests.get(url, timeout=5)
		mail_addresses = re.findall(EMAIL_REGEX, response.content)
	except Exception as e:
		print("[X] Error - {exception}".format(exception=e, ))

	# TODO: Recursion

	return mail_addresses

def extract_mail_addresses(names_list):
	total_names = len(names_list)
	for i, name in enumerate(names_list):
		print("[*] {index}/{total}".format(index=i + 1, total=total_names))
		# Querying Google for urls
		google_results = google_search(name)
		# TODO: DUPLICATES

		# Crawling the url for mail addresses
		for url in google_results:
			mail_addresses = crawl_for_addresses(url, CRAWLING_DEPTH)

		# Returning the found mail addresses
		yield mail_addresses
		# TODO: DUPLICATES

########
# Main #
########
def main():
	# Parse arguments
	parser = argparse.ArgumentParser()
	parser.add_argument('--input-file', type=argparse.FileType('rb'), required=True, help='Path for the input file')
	parser.add_argument('--log-path', default="MailCrawler.log", help='path to the log file')
	parser.add_argument('--output-path', default="MailCrawler.output", help='path to the output file')
	parser.add_argument('--debug', action='store_true')
	args = parser.parse_args()

	# Read the wanted sites list
	data_list = args.input_file.readlines()
	args.input_file.close()

	for address_list in extract_mail_addresses(data_list):
		if address_list:
			print("[-->]" + str(address_list))
			with open(args.output_path, 'ab') as output_file:
				output_file.write(b'\n'.join(address_list) + b'\n')

	# Log the results

if __name__ == "__main__":
	main()