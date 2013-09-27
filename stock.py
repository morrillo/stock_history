# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv
from datetime import datetime
import pdb
import logging

_logger = logging.getLogger(__name__)


class stock_product_history(osv.osv):
    _name = 'stock.product.history'
    _description = 'Historic record of stock'
    _columns = {
        'product_id' : fields.many2one('product.product', 'Products', ondelete='cascade', select=1, required=True),
        'location_id' : fields.many2one('stock.location', 'Location', ondelete='cascade', select=1, required=True),
        'date_stock': fields.datetime('Stock Date/Time'),
	'quantity': fields.float('Quantity')
    }

    def _update_daily_stock(self,cr,uid,ids=None,context=None):

	cr.execute("select * from stock_report_prodlots")

	now = datetime.today()
        for row in cr.dictfetchall():

		vals_stock = {
			'product_id': row['product_id'],
			'location_id': row['location_id'],
			'date_stock': now,
			'quantity': row['qty']
			}
		#import pdb;pdb.set_trace()
		stock_product_history_id = self.pool.get('stock.product.history').create(cr,uid,vals_stock)

      	_logger.debug("Updated product history " + str(now))
	#import pdb;pdb.set_trace()

stock_product_history()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
