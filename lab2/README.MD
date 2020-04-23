 HOW DOES LOOK GET METHOD::::::::::::
 
 curl -X GET http://localhost:5000/mail -d   '{"password": "Ghera123Ad", "email": "tsetsmtp@gmail.com"}'   -H 'Content-Type: application/json'
 
 HOW DOES LOOK POST METHOD::::::::::::::
 
 curl -X POST http://localhost:5000/mail -d   '{"password": "Ghera123Ad", "email": "tsetsmtp@gmail.com", "subject": "testBack", "message": "xxxxxxxxxxxxxx test backend post method", "receiver": "adrian.gherman1@gmail.com"}'   -H 'Content-Type: application/json'