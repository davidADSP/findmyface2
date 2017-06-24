import cognitive_face as CF

KEY = '77abe08c92574606aa8aa15b3c987e7f'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

BASE_URL = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)



// Create an empty person group
personGroupId = "myfriends";
CF.person_group.delete(personGroupId)
CF.person_group.create(personGroupId, name = "My Friends");

// Define people
obama = CF.person.create(personGroupId, name = "Obama");
cumberbatch = CF.person.create(personGroupId, name = "Cumberbatch");
maggie = CF.person.create(personGroupId, name = "Maggie");
jolie = CF.person.create(personGroupId, name = "Jolie");



CF.person.add_face('./img/obama.jpeg', personGroupId, obama['personId'])
CF.person.add_face('./img/cumberbatch.jpeg', personGroupId, cumberbatch['personId'])
CF.person.add_face('./img/maggie.jpeg', personGroupId, maggie['personId'])
CF.person.add_face('./img/jolie.jpeg', personGroupId, jolie['personId'])

CF.person_group.train(personGroupId)
