import os

def rename_files():
	# (1) get file names from a folder - path listed below is for Android 9
	image_directory = "/sdcard/Download/prank/prank"
	file_list = os.listdir(image_directory)
	print(file_list)
	
	saved_path = os.getcwd()
	print("Current Working directory is " + saved_path)

	# change to the directory with the images so we can work with them without
	# specifying the full path plus the image file name 	
	os.chdir(image_directory)
	
	# (2) for each file, rename filename
	for file_name in file_list:
		print("Old filename" + file_name)
		print("New filename" + file_name.translate(str.maketrans('','','1234567890')))
		# in python v2.7.x the code would be
		# os.rename(file_name, file_name.translate(None,'1234567890'))
		os.rename(file_name, file_name.translate(str.maketrans('','','1234567890')))

	#change the current directory back to the original directory		
	os.chdir(saved_path)
	
rename_files()