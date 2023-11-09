import json
import pytest
import requests
from requests import Response

@pytest.mark.order(1) # allows creating a User
def test_create_user():
    url = "https://petstore.swagger.io/v2/user"
    body = ({
        "username": "AnnaA",
        "firstName": "Anna",
        "lastName": "Abc",
        "email": "Annaabc@gmail.com",
        "password": "Pass111",
        "phone": "0111111",
        "userStatus": "0"
    })
    headers = {
        'Content-Type': 'application/json'
       }
    response = requests.post(url, headers=headers, data=json.dumps(body))
       
    assert response.status_code ==200, f'Expected status code ok, got {response.text}'


@pytest.mark.order(2) # allows login a User
def test__allows_login():
    headers = {
        'Accept': 'application/json'
        }
    url = "https://petstore.swagger.io/v2/user/login?username=test&password=test"
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    print(response.text)


@pytest.mark.order(3) # allows creating the list of Users
def test_create_user_list():
    url = "https://petstore.swagger.io/v2/user/createWithList"
    body = ([{
        "username": "AnnaA",
        "firstName": "Anna",
        "lastName": "Abc",
        "email": "Annaabc@gmail.com",
        "password": "Pass111",
        "phone": "0111111",
        "userStatus": "0"
    }])
    headers = {
        'Content-Type': 'application/json'
       }
    response = requests.post(url, headers=headers, data=json.dumps(body))
       
    assert response.status_code ==200, f'Expected status code ok, got {response.text}'


@pytest.mark.order(4) # allows Log out User
def test_allows_logout():
    headers = {
       'Accept': 'application/json'
        }
    url = "https://petstore.swagger.io/v2/user/logout"
    response = requests.get(url, headers=headers)

    assert response.status_code == 200


@pytest.mark.order(5) #allows adding a new Pet
def test_add_pet():
       url = "https://petstore.swagger.io/v2/pet"
       body = ({
        "category": {
        "id": "1",
        "name": "Pet"
        },
        "name": "Pet",
        "photoUrls": [
        "photo"
        ],
        "tags": [
        {
        "id": "1",
        "name": "Pet"
        }
        ],
        "status": "available"
        })
       headers = {
        'Content-Type': 'application/json'
       }
       response = requests.post(url, headers=headers, data=json.dumps(body))
       
       assert response.status_code ==200, f'Expected status code ok, got {response.text}'


@pytest.mark.order(6) # allows updating Pet’s image
def test_update_image_pet():
    url = "https://petstore.swagger.io/v2/pet" 
    body = ({
        "name": "Pet",
        "photoUrls": [
        "newphoto"
        ],
        })
    headers = {
        'Content-Type': 'application/json'
        }

    response = requests.put(url, headers=headers, data=json.dumps(body))

    assert response.status_code ==200, f'Expected status code ok, got {response.text}'


@pytest.mark.order(7) # allows updating Pet’s name and status
def test_update_name_status_pet():
    url = "https://petstore.swagger.io/v2/pet" 
    body = ({
        "category": {
        "name": "Pet1"
        },
        "tags": [
        {
        "name": "Pet1"
        }
        ],
        "status": "available1"
        })
    headers = {
        'Content-Type': 'application/json'
        }

    response = requests.put(url, headers=headers, data=json.dumps(body))

    assert response.status_code ==200, f'Expected status code ok, got {response.text}'


@pytest.mark.order(8) # allows deleting Pet 
def test_delete_pet():
    url = "https://petstore.swagger.io/v2/pet"
    body = ({
        "category": {
        "id": "1",
        "name": "Pet"
        },
        "name": "Pet",
        "photoUrls": [
        "photo"
        ],
        "tags": [
        {
        "id": "1",
        "name": "Pet"
        }
        ],
        "status": "available"
        })
    headers = {
        'Content-Type': 'application/json'
       }
    response = requests.post(url, headers=headers, data=json.dumps(body))
    response_id = response.json()["id"]
    print(response_id)
       
    assert response.status_code ==200, f'Expected status code ok, got {response.text}'

    
    url = f"https://petstore.swagger.io/v2/pet/{response_id}" 
      
    body = ""
    headers = {}

    response = requests.delete(url, data=body, headers=headers)

    assert response.status_code ==200, f'Expected status code ok, got {response.text}'





   


