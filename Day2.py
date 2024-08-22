#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[ ]:


import numpy as np
my_list = [1,2,3,4,5]
arr=np.array(my_list) #converting a list to array using np.array
print(arr)
new_numbr = 100
new_arr = np.append(arr,new_numbr)
print("Array after adding numbers:", new_arr)


# # Question2
# 

# In[4]:


my_list = [1,2,3,4,5,6]
arr=np.array(my_list) 
num_elements = int(input("How many elements do you want to add? "))
for _ in range(num_elements):
    element = float(input("Enter a number to add to the array: "))
    arr = np.append(arr, element)
print("Final array:", arr)


# # Question3
# 

# In[7]:



import json

json_data = '''
{
    "date": "2024-08-20",
    "explanation": "This is a sample explanation of the Astronomy Picture of the Day.",
    "hdurl": "https://example.com/hdurl",
    "media_type": "image",
    "service_version": "v1",
    "title": "Sample APOD Title",
    "url": "https://example.com/image.jpg"
}
'''

data = json.loads(json_data)

explanation = data.get("explanation", "No explanation available")
title = data.get("title", "No title available")

print("Explanation:", explanation)
print("Title:", title)


# # Question4

# In[8]:



import requests

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")


# # Question5

# In[9]:



import requests

url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    iss_position = data.get("iss_position", {})
    timestamp = data.get("timestamp")
    
    latitude = iss_position.get("latitude", "No data")
    longitude = iss_position.get("longitude", "No data")
    
    print("Latitude:", latitude)
    print("Longitude:", longitude)
    print("Timestamp:", timestamp)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")


# # Question6 

# In[ ]:



import requests
import pandas as pd
import time

url = "http://api.open-notify.org/iss-now.json"

num_records = 100

timestamps = []
latitudes = []
longitudes = []

for _ in range(num_records):
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        timestamp = data.get("timestamp")
        iss_position = data.get("iss_position", {})
        
        latitude = iss_position.get("latitude")
        longitude = iss_position.get("longitude")
        
        timestamps.append(timestamp)
        latitudes.append(latitude)
        longitudes.append(longitude)
        
        time.sleep(10)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        break

df = pd.DataFrame({
    "Timestamp": timestamps,
    "Latitude": latitudes,
    "Longitude": longitudes
})

df.to_csv("iss_location_data.csv", index=False)

print("Data has been written to iss_location_data.csv")


# In[ ]:




