# -*- coding: utf-8 -*-
# © 2015-2018 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Edit attachments",
    "version": "10.0.1.0.0",
    "author": "Therp BV,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Knowledge Management",
    "summary": "Edit attachments after upload",
    "depends": [
        'attachment_action',
    ],
    "data": [
        "views/ir_attachment.xml",
        'views/templates.xml',
    ],
    "qweb": [
        'static/src/xml/attachment_edit.xml',
    ],
}
