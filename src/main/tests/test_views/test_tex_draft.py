import pytest
from django.urls import reverse

from main.models import user_model, TexDraft


@pytest.fixture
@pytest.mark.django_db
def user() -> user_model:
    username = "testuser"
    password = "testpassword"
    return user_model.objects.create_user(
        username=username,
        password=password,
    )


@pytest.fixture
@pytest.mark.django_db
def tex_draft(user) -> TexDraft:
    return TexDraft.objects.create(
        name="Test tex draft",
        is_public=True,
        owner=user
    )


@pytest.mark.django_db
class BaseTestLoginRequired:
    """
    general test class for test_views that require login
    Redefine 'url' to use it for specific view
    """
    @pytest.fixture
    def url(self):
        raise NotImplemented

    @pytest.fixture
    def authorized_client(self, client, user):
        client.force_login(user)
        return client

    def test_unauthorized_access(self, client, url):
        print(url)
        response = client.get(url)
        assert response.status_code == 302

    def test_authorized_access(self, authorized_client, user, url):
        response = authorized_client.get(url)
        assert response.status_code == 200


class TestTexDraftListView(BaseTestLoginRequired):

    @pytest.fixture
    def url(self):
        return reverse('tex_draft_list')

    def test_adding_tex_draft(self, authorized_client, user, tex_draft, url):
        response = authorized_client.get(url)
        assert tex_draft.name in response.rendered_content

    def test_deleting_tex_draft(self, authorized_client, tex_draft, user, url):
        tex_draft_name = tex_draft.name
        tex_draft.delete()
        response = authorized_client.get(url)
        assert tex_draft_name not in response.rendered_content


class TestTexDraftCreateView(BaseTestLoginRequired):

    @pytest.fixture
    def url(self):
        return reverse('tex_draft_create')

    def test_create_tex_draft(self, user, authorized_client, url):
        tex_draft_name = 'test_template'
        data = {'name': tex_draft_name, 'owner': user}

        response = authorized_client.post(url, data)
        assert response.status_code == 302
        assert TexDraft.objects.filter(name=tex_draft_name).exists()

    def test_create_invalid_tex_draft(self, user, authorized_client, url):
        tex_draft_name = 'test_template'
        data = {}

        response = authorized_client.post(url, data)
        assert response.status_code == 200
        assert not TexDraft.objects.filter(name=tex_draft_name).exists()


class TestTexDraftDeleteView(BaseTestLoginRequired):
    @pytest.fixture
    def url(self, tex_draft):
        return reverse('tex_draft_delete', kwargs={'pk': tex_draft.uuid})

    def test_delete_tex_draft(self, authorized_client, tex_draft, url):
        response = authorized_client.post(url)
        assert response.status_code == 302
        print(TexDraft.objects.filter(pk=tex_draft.pk))
        print(url)
        assert not TexDraft.objects.filter(pk=tex_draft.uuid).exists()


class TestTexDraftDetailView(BaseTestLoginRequired):
    @pytest.fixture
    def url(self, tex_draft):
        return reverse('tex_draft_detail', kwargs={'pk': tex_draft.uuid})

    def test_view_displayed_data(self, authorized_client, url, tex_draft):
        response = authorized_client.get(url)
        assert response.status_code == 200
        assert tex_draft.name in response.rendered_content
