from django.test import TestCase
from .models import Post
from django.urls import reverse


class PostContentTest(TestCase):
    def setUp(self):
        post = Post.objects.create(text="Just a test")

    def test_text_content(self):
        post = Post.objects.get(id=1)    
        excepted_object_name = f"{post.text}"
        self.assertEqual(excepted_object_name, "Just a test")


class HomePageViewTest(TestCase):
    def setUp(self):
        post = Post.objects.create(text="Another one")

    def test_view_url_exist_on_location(self):
        response = self.client.get("/posts")
        self.assertEqual(response.status_code, 200)


    def test_view_url_by_name(self):
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)


    def test_view_template(self):
        post = Post.objects.get(id=2)
        excepted_object_name = f"{post.text}"
        self.assertEqual(excepted_object_name, "Another one")
        self.assertTemplateUsed("posts.html")
