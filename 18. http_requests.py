import requests

''' 1. To get html content from a web page '''
r = requests.get('https://xkcd.com/353/')

print(dir(r))
print(r.text) # html

''' 2. To get image from a web url and save it in local '''
img_r = requests.get('https://imgs.xkcd.com/comics/python.png')
print(img_r.content) # binary

with open('comic.png', 'wb') as f:
    f.write(img_r.content)

print(img_r.status_code)

"""
    Basic - Status Codes:
    ---------------------
    200s    -   Success
    300s    -   Redirects    
    400s    -   Client Errors (Access related)
    500s    -   Server Errors
"""

print(img_r.ok) # Except 400s & 500s, others comes OK!
print(img_r.headers)


""" Helpful website to grasp requests concepts easier - https://httpbin.org """

''' 1. Get Method '''

payload = {'page': 2, 'count':25}
r = requests.get('https://httpbin.org/get',params=payload)
print(r.url) # Requested Url
print(r.text)

''' 2. Post Method '''
payload = {'username': 'corey', 'password': 'testing'}
qParams = {'page': 5}
r = requests.post('https://httpbin.org/post',data=payload, params=qParams)
r_dict = r.json()
print(r_dict['form'])


''' 3. Basic Authentication '''
r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey','testing'))
print(r)

''' 4. Setting Timeouts '''
seconds = 2.7
r = requests.get(f'https://httpbin.org/delay/{seconds}', timeout=3)
print(r)