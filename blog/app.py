blogs = dict() # blog_name: Blog obj

def menu():
    # Show the user the available blogs
    # Let the user make a choice
    print_blogs()

def print_blogs():
    # Print the available blogs
    print("Blogs!")
    for key, blog in blogs.items(): # [(blog_name, Blog), ... (blog_name_n, Blog_n)]
        print('- {}'.format(blog))
