### JavaScript Obnect Notation ###
import json

event_string = '''
{
  "events": [
    {
        "event": "Puppet show",
        "time": 1330
    },
    {  
        "event": "Spectacle du Marionette",
        "time": 1500
    }
  ] 
}
'''

data = json.loads(event_string)

for event in data['events']:
  del event['time']

print(data['events'])
