# API
- [User](#-user)
- [Diary](#-diary)
- [Record](#-record)
- [TitleRecord](#-titlerecord)
- [Psycologist(Psychologist)](#-psycologist)
- [Questions](#-questions)


# User
### Methods
- Create User (Sign Up)
- Login

### Create User (SignUp)
> POST /auth/users/

Body:
```json
{
    "name": "name",
    "username": "uname",
    "password": "pwd",
    "age": 1,
    "children": [
        {
            "sex": "male|female",
            "age": 12,
        },
        {
            "sex": "male|female",
            "age": 12,
        },
    ]
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

-----
-----
-----

# Diary
### Methods
- Get Diaries
- Create Diary
- Append Record

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
        "title": "user1 tit123le"
    }
]
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

### Register
> POST api/psycologists/authentication/signup

Body:
```json
{
    "username": "uname32",
    "password": "pwd",
    "name": "name"
}
```

 - Get diaries
 - Get patients
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
