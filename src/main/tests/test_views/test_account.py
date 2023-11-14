import pytest
from django.urls import reverse

from main.models import user_model


@pytest.fixture
@pytest.mark.django_db
def user() -> user_model:
    username = "testuser"
    password = "testpassword"
    return user_model.objects.create_user(
        username=username,
        password=password,
    )


def test_login_view_available(client):
    response = client.get(reverse('login'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_logout_view_available(client, user):
    client.force_login(user)
    response = client.get(reverse('logout'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_profile_view_available(client, user):
    client.force_login(user)
    response = client.get(reverse('profile', kwargs={'pk': user.pk}))
    assert response.status_code == 200
    assert user.username in response.rendered_content
