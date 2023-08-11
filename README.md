# FastAPI JWT authentication.

### 1. Instal requirements

```bash
pip3 install -r requirements.txt
```

### 2. Run project

```bash
uvicorn run:app --reload
```

### Register user

Go to ``` http://127.0.0.1:8000/auth/register/```

Send next json parameters:

* username
* name
* surname
* age
* password

Response: 

```json
{
  'access_token': 'your_access_JWT', 
  'refresh_token': 'your_refresh_JWT'
}

```

### Login user

Go to ``` http://127.0.0.1:8000/auth/login/```

Send next json parameters:

* username
* password

Response: 

```json
{
  'access_token': 'your_access_JWT', 
  'refresh_token': 'your_refresh_JWT'
}

```

### Make new access token

Go to ``` http://127.0.0.1:8000/auth/jwt/refresh/```

Send next HEADER parameters:

* Authorization: Bearer <your_refresh_token>

Response: 

```json
{
  'access_token': 'your_access_JWT', 
  'refresh_token': 'your_refresh_JWT'
}

```

### Get user info

Go to ``` http://127.0.0.1:8000/user/me/```

Send next HEADER parameters:

* Authorization: Bearer <your_refresh_token>

Response: 

```json
{
  'age': 18, 
  'id': 1, 
  'name': 'name', 
  'surname': 'surname', 
  'username': 'username'
}
```

