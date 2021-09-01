from odoo import api, fields, models, _

class AccountMove(models.Model):
	_inherit = "account.move"

	def action_post(self):
		# ctx = self._context or {}
		# for inv in self:
		# 	if inv.state == 'draft' and inv.move_type in ('out_invoice'):
		# 		return self.with_context(payment_invoice=True).action_register_payment()
		return super(AccountMove, self).action_post()

	# action_register_payment