from unittest import TestCase
from blog.blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test Title', 'Test Author')
        self.assertEqual(b.title, 'Test Title')
        self.assertEqual(b.author, 'Test Author')
        self.assertListEqual(b.posts, [])