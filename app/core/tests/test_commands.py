""""
test custom django management commands

"""

from unittest.mock import patch #for mocking the behaviour to save time in testing

from psycopg2 import OperationalError as Psycopg2Error #possible error if database is not properly setup before connecting to the app


from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.check')  #this decorator is used to mock the behaviour of all the tests

class CommandTests(SimpleTestCase):
    """tests commands"""
    
    def test_wait_for_db_ready(self,patched_check):
        """test waiting for the database if database is ready"""
        patched_check.return_value=True
        
        call_command('wait_for_db')
        
        #check if the check command is called
        patched_check.assert_called_once_with(database=['default'])
        
    
    @patch('time.sleep')
        
    def test_wait_for_db_delay(self,patched_sleep,patched_check):
        """test waiting for the database when getting operational error"""
        patched_check.side_effect=[Psycopg2Error]*2 + [OperationalError]*3 + [True]
        
        #call the Command
        call_command('wait_for_db')
        
        self.assertEqual(patched_check.call_count,6) #it should be called exactly 6 times
        
        patched_check.assert_called_with(database=['default'])