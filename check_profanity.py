import urllib.request

def read_text():
	quotes = open('movie_quotes.txt')
	contents_of_file = quotes.read()
	print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)
	#check_profanity("tits%20shit")
	
def check_profanity(text_to_check):
	# replace spaces with % equivalent of space
	text_to_check = text_to_check.replace(" ","%20")
	# replace newlines with % equivalent of space
	text_to_check = text_to_check.replace("\n","%20")	
	url = "http://www.wdylike.appspot.com/?q=" + text_to_check
	print(url)
	connection = urllib.request.urlopen(url)
	output = connection.read()
	connection.close()

	if "false" in str(output):
		print("No profanity was found")
	elif "true" in str(output):
		print("Profanity Alert!!!")
	else:
		print("Unable to process the text")
			
read_text()