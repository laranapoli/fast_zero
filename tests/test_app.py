from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_hello_world(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World'}


def test_create_users(client):
    response = client.post(  # Teste do UserSchema (request)
        '/users/',
        json={
            'username': 'xpto',
            'email': 'xpto@gmail.com',
            'password': '123456',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {  # Teste do UserPublic
        'username': 'xpto',
        'email': 'xpto@gmail.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'xpto',
                'email': 'xpto@gmail.com',
                'id': 1,
            }
    ]}


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'xpto2',
            'email': 'xpto@gmail.com',
            'password': 'aaaa',
        }
    )
    assert response.status_code == HTTPStatus.OK


def test_update_user_not_found(client):
    response = client.put(
        '/users/1000',
        json={
            'username': 'xpto2',
            'email': 'xpto@gmail.com',
            'password': 'aaaa',
        }
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted!'}


def test_delete_user_not_found(client):
    response = client.delete('/users/1000')

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_read_user_id(client):
    response = client.get('users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'xpto2',
        'email': 'xpto@gmail.com',
        'password': 'aaaa',
    }


def test_read_user_id_not_found(client):
    response = client.get('users/1000')

    assert response.status_code == HTTPStatus.NOT_FOUND
