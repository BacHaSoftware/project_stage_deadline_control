from fsspec.registry import default

from odoo import models, fields


class BHSProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    is_show_deadline = fields.Boolean(string='Show Deadline', default=True)

class BHSProjectTask(models.Model):
    _inherit = 'project.task'

    is_show_deadline = fields.Boolean(string='Show Deadline', related='stage_id.is_show_deadline', default=True)
