# Utility script to download and extract the Tracy profiler server application from the Tracy repository

import os
import zipfile
import requests

tracyFolder = 'Engine/Source/ThirdParty/Tracy'
tracyServerApplicationFolder = os.path.join(tracyFolder, 'ServerApplication')
if not os.path.exists(tracyServerApplicationFolder):
	# URL for downloading the Tracy server application
	url = 'https://github.com/wolfpld/tracy/releases/download/v0.11.1/windows-0.11.1.zip'

	# Define the path where you want to download and extract the file
	zip_file_path = os.path.join(tracyFolder, 'windows-0.11.1.zip')

	# Ensure the download folder exists
	os.makedirs(tracyFolder, exist_ok=True)

	# Download the file
	print("Downloading Tracy server applcation...")
	response = requests.get(url, stream=True)

	# Check if the download was successful
	if response.status_code == 200:
		with open(zip_file_path, 'wb') as zip_file:
			for chunk in response.iter_content(chunk_size=8192):
				zip_file.write(chunk)
		print("Download completed successfully.")
	else:
		print(f"Failed to download the file. HTTP Status Code: {response.status_code}")

	# Extract the zip file
	if os.path.exists(zip_file_path):
		with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
			zip_ref.extractall(tracyServerApplicationFolder)
	else:
		print("The zip file does not exist. Download may have failed.")

	# Destroy the temporary download file
	os.remove(zip_file_path)
	