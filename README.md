## API server of arex (Django)

##### api routes: login, ping


###### ----------- login -----------
Request
```
POST http://server-ip/login
Content-Type: Application/json

{
  "code": "123456"
}
```
"code": user password - 1

Response
```
{
  "data": 324000000,
  "time": 1525137
}
```
"data": remaining data
"time": remaining time
###### ----------- ping -----------
Request
```
GET http://server-ip/login
```
Response
```
{
  "message": "pong"
}
```