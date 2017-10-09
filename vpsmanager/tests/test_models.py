from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.utils.html import escape

from vps.models import VPS

class VPSInventoryTest(TestCase):
    def test_list_vps(self):
        vps = VPS()
        assert vps.get_vps_list()

