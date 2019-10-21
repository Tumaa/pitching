import unittest
from app.models import Pitch, User
from app import db

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.user_Tuma = User(username = 'Tuma',password = 'potato', email = 'tumaa@gmail.com')
        self.new_pitch = Pitch(id=12,pitch_content='strive and you will win',pitch_category="interview pitch",user = self.user_Tuma)
    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.id,12)
        self.assertEquals(self.new_pitch.pitch_content,'strive and you will win')
        self.assertEquals(self.new_pitch.pitch_category,"interview pitch")
        self.assertEquals(self.new_pitch.user,self.user_Tuma)
    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        got_pitch = Pitch.get_pitch(12)
        self.assertTrue(got_pitch is not None)
