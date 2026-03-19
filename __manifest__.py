# -*- coding: utf-8 -*-
{
    'name': 'Code Silae pour Contacts',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Ajoute le champ Code Silae sur les contacts',
    'description': """
        Ce module ajoute un champ "Code Silae" sur le modèle Contacts (res.partner).
        Fonctionnalités incluses :
        - Champ avec contrainte d'unicité.
        - Ajout dans les vues Formulaire, Liste et Kanban.
        - Filtre de recherche.
        - Droits d'accès spécifiques pour verrouiller l'édition du code Silae aux employés ciblés.
    """,
    'author': 'Geoffrey',
    'depends': ['base', 'contacts'],
    'data': [
        'security/partner_silae_security.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
