from django.test import TestCase
from blog.forms import CommentForm

# TestCase is Django's testing library 
# CommentForm is the first form we created in blog/forms.py. The path should reflect the folder structure


# class TestCommentForm(TestCase):

#     def test_form_is_valid(self):
#         comment_form = CommentForm({'body': 'Great Post'})
#         self.assertTrue(comment_form.is_valid(), msg='Form is not valid')

class TestCommentForm(TestCase):
# both tests check the same thing, asserting either True or False

    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid(), msg='Form is not valid')

    def test_form_is_invalid(self):
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")