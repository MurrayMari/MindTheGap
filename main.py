# current problems - how to often to refresh? 

# code to write - if internet inop light up all 

import requests
# from config import apikey, apiname

# Transport for London's OpenAPI.
# https://github.com/ZackaryH8/tube-naptan?tab=readme-ov-file ->>> naptan tube station ids
# Calling the api
# url = 'https://api.tfl.gov.uk/Line/Mode/tube/Disruption'
# response = requests.get(url)
# currentissues = response.json()
# print(currentissues)

# "naptanID":"940GZZLUPCC","commonName":"Piccadilly Circus Underground Station"
# {"naptanID":"940GZZLUBSC","commonName":"Barons Court Underground Station"}
class myStop:

  def __init__(self):
    pass
# Calling the api

# lineName = input('Enter Line name: ')
# naptanID = input('Enter station naptanID: ')

  def get_line(lineName, naptanID):
    
    # returns 
    url = "https://api.tfl.gov.uk/Line/{}/Arrivals/{}?direction=inbound".format(lineName, naptanID)
    newresponse = requests.get(url)
    next = newresponse.json()
    # for i in next:
    #   # print((int(i['timeToStation']))/60)
    #   print('Time to next train is', int(i['timeToStation'])/60,, 'The train is currently at', i['currentLocation'], 'It is due at', i['expectedArrival'])
    return next
  
  def next_train_times()


# lineName = 'Piccadilly'
# naptanID = '940GZZLUBSC'

s = myStop()
s.get_line('Piccadilly' '940GZZLUBSC')



# url = "https://api.tfl.gov.uk/Line/{}/Arrivals/{}?direction=inbound".format(lineName, naptanID)
# newresponse = requests.get(url)
# next = newresponse.json()

# print(type(next[1]))
