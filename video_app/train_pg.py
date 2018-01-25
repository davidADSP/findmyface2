import cognitive_face as CF
import json

KEY = '89ab23ac10744742b8e3a6589ed766a6'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

BASE_URL = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)


personGroupId = "users";
CF.person_group.train(personGroupId)

