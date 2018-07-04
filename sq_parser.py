import requests
r = requests.get(url='https://6d0baa3814d5b5e4bbc64cdf8dbeb6cc0d4f60d4:@jenkins.nttsecuritylab.co.uk:9000/api/issues/search?types=VULNERABILITY&severities=BLOCKER')
print(r.json())