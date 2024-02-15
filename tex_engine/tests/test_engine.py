import pytest
import requests

from main import app


@pytest.fixture()
def client():
    return app.test_client()


@pytest.fixture()
def tex_template():
    return "\\documentclass{article}\n\\begin{document}\nHello, {{ name }}!\n\\end{document}"

@pytest.fixture()
def template_variables():
    return {"name": "Aliona"}


def test_valid_request(client, tex_template, template_variables):
    request_json = {
        "template": tex_template,
        "variables": template_variables
    }
    response = client.post('/', json=request_json)
    assert response.status_code == 200
    assert response.mimetype == 'application/pdf'


def test_missing_keys(client, tex_template):
    request_json = {
        "template": tex_template,
    }
    response = client.post('/', json=request_json)
    assert response.status_code == 400
    assert response.json == {'message': 'Expected keys: template, variables', 'status': '400'}


def test_missing_variables(client, tex_template):
    request_json = {
        "template": tex_template,
        "variables": {
            "wrong": "Aliona"
        }
    }
    response = client.post('/', json=request_json)
    assert response.status_code == 400
    assert response.json == {'message': 'Expected variable keys: name', 'status': '400'}


def test_wrong_template_syntax(client, template_variables):
    request_json = {
        "template": "\\documentclass{article}\n\\begin{document}\nHello, {{ name !\n\\end{document}",
        "variables": template_variables
    }
    response = client.post('/', json=request_json)
    assert response.status_code == 400
    assert response.json == {'message': 'Template has some syntax errors', 'status': '400'}


def test_template_tex_error(client, template_variables):
    request_json = {
        "template": "\\begin{document}\nHello, {{ name }}!\n\\end{document}",
        "variables": template_variables
    }
    response = client.post('/', json=request_json)
    assert response.status_code == 400
    assert response.json == {'message': 'Template has some syntax errors', 'status': '400'}
