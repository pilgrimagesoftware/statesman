__author__ = "Paul Schifferer <paul@schifferers.net>"
"""
adj.py
- Synonym for 'adjust'
"""


from flask import current_app
from statesman_api.controllers.actions import adjust


def execute(org_id:str, user_id:str, args:list) -> list:
    current_app.logger.debug("org_id: %s, user_id: %s, args: %s", org_id, user_id, args)

    return adjust.execute(org_id, user_id, args)
