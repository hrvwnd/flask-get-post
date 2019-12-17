from flask import Flask 
import requests

#GET
response = requests.get("http://localhost:5000")
print (response.text)

#POST
requests.post("http://localhost:5000",json={"name":"Bob"})







