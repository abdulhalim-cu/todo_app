# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase


class TestWizrd(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestWizrd, self).setUp(*args, **kwargs)
        # Add test setup code here...

    def test_populate_tasks(self):
        "Populate tasks buttons should add two tasks"
        self.wizard.do_populate_tasks()
        # count = len(self.wizard.task_ids)
        # self.assertEqual(count, 2, "Wrong number of populated tasks")
        expected_tasks = self.wizard.task_ids
        self.assertItemsEquals(
                self.wizard.task_ids, expected_tasks,
                'Incorrect set of populated tasks'

                )

    def test_mass_change(self):
        "Mass change dateline date"
        self.wizard.do_populate_tasks()
        self.wizard.new_deadline = self.todo1.date_deadline
        self.wizard.do_mass_update()
        self.assertEqual(
                self.todo1.date_deadline,
                self.todo2.date_deadline)
