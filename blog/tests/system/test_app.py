from unittest import TestCase
from unittest.mock import patch
import blog.app
from blog.blog import Blog
from blog.post import Post


class TestApp(TestCase):
    def test_menu_prints_prompt(self):
        with patch('builtins.input') as mocked_input:
            blog.app.menu()
            mocked_input.assert_called_with(blog.app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('blog.app.print_blogs') as mocked_print_blogs:
            # to pass prog for waiting input
            with patch('builtins.input', return_value='q'):
                blog.app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        b = Blog('Test', 'Test Author')
        blog.app.blogs = {'Test': b}

        with patch('builtins.print') as mocked_print:
            blog.app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            # passing value by order to the input
            mocked_input.side_effect = ('Test', 'Test Author')
            blog.app.ask_create_blog()
            self.assertIsNotNone(blog.app.blogs.get('Test'))

    def test_ask_read_blog(self):
        b = Blog('Test', 'Test Author')
        blog.app.blogs = {'Test': b}
        with patch('builtins.input', return_value='Test'):
            with patch('blog.app.print_posts') as mocked_print_posts:
                blog.app.ask_read_blog()
                mocked_print_posts.assert_called_with(b)

    def test_print_posts(self):
        b = Blog('Test', 'Test Author')
        blog.app.blogs = {'Test': b}
        b.create_post('Test Post', 'Test Content')

        with patch('blog.app.print_post') as mocked_print_post:
            blog.app.print_posts(b)

            mocked_print_post.assert_called_with(b.posts[0])

    def test_print_post(self):
        post = Post('Post Title', 'Post Content')
        expected_print = '''
--- Post Title ---

Post Content

'''
        with patch('builtins.print') as mocked_print:
            blog.app.print_post(post)
            mocked_print.assert_called_with(expected_print)
