from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='admin@sky.ru', password='qwerty')
        self.course = Course.objects.create(name='Biology', owner=self.user)
        self.lesson = Lesson.objects.create(name='Fauna', url_video='http://video.youtube.com', owner=self.user,
                                            course=self.course)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('materials:lesson_retrieve', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'),
            self.lesson.name
        )

    def test_lesson_list(self):
        url = reverse('materials:lesson_list')
        response = self.client.get(url)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    # def test_lesson_create(self):
    #     url = reverse('materials:lesson_create')
    #     data = {
    #         "name": "Flora"
    #     }
    #     response = self.client.post(url, data)
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_201_CREATED
    #     )

    # def test_lesson_update(self):
    #     url = reverse('materials:lesson_update', args=(self.lesson.pk,))
    #     data = {
    #         "name": "Flora"
    #     }
    #     response = self.client.patch(url)
    #     data = response.json()
    #     self.assertEqual(
    #         data.get('name'),
    #         "Flora"
    #     )
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_200_OK
    #     )

    def test_lesson_delete(self):
        url = reverse('materials:lesson_delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            Lesson.objects.all().count(),
            0
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
