import sys 
import requests 
from bs4 import BeautifulSoup  
from csv import writer 

response = requests.get('https://leetcode.com/shubhamk314') 
soup = BeautifulSoup(response.text, 'html.parser') 

# It will create csv files named progress.csv in root folder once this is script is called. 
with open('progress.csv', 'w') as csv_file: 
	csv_writer = writer(csv_file) 
	headers = ['Name', 'Score'] 
	csv_writer.writerow(headers) 
	csv_writer.writerow(['rohan', '90'])

print("csv file created for leetcode") 
