import json, sys, os
d = json.load(sys.stdin)['assets']
for a in d:
    if a['name'].startswith(sys.argv[1]):
        os.system('curl -u jimhester:' + os.getenv('GH_TOKEN') + ' -X DELETE ' + a['url'])
