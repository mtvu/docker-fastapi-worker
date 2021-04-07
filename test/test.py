import requests

for i in range(200):
    r = requests.post('http://ab-ubuntu-vm-node7:8001/power?x=123132&y=123123')

