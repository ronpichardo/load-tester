import requests
import threading, logging
from fake_useragent import UserAgent

website = 'http://10.0.0.61'
threads_to_run = 5000
# logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-10s) %(message)s')

def make_request():
    try:
        # Randomize user-agent headers
        ua = UserAgent()
        headers = {
            'User-Agent': ua.random
        }
        r = requests.get(website, headers=headers)

        # print(r.status_code)
    except Exception as e:
        print(e)
    
    return

threads = []
for i in range(threads_to_run):
    t = threading.Thread(target=make_request)
    threads.append(t)
    t.start()