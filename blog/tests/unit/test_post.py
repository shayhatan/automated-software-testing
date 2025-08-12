from unittest import TestCase
from blog.post import Post


class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test', 'Test Content')
        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)

    def test_json(self):
        p = Post('Test', 'Test Content')
        expected = {'title': 'Test', 'content': 'Test Content'}

        # can not use assertEqual because it will check dict obj is exactly the same, but they may be diff
        self.assertDictEqual(expected, p.json())

