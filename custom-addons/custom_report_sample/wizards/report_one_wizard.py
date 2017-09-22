# _*_ coding: utf-8 _*_
from odoo import models, fields, api


class ReportOneWizard(models.TransientModel):
    _name = "custom_report_sample.report_one_wizard"

    content = fields.Char()

    @api.multi
    def action_print(self):
        self.ensure_one()

        data = dict()
        data["content"] = self.content

        return self.env['report'].get_action(self, 'custom_report_sample.report_one', data=data)
