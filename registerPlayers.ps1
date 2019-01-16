Invoke-WebRequest -Headers @{'Content-Type' = 'application/json'} `
  -Method Post `
  -Uri 'http://localhost:8080/api/players' `
  -Body '{
	"id": "a9cd1ada-c81a-463a-b997-b6ef8ee57da9",
	"name": "Giant Wipeout",
	"address": "http://10.0.75.1:9080"
}'


Invoke-WebRequest -Headers @{'Content-Type' = 'application/json'} `
  -Method Post `
  -Uri 'http://localhost:8080/api/players' `
  -Body '{
	"id": "7c3c1128-792c-46b2-afa1-1de3e55974e2",
	"name": "Purple spawn",
	"address": "http://10.0.75.1:9080"
}'

Invoke-WebRequest -Headers @{'Content-Type' = 'application/json'} `
  -Method Post `
  -Uri 'http://localhost:8080/api/players' `
  -Body '{
	"id": "cc9ddc91-2e0d-4565-af30-a39748f2344b",
	"name": "Swamp prawns",
	"address": "http://10.0.75.1:9080"
}'

Invoke-WebRequest -Headers @{'Content-Type' = 'application/json'} `
  -Method Post `
  -Uri 'http://localhost:8080/api/players' `
  -Body '{
	"id": "414d3aef-a0a4-4f1b-b2d7-b77d52df9c40",
	"name": "Blank pixies",
	"address": "http://10.0.75.1:9080"
}'
