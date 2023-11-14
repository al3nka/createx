from django.urls import reverse


def test_landing_view_available(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200
