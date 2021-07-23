# All data retrieved from Nomics will require a key; use the following: 97256ed7630b914faff021a4a07df5fe66eb6c45
import urllib.request

# Create a string for the URL used to retrieve data
url = "https://api.nomics.com/v1/currencies/sparkline?key=97256ed7630b914faff021a4a07df5fe66eb6c45&ids=BTC,ETH," \
      "XRP&start=2018-04-14T00%3A00%3A00Z&end=2018-05-14T00%3A00%3A00Z"
# Note the &ids, &start, and &end fields. These can be changed as desired to retrieve different data. Currently,
# data on BTC, ETH, and XRP is being retrieved between the period 4/14/2018 and 5/14/2018

# Store the raw data in a variable (stored in json format)
raw_data = urllib.request.urlopen(url)
# Read the raw data into a variable (stored as a string)
string_data = raw_data.read().decode()
# Print the read data
print(string_data)

# Alternatively, data can be saved to a file as follows:
write_object = open("sample.txt", "w")
write_object.write(string_data)

# Now that the data is stored as a json string, it will have to be parsed from that string. From what I could find,
# this is a pretty common operation and there are plenty of tutorials on it. Keep in mind our json data will look like
# this (see sample.txt for actual data):

# [ { "currency" : name_of_currency, "timestamps" : [ matrix containing consecutive dates separated by a comma ],
# "prices" : [ matrix containing consecutive prices corresponding to the dates in the timestamp matrix ] } ... ]

# It is my thinking that the timestamps can be largely ignored, because each consecutive price will correspond to a day.
# I'll leave this up to the person responsible for loading data, though.



