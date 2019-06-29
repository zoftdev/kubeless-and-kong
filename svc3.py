def echo(event, context):
  print event
  event['host']='svc3'
  return event['host']
