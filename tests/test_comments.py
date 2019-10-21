import unittest
from app.models import Pitch, User, Comments
from app import db

class CommentsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.user_Tuma = User(username = 'Tuma',password = 'potato', email = 'tumaa@gmail.com')
        self.new_pitch = Pitch(id=12,pitch_content='strive and you will win',pitch_category="interview pitch",user = self.user_Tuma)
        self.new_comment = Comments(id=15, comment='good work', user = self.user_Tuma)
    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id,15)
        self.assertEquals(self.new_comment.comment,'good work')
        self.assertEquals(self.new_comment.user,self.user_Tuma)
    

