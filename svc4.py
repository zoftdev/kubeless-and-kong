import json
def echo(event, context):
  print event
  ret={}
  ret['data']=event['data']
  ret['host']='svc4'
  retjson= json.dumps(ret)
  print retjson
  return  retjson
