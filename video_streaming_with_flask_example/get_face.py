import httplib, urllib, base64, json



def get_attributes(image,conn, headers, params):

    # The URL of a JPEG image to analyze.
   # body = "{'url':'https://upload.wikimedia.org/wikipedia/commons/c/c3/RH_Louise_Lillian_Gish.jpg'}"
   # body = image
    try:
        # Execute the REST API call and get the response.
        
        conn.request("POST", "/face/v1.0/detect?%s" % params, image, headers)
        response = conn.getresponse()
        data = response.read()

        # 'data' contains the JSON data. The following formats the JSON data for display.
        parsed = json.loads(data)
        print(data)
        #json_out = json.dumps(parsed, sort_keys=True, indent=2)
        return parsed
        #conn.close()

    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))