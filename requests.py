import requests

#GET
response = requests.get("http://localhost:5000")
print (response.test)

#POST
responsepose("http://localhost:5000",json={"name":"Bob"})





