import cognitive_face as CF

KEY = '77abe08c92574606aa8aa15b3c987e7f'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

BASE_URL = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
result = CF.face.detect(img_url)
print result[0]