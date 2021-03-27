# API
- [User](#-user)
- [Diary](#-diary)
- [Record](#-record)
- [TitleRecord](#-titlerecord)
- [Psycologist(Psychologist)](#-psycologist)
- [Questions](#-questions)
- [Transfers](#-transfers)
- [Supervisors](#-supervisors)


# User
### Methods
- Create User (Sign Up)
- Login
- Create Children
- Remove Children
- Update
- Get Info

### Create User (SignUp)
> POST /auth/users/

Body:
```json
{
    "name": "name",
    "username": "uname",
    "password": "pwd",
    "age": 1,
}
```
Response:
```json
{
    "email": "",
    "username": "uname",
    "_id": "604644edfc3c9a169d9ce85b"
}
```
### Login (SignIn)
> POST /auth/token/login/

Body:
```json
{
    "username": "user",
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

### Add(Create) children
> POST account/children

Body:
```json
{
    "children": [
        {
            "sex": "M|F",
            "age": 12,
        },
        {
            "sex": "M|F",
            "age": 12,
        },
    ]
}
```

### Remove (dead?) children
> DELETE account/children

Body:
```json
{
    "children": [
        "$oid",
        "$oid",
    ]
}
```

Response:
```json
[
    {
        "sex": "M|F",
        "age": 12,
    },
    {
        "sex": "M|F",
        "age": 12,
    },
]
```

-----
-----
-----


### Update Neighbor info
> PUT account/

body:
```json
{
    "neighbor_description" : "str"
}
```

response:
```json
{
    "message" : "updated"
}
```

### Get info
> GET auth/users/me

# Diary
### Methods
- Get Diaries
- Create Diary

### Get Diaries
> GET /api/diary

Response:
```json
[
    {
        "_id": "60464640fc3c9a169d9ce85e",
        "records": [
            {
                "_id": "6046466dfc3c9a169d9ce85f",
                "text": "text32\n\n\n\n\nPies eat) \n\nene eeet elton \neae) « \nNotifications € ",
                "attatched_file": "/media/records/Screenshot_from_2021-02-12_12-05-48_IIQMxYf.png",
                "file_type": "i"
            }
        ],
        "title": "user1 tit123le",
        "created": "datetime"
    }
]
```

### Create Diary
> POST /api/diary/
body
```json
{
    "title": "title"
}
```

-----
-----
-----

# Record
### Methods
- RUD
- Append Record

### RUD
> GET|PUT|DELETE /api/record/<record_id>/

`GET` Response:
```json
{
    "_id": "6046466dfc3c9a169d9ce85f",
    "text": "text32\n\n\n\n\nPies eat) \n\nene eeet elton \neae) « \nNotifications € ",
    "attatched_file": "/media/records/Screenshot_from_2021-02-12_12-05-48_IIQMxYf.png",
    "file_type": "i"
}
```

`PUT` Body:
```json
{
    "text": "lolllllll"
}
```
`PUT` Response:
```json
{
    "_id": "6046466dfc3c9a169d9ce85f",
    "text": "lolllllll",
    "attatched_file": "/media/records/Screenshot_from_2021-02-12_12-05-48_IIQMxYf.png",
    "file_type": "i"
}
```
`DELETE` Response:
```json
{
    "_id": null,
    "text": "",
    "attatched_file": null,
    "file_type": null
}
```
### Append Record
> POST /api/record/?diary_id=<diary_id>

`use FormData insted Body, to provide images`

FormData:
| Key | Value | Description |
| --- | ----- | ----------- |
| text | text32 | text in record |
| file_type | `i` or `s` | i - image, s - sound |
| attatched_file | `File` | Image or Soundtrack |

-----
-----
-----


# TitleRecord
### Methods
- Get title records

> GET /api/title_record

Response:
```json
[
    {
        "_id": "6046495bfc3c9a169d9ce861",
        "text": "some title record",
        "attatched_file": "/media/title_records/Imagine_Dragons_-_Fade.mp3",
        "duration": 182
    }
]
```


-----
-----
-----

# Psycologist
### Authenication
> set request header `Authorization-Psy` = token

### Login
> POST /api/psycologists/authentication/signin

Body:
```json
{
    "username": "uname32",
    "password": "pwd"
}
```


### Get Patients

> GET /api/psycologists/patients/<id>

### Append Patient

> POST /api/psycologists/patients/<id>

body:
```json
{
    "patient_id": "<ID>"
}
```



### Register


> POST api/psycologists/authentication/signup
>> U can also create a psychologist with with endpoint

Body:
```json
{
    "username": "uname32",
    "password": "pwd",
    "name": "name"
}
```

### Get Diaries(Transfers)
> GET api/psycologists/transfers/
> will return all transfer groups for psycologist


### Append Diary(Transfer)
> PUT api/psycologists/transfers/
> will updated transfer group

body:
```json
{
    "group": [
        {
            "tid": "<transferId>",
            "fb" : "transfer feedback"
        },
        {
            "tid": "<transferId>",
            "fb" : "transfer feedback"
        },
    ],
    "feedback": "transfer group feedback",
    "status": "a|d"
}
```

Status:
| Key | Desc |
| --- | ---- |
| a | Answered |
| d | Dismissed | 


## Update Psycologist Info

> PUT api/psycologists/manage/<str:id>

body:
```json
{
    "delay_duration": 0,
    "verified": true,
}
```


-----
-----
-----

# Questions

> GET /api/question/<mood>

| Indicator | Mood |
| --------- | ---- |
| 1 | Sad |
| 2 | Bad |
| 3 | It's okay |
| 4 | Good |
| 5 | Happy |

Response:
```json
[
    {
        "_id": "60464aa1fc3c9a169d9ce863",
        "content": "asdasdasdasd",
        "mood": "1"
    }
]
```

[Postman collection link](https://www.getpostman.com/collections/7f5a9d73a871df1bf15c)

