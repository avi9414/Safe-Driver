import requests
import json

# des=28.943280
# des2=77.369956
# sourcehere=str(des)+'%2C'+str(des2)
# des3=28.966337
# des23=77.642472
# destinationhere=str(des3)+'%2C'+str(des23)
# url="https://route.ls.hereapi.com/routing/7.2/calculateroute.json?waypoint0="+str(sourcehere)+"&waypoint1="+str(destinationhere)+"&mode=fastest%3Bcar%3Btraffic%3Aenabled&departure=now&apiKey=pFxtp-n9GU-BDg57vT-_oFpg5SJLeUAT-0H-WXuMKCw"
# ans=requests.get(url)
# ans=ans.json()
# print(ans),
# print(ans['response']['route'][0]['leg'][0]['maneuver'][1]['position']['latitude'],ans['response']['route'][0]['leg'][0]['maneuver'][1]['position']['longitude'])

headers = {
    'Authorization': 'prj_test_sk_9a5973ba2e210239e219957c1c79545f5b44dcbc',
}

data = {
  'deviceId': 'test_device',
  'userId': '1',
  'latitude': '28.943498',
  'longitude': '77.369886',
  'accuracy': '10'
}

response = requests.post('https://api.radar.io/v1/track', headers=headers, data=data)
print(response.status_code),
print(response.json()),


# data = {
#   'description': 'Roadfence',
#   'tag': 'venue',
#   'externalId': '2',
#   'type': 'polygon',
#   'coordinates': '[[77.4966694,28.961599],[77.4966689,28.961609],[77.4102936,28.957735],[77.4102959,28.9577159],[77.4966694,28.961599]]',
# }

# response = requests.post('https://api.radar.io/v1/geofences', headers=headers, data=data)

# #print(response.json())
# response=response.json()
# print(response)



# data = {
#   'description': 'meer',
#   'tag': 'venue',
#   'externalId': '5',
#   'type': 'circle',
#   'coordinates': '[77.700744,28.973305]',
#   'radius': '5000'
# }

# response = requests.post('https://api.radar.io/v1/geofences', headers=headers, data=data)

# #print(response.json())
# response=response.json()
# print(response)

