# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase


class TestWizrd(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestWizrd, self).setUp(*args, **kwargs)
        # Add test setup code here...

    def test_populate_tasks(self):
        "Populate tasks buttons should add two tasks"
        # Add test code
