"""
Django command for waiting for the database to be availabe for connnection
"""

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    
    def handle(self,*args,**options):
        pass