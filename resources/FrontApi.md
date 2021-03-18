# Admin
### Methods
- Login

### Login (SignIn)
> POST /auth/token/login/

Body:
```json
{
    "email": "user@email.ru",
    "password": "user-loliallen"
}
```
Response:
```json
{
    "auth_token": "4e80dd34f02321f3658e2d29de4f9db197d12f8d"
}
```

> For each subsequent query put the field `auth_token` in the header `Authorization: Token <token>`

# Supervisors
> Admin Auth Required
>> Tomorrow here will be autheication methods

### Create Supervisor
> POST /supervisor/manage/

Body:
```json
{
    "name":"name",
    "email":"email",
    "password":"pwd",
}
```


### Get All Supervisors
> Get /supervisor/manage/

Response:
```json
[
    {
        "name":"name",
        "email":"email",
        "password":"pwd",
    },
    {
        "name":"name",
        "email":"email",
        "password":"pwd",
    },
    {
        "name":"name",
        "email":"email",
        "password":"pwd",
    },
    {
        "name":"name",
        "email":"email",
        "password":"pwd",
    },
]
```

### Basic Authenication (not confirmed)

> POST /supervisor/authentication/signin

Body:
```json
{
    "email":"email",
    "password":"pwd",
}
```

# Psychologists

## Authenication

### Login
> POST /api/psycologists/authentication/signin

body:
```json
{
    "username": "uname", 
    "password": "pwd" 
}
```


### Register
> POST /api/psycologists/authentication/signup

body:
```json
{
    "username": "uname", 
    "password": "pwd" ,
    "name": "name"
}
```

## Transfers

### Get Transfers
> GET /api/psycologists/transfers/

response:
```json
    ...?
```

### Update Transfer
> PUT /api/psycologists/transfers/


Choices:
| key | value |
| --- | ----- |
| i   | idle |
| s   | searching (default) |
| r   | on review |
| a   | answered |
| d   | dismiss |



body:
```json
{
    "group": [
        {
            "tid": "transfer_id",
            "fb": "transfer_feedback",
        }
    ],
    "status": "<choices>"
}   
```

response:
```json
    ...?
```

# Supervisor

## Psycologist patients

### Append patient to psy

> POST /api/psycologists/patients/<str:id>
>> id - psychologist ID


body:
```json
{
    "patient_id" : "patient_id"
}
```

### Remove patient from psy

> DELETE /api/psycologists/patients/<str:id>
>> id - psychologist ID


body:
```json
{
    "patient_id" : "patient_id"
}
```