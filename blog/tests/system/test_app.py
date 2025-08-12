from unittest import TestCase
from unittest.mock import patch
import blog.app
from blog.blog import Blog


class TestApp(TestCase):
    def test_print_blogs(self):
        b = Blog('Test', 'Test Author')
        blog.app.blogs = {'Test': b}

        with patch('builtins.print') as mocked_print:
            blog.app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')
