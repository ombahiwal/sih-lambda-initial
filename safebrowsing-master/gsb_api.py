import safebrowsing

apikey = 'AIzaSyASwRXWJOVBzJZnW6iD2OsCnZ0yCJvtyas'
sb = safebrowsing.LookupAPI(apikey)
resp = sb.threat_matches_find('ihaveaproblem.info','http://testsafebrowsing.appspot.com/apiv4/ANY_PLATFORM/MALWARE/URL/')
print(resp)