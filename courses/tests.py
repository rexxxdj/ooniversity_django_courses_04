# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from courses.models import Course, Lesson
from coaches.models import Coach


def course_create(ccount=1):
	for i in xrange(ccount):	
		course = Course.objects.create(
				name = 'Course {}'.format(i+1),
				short_description = 'Description {}'.format(i+1),
				)
	return course


class CoursesListTest(TestCase):
	'''
	Test index page
	'''

	def test_course_list(self):		
		client = Client()
		response = client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_new_course_count(self):
		course_create(10)	
		self.assertEqual(Course.objects.all().count(), 10)

	def test_link_add_course(self):
		response = self.client.get('/')
		self.assertContains(response, '/courses/add/')	

	def test_link_edit_all_course(self):
		course_create(5)
		response = self.client.get('/')	
		for i in range(1, 5):
			self.assertContains(response, '/courses/edit/{}/'.format(i))

	def test_link_delete_all_course(self):
		course_create(5)
		response = self.client.get('/')	
		for i in range(1, 5):
			self.assertContains(response, '/courses/remove/{}/'.format(i))			


class CoursesDetailTest(TestCase):
    '''
    Test for view course detail page
    '''

    def test_course_view(self):
    	course = course_create()
        client = Client()
        response = client.get(reverse('courses:detail', 
        								args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_lesson_theme(self):
        course = course_create()
        for i in xrange(10):
            newlesson = Lesson.objects.create(
                subject=u'Theme {}'.format(i+1),
                description='Test description {}'.format(i+1),
                course=course,
                order=i+1,)

        client = Client()
        response = client.get(reverse('courses:detail',
            args=(1,)))
        self.assertContains(response, newlesson.subject)

    def test_course_lesson_order(self):
        '''
        Test for exists lesson_name on course page
        '''
        course = course_create()
        for i in xrange(10):
            newlesson = Lesson.objects.create(
                subject=u'Theme {}'.format(i+1),
                description='Test description {}'.format(i+1),
                course=course,
                order=i+1,)

        client = Client()
        response = client.get(reverse('courses:detail', 
                                        args=(1,)))
        self.assertContains(response, newlesson.order)

    def test_course_lesson_description(self):
        course = course_create()
        for i in xrange(10):
            newlesson = Lesson.objects.create(
                subject=u'Theme {}'.format(i+1),
                description='Test description {}'.format(i+1),
                course=course,
                order=i+1,)

        client = Client()
        response = client.get(reverse('courses:detail', 
                                        args=(1,)))
        self.assertContains(response, newlesson.description)

    def test_course_name(self):
		course = course_create()
		client = Client()
		response = client.get(reverse('courses:detail', 
										args=(1,)))
		self.assertContains(response, course.name)

