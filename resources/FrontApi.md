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

### Edit Supervisor

> PUT api/admin/supervisor/<str:id>

Body:
```json
{
    "name":"name",
    "email":"email",
    "password":"pwd",
}
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



### Update Transfer

> supervisor/transfers/<str:id>

Moderations Status
| Key | Desc |
| --- | ---- |
| r | on review |
| c | confirmed |
| d | dismiss |

Body:
```json
{
    "group": [
        {
            "tid": "",
            "comment": ""
        }
    ],
    "status": "r|c|d"
}
```

### Get Transfer(s)

Get Transfers
> GET supervisor/transfers/

Get Transfer By ID
> GET supervisor/transfers/<str:id>

Get User Transfers
> GET supervisor/user/transfers/<str:uid>

Get Psycologist Transfers
> GET supervisor/psy/transfers/<str:uid>

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

## Transfers (Psy)

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

# Supervisor (Manage)

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






## Config

### Edit/Read Config

> PUT api/admin/settings/ 

Body:
```json
{
    "count_of_questions": 0,
    "min_count_of_diaries_for_transfer": 0,
    "count_of_diaries_each_day_for_psycologist": 0
}
```


> GET api/admin/settings/ 

Response:
```json
{
    "count_of_questions": 0,
    "min_count_of_diaries_for_transfer": 0,
    "count_of_diaries_each_day_for_psycologist": 0
}
```