# -*- coding: utf-8 -*-
{
    'name': "Module Sale Custom",
    'summary': "Adecuaciones a ventas e inventarios",
    'description': """
        > Desarrollo en Ventas-Inventario, al crear el picking desde ventas, este tiene que estar reservada la totalidad de cantidad de venta solicitada
        """,
    'author': "Gustavo H.",
    'category': 'Sales/Sales',
    'version': '1.0',
    'depends': ['sale_stock','stock'],
    'qweb': [
    ],
    'data': [
        "views/sale_order_view.xml",
        # "report/report_stockpicking_operations.xml"
    ],
}