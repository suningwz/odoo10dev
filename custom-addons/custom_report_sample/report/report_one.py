# _*_ coding: utf-8 _*_
from odoo import models, fields, api


class ReportOne(models.AbstractModel):
    _name = "report.custom_report_sample.report_one"

    @api.multi
    def render_html(self, data=None):
        report = self.env['report']
        content = data.get("content", None)

        docargs = {
            "content": content
        }
        return report.render('custom_report_sample.report_one_template', docargs)
