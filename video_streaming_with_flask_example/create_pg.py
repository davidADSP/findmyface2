import cognitive_face as CF
import json

KEY = '77abe08c92574606aa8aa15b3c987e7f'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

BASE_URL = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)


personGroupId = "myfriends";
CF.person_group.delete(personGroupId)
CF.person_group.create(personGroupId, name = "My Friends");


obama = CF.person.create(personGroupId, name = "Obama", user_data=json.dumps({"skills":["R","Python","SQL"]}));
cumberbatch = CF.person.create(personGroupId, name = "Cumberbatch", user_data=json.dumps({"skills":["Design","UX","Photoshop"]}));
maggie = CF.person.create(personGroupId, name = "Maggie", user_data=json.dumps({"skills":["Presentation","Pitching","Start-ups"]}));
jolie = CF.person.create(personGroupId, name = "Jolie", user_data=json.dumps({"skills":["Management","Projects","Finance"]}));

CF.person.add_face('./img/obama.jpeg', personGroupId, obama['personId'])
CF.person.add_face('./img/cumberbatch.jpeg', personGroupId, cumberbatch['personId'])
CF.person.add_face('./img/maggie.jpeg', personGroupId, maggie['personId'])
CF.person.add_face('./img/jolie.jpeg', personGroupId, jolie['personId'])

CF.person_group.train(personGroupId)
