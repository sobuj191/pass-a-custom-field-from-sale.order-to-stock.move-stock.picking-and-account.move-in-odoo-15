{
    'name': 'Learning',
    'version': '1.0.0',
    'sequence': -100,
    'category': 'Sales/Sales',
    'summary': 'Sales internal machinery',
    'description': """
This module contains all the common features of Sales Management and eCommerce.
    """,
    'depends': ['base','sale'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order.xml',
        'views/stock_picking.xml',
        'views/account_move.xml',
        # # 'views/account_move_line.xml',
        'views/stock_move.xml',
        # 'views/stock_move_line.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
