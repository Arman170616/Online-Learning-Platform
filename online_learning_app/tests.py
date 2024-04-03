from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Course, Enrollment

class CourseAPITestCase(APITestCase):
    def setUp(self):
        self.course1 = Course.objects.create(title='Course 1', description='Description 1', instructor='Instructor 1', duration=60, price=100.00)
        self.course2 = Course.objects.create(title='Course 2', description='Description 2', instructor='Instructor 2', duration=90, price=150.00)

    def test_get_courses(self):
        url = reverse('course_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_get_course_by_id(self):
        url = reverse('course_detail', args=[self.course1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Course 1')

    def test_create_course(self):
        url = reverse('course_list')
        data = {'title': 'New Course', 'description': 'New Description', 'instructor': 'New Instructor', 'duration': 120, 'price': 200.00}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Course.objects.count(), 3)


