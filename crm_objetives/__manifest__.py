{
    'name': "crm objetives",
    'summary': """
        Seguimiento de objetivos anual y mensual.
        Implantación de actividades.
        Cuadros de dirección.
        Compartición de info con clientes.
        Integración ERP actual.
        """,
    'author': "Pedro Guirao",
    'license': 'AGPL-3',
    'website': "https://ingenieriacloud.com",
    'category': 'Tools',
    'version': '12.0.1.0.0',
    'depends': [
        'sale_management',
        'website_sale',
        'contacts',
    ],
    'data': [
        'views/shop_inh_product_view.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'application': True,
}
