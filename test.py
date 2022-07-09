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
    },
    {
      "event": "Communication between Technology and Information"
       "time":06h30
      }
  ] 
}
'''

data = json.loads(event_string)

print(data)
