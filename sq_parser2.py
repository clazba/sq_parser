import json
import urllib.request
import csv

urlData = "https://jenkins.nttsecuritylab.co.uk:9000/api/issues/search?types=VULNERABILITY&severities=BLOCKER"

webURL = urllib.request.urlopen(urlData)

data = webURL.read()
#print(data)
encoding = webURL.info().get_content_charset('utf-8')
JSON_object = json.loads(data.decode(encoding))
#JSON_read = json.loads(data)
#print(JSON_object)
for rule in JSON_object['issues']:
    #print (rule['rule'],rule['tags'])
    rule_param = rule['rule']
    urlRuleUri = "https://jenkins.nttsecuritylab.co.uk:9000/api/rules/search?rule_key="
    urlRuleString = (urlRuleUri)+(rule_param)
    #print(urlRuleString)
    weburlRuleString = urllib.request.urlopen(urlRuleString)
    ruleData = weburlRuleString.read()
    encodingRule= weburlRuleString.info().get_content_charset('utf-8')
    RuleJSON_object = json.loads(ruleData.decode(encodingRule))
    #for name in RuleJSON_object['rules']:
    for name in RuleJSON_object['rules']:
        #print (name['name'],name['sysTags'])
        with open('rules.csv', 'w', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(name['name'])