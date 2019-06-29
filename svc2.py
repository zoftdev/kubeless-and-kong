import requests
import json
def echo(event, context):
  
# api-endpoint 
  URL = "http://kong-poc-svc3.default.arctic.true.th"
  input=json.loads(event['data'])
  if input['url'] is not None:
    URL = input['url']
    
# location given here 
  location = "svc2"
  
# defining a params dict for the parameters to be sent to the API 
  PARAMS = {'from':location} 
  
# sending get request and saving the response as response object 
  r = requests.get(url = URL, params = PARAMS) 
  
# extracting data in json format 
  data= json.dumps( {'action':'svc2 call to '+URL , 'data':r.text})
  print data
  return data
