from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post


# Create your tests here.
class ThoughtShareTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Post 1', context='Post example 1', created_at='29-05-2024', author='Thinker')

    def test_post_has_title(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'Post 1')

    def test_post_has_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.context, 'Post example 1')


    def test_post_has_author(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.author, 'Thinker')


class ThoughtShareTests2(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='thinker', password='testpass')
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpass')
        self.post = Post.objects.create(title="Post 1", context="Test context", author="thinker")

    def test_list_view(self):
        self.client.login(username='thinker', password='testpass')
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ThoughtShare/post_page.html')
        self.assertContains(response, self.post.title)

    def test_add_post_view_get(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('add_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ThoughtShare/add_post.html')

    def test_delete_post_view_get(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('delete_post', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ThoughtShare/delete_post.html')

    def test_edit_post_view_get(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('edit_post', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ThoughtShare/edit_post.html')