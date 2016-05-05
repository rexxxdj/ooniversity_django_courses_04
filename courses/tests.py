# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from courses.models import Course, Lesson
from coaches.models import Coach


class CoursesListTest(TestCase):

	def test_course_list(self):
		'''
		Test index page
		'''
		client = Client()
		response = client.get('/')
		self.assertEqual(response.status_code, 200)


class CoursesDetailTest(TestCase):

    def test_course_view(self):
    	'''
    	Test for view course page
    	'''
    	#Создаю курс
    	course1 = Course.objects.create(
    		name='Python', 
    		short_description='Web development with Python'
    		)
    	coursenum = 1 
       	#Проверка отображения страницы курса
        client = Client()
        response = client.get(reverse('courses:detail', 
        								args=(coursenum,)))
        self.assertEqual(response.status_code, 200)

    def test_lesson_theme(self):
        course1 = Course.objects.create(
            name='Python',
            short_description='Web development with Python',
            description = 'Test description for TestCase'
            )
        coursenum = 1
        #Создаю lessons (10)
        for i in xrange(10):
            newlesson = Lesson.objects.create(
                subject=u'Theme {}'.format(i+1),
                description='Test description {}'.format(i+1),
                course=course1,
                order=i+1,)

        client = Client()
        response = client.get(reverse('courses:detail',
            args=(coursenum,)))
        self.assertContains(response, newlesson.subject)

    def test_course_lesson_order(self):
        '''
        Test for exists lesson_name on course page
        '''
        #Создаю курс
        course1 = Course.objects.create(
            name='Python', 
            short_description='Web development with Python',
            description = 'Test description for TestCase'
            )
        coursenum = 1       
        #Создаю lessons (10)
        for i in xrange(10):
            newlesson = Lesson.objects.create(
                subject=u'Theme {}'.format(i+1),
                description='Test description {}'.format(i+1),
                course=course1,
                order=i+1,)

        client = Client()
        response = client.get(reverse('courses:detail', 
                                        args=(coursenum,)))
        self.assertContains(response, newlesson.order)

    def test_course_lesson_description(self):

        #Создаю курс
        course1 = Course.objects.create(
            name='Python', 
            short_description='Web development with Python',
            description = 'Test description for TestCase'
            )
        coursenum = 1       
        #Создаю lessons (10)
        for i in xrange(10):
            newlesson = Lesson.objects.create(
                subject=u'Theme {}'.format(i+1),
                description='Test description {}'.format(i+1),
                course=course1,
                order=i+1,)

        client = Client()
        response = client.get(reverse('courses:detail', 
                                        args=(coursenum,)))
        self.assertContains(response, newlesson.description)

    def test_course_name(self):
		'''
		Test for exists course_name on page
		'''
		#Создаю курс
		course1 = Course.objects.create(
			name='Python', 
			short_description='Web development with Python'
			)
		coursenum = 1 
		#Проверка отображения страницы курса
		client = Client()
		response = client.get(reverse('courses:detail', 
										args=(coursenum,)))
		#Проверка отображения Имени курса
		self.assertContains(response, course1.name)

