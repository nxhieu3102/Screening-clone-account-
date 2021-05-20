import requests

r = requests.get('http://techtv.mit.edu/videos/1585-music-session-02/download.source') 
for i in r.history:
    print(i.url) 