import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Question


# Create your tests here.
def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionMethodTest(TestCase):
    
    def test_index_view_with_no_question(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        
    def test_index_view_with_a_past_question(self):    
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question.>'])
        
    def test_index_view_with_a_future_question(self):
        create_question(question_text='Future Quesion', days=30)
        response = self.client.get(reverse('polls:index'))
        #self.assertQuerysetEqual(response.context['latest_question_list'], [''])
        self.assertContains(response, "No polls are available", status_code=200)
    
    def test_index_view_with_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        should be displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_index_view_with_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )        
    
    ####    
    
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