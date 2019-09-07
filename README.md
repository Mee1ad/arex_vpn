## API server of arex (Django)
#### api routes: login, ping

##### example:

###### ----------- login -----------
******* Request *******
```
POST http://server-ip/login
Content-Type: Application/json

{
  "code": "123456"
}
```
******* Response *******
```
{
  "data": 324000000,
  "time": 1525137
}
```
###### ----------- ping -----------
******* Request *******
```
GET http://server-ip/login
```
******* Response *******
```
{
  "message": "pong"
}
```