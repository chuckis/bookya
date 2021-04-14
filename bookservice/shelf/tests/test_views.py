import pytest
from django.core import mail
from django.contrib.auth.models import AnonymousUser
from django.http import Http404
from django.test import RequestFactory
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

import shelf.views as views


class TestBookList:
    def test_anonymous(self):
        req = RequestFactory().get('/shelf')
        resp = views.BookList.as_view()(req)
        assert resp.status_code == 200, 'Should be callable by anyone'

