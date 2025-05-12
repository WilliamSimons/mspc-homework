from diary import Diary
from personality import Personality
from promps import master_prompt

class Client:

    def __init__(self):
        """initializes a new client consisting of a personality and a diary"""
        self.diary = Diary
        self.personality = Personality
    
    def get_personality(self):
        """returns the personality dictionaty"""
        return self.personality
    
    def get_diary(self):
        """returns the diary dictionary"""
        if self.diary.length >= 7:

    

