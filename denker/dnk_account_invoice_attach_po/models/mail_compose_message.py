from odoo import models, fields, api


class MailComposeMessage(models.TransientModel):
    _inherit = 'mail.compose.message'

    @api.multi
    @api.onchange('template_id')
    def onchange_template_id_wrapper(self):
        self.ensure_one()
        values = self.onchange_template_id(self.template_id.id, self.composition_mode, self.model, self.res_id)['value']
        #print "ESTA ES LA FUNCION QUE VOY A MODIFICAR, PARA TODOS; LA VOY A REESCRIBIR :("
        print self.model
        if self.model == 'account.invoice' and self.res_id:
            attachs = values.get('attachment_ids')[0][2]
            #print attachs
            Attachment = self.env['ir.attachment']
            Account = self.env['account.invoice']
            ir_account = Account.search([('id','=',self.res_id)]) #Me traigo la factura para acceder al nombre del archivo
            if ir_account:
                #Busco el adjunto en la tabla de adjuntos por el nombre del archivo adjunto y que sea de la factura
                ir_attachment_po = Attachment.search([('res_id','=',self.res_id),('name','=',ir_account.filename)], limit=1, order="id desc")
                #Si encontre factura y tengo como true el valor de adjuntar PO en el cliente,  entonces lo hago
                if ir_attachment_po and ir_account.partner_id.attach_purchase_order_to_invoice_mail:
                    #si encuentro algo, se lo agrego y hago el update de values
                    attachs.append(ir_attachment_po.id)
                    values.update({'attachment_ids' : [(6, 0, attachs)]})
        for fname, value in values.iteritems():
                # print fname
                # print value
            setattr(self, fname, value)
