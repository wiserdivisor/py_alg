from html.parser import HTMLParser

class htmlparser(HTMLParser):
    def handle_comment(self, comment):
        if '\n' in comment:
            print('>>> Multi-line Comment\n',comment)
        else:
            print('>>> Single-line Comment\n',comment)

    def handle_data(self, data):
        print(">>> Data\n",data)

parse = htmlparser()
parse.feed(
'''
<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->
''')
parse.close()
