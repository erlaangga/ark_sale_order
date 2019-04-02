{
    'name': 'Ark - Sale Order',
    'author': 'Arkana',
    'version': '0.1',
    'depends': [
        'sale_management',
    ],
    'data': [
        'views/invoice_view.xml'
        'views/partner_view.xml',
        'views/sale_view.xml',
    ],
    'qweb': [
        # 'print/nama_template.xml',
    ],
    'sequence': 2,
    'auto_install': False,
    'installable': True,
    'application': True,
    'category': 'Academy Day 3',
    'summary': 'Sale Order versi Arkana',
    'license': 'OPL-1',
    'website': 'https://www.arkana.co.id/',
    'description': """
'Nama Business App / Module'
=============

Modul ini digunakan untuk : 

1. ...

2. ... 

# Deskripsi ini hanya akan terlihat jika application = False

""",

}
