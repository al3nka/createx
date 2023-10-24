from django.http import Http404


class OwnerAccessMixin:
    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        if self.request.user == object.owner:
            return object
        raise Http404()
