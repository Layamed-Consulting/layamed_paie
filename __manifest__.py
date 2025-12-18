{
    'name': "Layamed Consulting - Paie",
    'description': "Layamed Consulting Paie",
    'summary': "",
    'author': 'Anass Hajjouj',
    'category': 'base',
    'version': '1.0',
    'description': """
        This module introduces custom features for ChicCorner
    """,
    'author': 'Anass Hajjouj',
    'website': 'http://www.layamedconsulting.com.com',
    'category': '',
    'depends': ['base','hr_payroll'],
    'data': [
        'views/payroll_order_payment.xml',
        'report/bulettin_de_paie.xml',
        'report/bulletin_report.xml',
        'report/bulletin_template.xml',
        'report/payroll_order_virement.xml',
        'report/payroll_report.xml',
        'report/payroll_template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
