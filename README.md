## API server of arex (Django)
#### api routes: login, ping

##### example:

###### login
```
POST http://server-ip/login
Content-Type: Application/json

{
  "code": "123456"
}
```
###### ping
```
GET http://server-ip/login