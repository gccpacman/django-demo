import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Question




class QuestionMethodTest(TestCase):
    
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for question 
        whose pub_date is in future
        """
        
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        
        self.assertEqual(future_question.was_published_recently(), False)
        #self.assertFalse(future_question.was_published_recently())
    
    def test_was_published_recently_with_now_question(self):
        time = timezone.now()
        now_question = Question(pub_date=time)
    
        self.assertTrue(now_question.was_published_recently())        
    
        
    def test_was_published_recently_with_day2ago_question(self):
        time = timezone.now() - datetime.timedelta(days=2)
        day2ago_question = Question(pub_date=time)
    
        self.assertFalse(day2ago_question.was_published_recently())    