import json
import urllib.request

def rule_param():

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

def rule_lookup ():
	RuleJSON_object = json.loads(data.decode(encodingRule))
	#for name in RuleJSON_object['rules']:
	print (RuleJSON_object)
	#break
	#\print (RuleJSON_object)

rule_lookup()
