import requests, json
from requests import Request, Session

#Imput Names credential, Organization, discovery
nameCredential = raw_input("Insert the name credential: ")
nameOrganization = raw_input("Insert the name Organization: ")
namediscovery = raw_input("Insert the name Organization: ")

#Create Credential and save lastCredential ID
s = requests.Session()
s.auth = ('em7admin', 'em7admin')
urlCredential = "http://172.26.93.101/api/credential/powershell"
jsonCredential = json.dumps({"cred_name": "serverScript1","cred_user": "administrator","cred_pwd": "MTat2019","cred_host": "10.30.140.167","cred_port": "5985","cred_timeout": "1000","ps_account_type": "2"})
jsonCredential = jsonCredential.replace("serverScript1", nameCredential)
credentialRequest = s.post(urlCredential, jsonCredential)
allCredentials= s.get("http://172.26.93.101/api/credential/powershell")
responseCredendial = allCredentials.json()
lastCredential=responseCredendial[u'result_set'][-1][u'URI']

#Create Organization and save lastOrganization ID
urlOrganization = "http://172.26.93.101/api/organization"
jsonOrganization = json.dumps({"updated_by": "/api/account/1","company": "testPostScript1","city": "Los Angeles","state": "LA","country": "US","contact_fname": "Jose","contact_lname": "Gala","theme": "1"})
jsonOrganization = jsonOrganization.replace("testPostScript1", nameOrganization)
organizationRequest = s.post(urlOrganization, jsonOrganization)
allOrganizations = s.get("http://172.26.93.101/api/organization")
responseOrganization = allOrganizations.json()
lastOrganization=responseOrganization[u'result_set'][-1][u'URI']


#Create Discovery Session
urlDiscovery = "http://172.26.93.101/api/discovery_session_active"
jsonDiscovery = json.dumps({"organization":"/api/organization/0","discover_non_snmp": "1","scan_ports": ["21","22","23","25","80"],"dhcp_enabled": "0","log_all": "1","aligned_collector":"/api/appliance/2","name":"discoverytestScript1","interface_inventory_timeout": "600000","max_interface_inventory_count": "10000","ip_lists": [{"start_ip": "10.30.140.167","end_ip": "10.30.140.167"}],"credentials": ["/api/credential/powershell/1"]})
jsonDiscovery = jsonDiscovery.replace("discoverytestScript1", namediscovery)
jsonDiscovery = jsonDiscovery.replace("/api/organization/0", lastOrganization)
jsonDiscovery = jsonDiscovery.replace("/api/credential/powershell/1", lastCredential)
s.post(urlDiscovery, jsonDiscovery)