from flask import Flask, request, render_template
import requests
import Keys


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/directions',methods = ['POST', 'GET'])
def navi():
	sor = request.form['source']
	des = request.form['destination']
	headers = {
    'Authorization': Keys.radarapi,
	}
	
	url='https://api.radar.io/v1/geocode/forward?query='+str(sor)
	response =requests.get(url, headers=headers)
	response=response.json()
	des=response['addresses'][0]['latitude']
	des2=response['addresses'][0]['longitude']
	source=str(des)+','+str(des2)
	sourcehere=str(des)+'%2C'+str(des2)
	url='https://api.radar.io/v1/geocode/forward?query='+str(des)
	response =requests.get(url, headers=headers)
	response=response.json()
	des=response['addresses'][0]['latitude']
	des2=response['addresses'][0]['longitude']
	
	# for i in range(len(ans['response']['route'][0]['leg'][0]['maneuver'])):
	# 	lat=ans['response']['route'][0]['leg'][i]['maneuver']['latitude']
	# 	longi=ans['response']['route'][0]['leg'][0]['maneuver']['longitude']
	destination=str(des)+','+str(des2)
	destinationhere=str(des)+'%2C'+str(des2)
	url="https://route.ls.hereapi.com/routing/7.2/calculateroute.json?waypoint0="+str(sourcehere)+"&waypoint1="+str(destinationhere)+"&mode=fastest%3Bcar%3Btraffic%3Aenabled&departure=now&apiKey="+Keys.hereapi
	ans=requests.get(url)
	ans=ans.json()	
	lat2=ans['response']['route'][0]['leg'][0]['maneuver'][1]['position']['latitude']
	long2=ans['response']['route'][0]['leg'][0]['maneuver'][1]['position']['longitude']
	fenccent='['+str(long2)+','+str(lat2)+']'
	data = {
  'description': 'hwll',
  'tag': 'venue',
  'externalId': '4',
  'type': 'circle',
  'coordinates': fenccent,
  'radius': '50'
	}

	response = requests.post('https://api.radar.io/v1/geofences', headers=headers, data=data)
	print(response.json())
	waypnts={'s_begin':source,'s_end':destination}
	return render_template('directions.html',waypnts=waypnts)

if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run(debug=True) 