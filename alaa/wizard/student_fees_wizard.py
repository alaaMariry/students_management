from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class Wizards(models.TransientModel):
    _name = "student.wizard"
    _description = "Wizard: student fees update"

    @api.model
    def default_get(self, fields):
        res = super(Wizards, self).default_get(fields)
        res['student_id'] = self.env.context.get('active_id')
        return res

    student_id = fields.Many2one('st.profile', string='Student', domain=[('pay', '=', False)])
    fees_old = fields.Float(strnig="Old payments", related="student_id.fees", readonly=True)
    fees_new = fields.Float(strnig="new payments")
    date_fees = fields.Date(string="Date", default=fields.Date.today)

    def update_fees(self):
        ids = self._context.get("active_ids")
        if self.fees_new < 0:
            raise ValidationError(_("Error ........."))
        else:
            return self.env['st.profile'].browse(ids).update({'fees': self.fees_old + self.fees_new})
