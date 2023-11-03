# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Student(models.Model):
    _name = 'st.profile'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # _rec_name = 'name'

    name = fields.Char(string="Name", tracking=True)
    st_code = fields.Char(string="Student Code", required=True, copy=False, readonly=True, index=True,
                          default=lambda self: _('New'))
    image = fields.Binary("Photo")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    dob = fields.Date(string="Birthdate")
    city = fields.Char(string="City")
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female')])
    result_id = fields.One2many('st.result', inverse_name='student_id', string='Result')
    total = fields.Integer(compute="_value_pc", store=True)
    total_subjects = fields.Integer(compute="value_pc", store=True)
    average = fields.Float(compute="_value_avg", store=True)
    kan_color = fields.Integer('Color', compute="change_color_on_kanban", store=True)
    manager_id = fields.Many2one("res.users", string="manager")
    pay = fields.Boolean(string='Payment', default=False, tracking=True, compute="_compute_pay", readonly=True)
    notes = fields.Html(string="Notes")
    currency_id = fields.Many2one('res.currency', string='currency', readonly=True)
    fees = fields.Float(strnig='Fees', tracking=True)
    state = fields.Selection([
        ('A class', 'A class'),
        ('B class', 'B class'),
        ('C class', 'C class'),
        ('None', 'None')], default='None', string='status', required=True)

    # def payments_wizard(self):
    #     action = self.env.ref('alaa.student_wizard_action').read()[0]
    #     return action

    def _compute_pay(self):
        for rec in self:
            if (rec.fees == 1500):
                rec.pay = True
            else:
                rec.pay = False



    def a_class(self):
        for rec in self:
            rec.state = 'A class'

    def b_class(self):
        for rec in self:
            rec.state = 'B class'

    def c_class(self):
        for rec in self:
            rec.state = 'C class'

    # @api.constrains('email')
    # def check_email(self):
    #     for rec in self:
    #         x = self.env['st.profile'].search(['email', '=', rec.email])
    #         if x:
    #             raise ValidationError("email %s already exist" % rec.email)

    _sql_constraints = [
        ('unique_em', 'unique (email)', "the email  is already registered please choose another one ")
    ]

    @api.model
    def create(self, record):
        if record.get('st_code', _('New')) == _('New'):
            record['st_code'] = self.env['ir.sequence'].next_by_code('student.sequence') or _('New')
        return super(Student, self).create(record)


    @api.depends('total')
    def _value_avg(self):
        for record in self:
            if (record.total_subjects != 0):
                record.average = ((record.total) / record.total_subjects)

    @api.depends('result_id', 'result_id.subject_score')
    def _value_pc(self):
        for rec in self:
            print('>>>>>>>>>>>>>>', rec)
            s = 0
            sc = 0
            for x in rec.result_id:
                print('<<<<<<<<<<<<<< ', x)
                s += x.subject_score
                sc += 1
            rec.total = s
            rec.total_subjects = sc



    def action_whatsapp(self):
        if not self.phone:
            raise ValidationError(_("Missing phone number ......."))
        msg = 'Hi %s Current payments are %s ' % (self.name, self.fees)
        whatsapp_api = 'https://api.whatsapp.com/send?phone=%s&text=%s' % (self.phone, msg)
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': whatsapp_api
        }

    @api.depends('average')
    def change_color_on_kanban(self):
        '''
            6 = red(9 غامق)
            3 = yellow
            4= blue
            5 = green/خمري
            7 = ازرق غامق
            10=green
        '''
        for record in self:
            color = 1
            if record.average >= 85.00:
                color = 10
            elif 84 >= record.average >= 60:
                color = 7
            else:
                color = 9
            record.kan_color = color


class Subjects(models.Model):
    _name = 'st.subjects'
    _rec_name = 'subjects_name'
    # _rec_name =' subjects_name'
    subjects_name = fields.Char(string='subjects')


class Result(models.Model):
    _name = "st.result"
    subject_score = fields.Integer(string='Marks')
    subject_ids = fields.Many2one('st.subjects', ondelete="cascade", string='Subjects')
    student_id = fields.Many2one('st.profile', ondelete="cascade", string='Student')
