#!/usr/bin/env python3
import io
import unittest

from html_render import *

def render_result(element, ind=""):
    """
    calls the element's render method, and returns what got rendered as a
    string
    """
    # the StringIO object is a "file-like" object -- something that
    # provides the methods of a file, but keeps everything in memory
    # so it can be used to test code that writes to a file, without
    # having to actually write to disk.
    outfile = io.StringIO()
    # this so the tests will work before we tackle indentation
    if ind:
        element.render(outfile, ind)
    else:
        element.render(outfile)
    return outfile.getvalue()


class HTMLRenderTests(unittest.TestCase):

    def test_a(self):
        ca = A("http://google.com", "link to google")
        file_contents = render_result(ca)
        expected = f'<a href="http://google.com">link to google</a>'
        print(file_contents)

        self.assertEqual(expected, f'<a href="http://google.com">link to google</a>')

    def test_ul(self):
        ul = Ul(style='list-style-type:disc;')
        ul.append(Li("List item 1"))
        ul.append(Li("List item 2"))

        file_contents = render_result(ul).strip()
        print(file_contents)

        self.assertEqual(file_contents[:3], "<ul")
        assert file_contents.endswith("</ul>")
        assert f'\nList item 1\n' in file_contents
        assert f'\nList item 2\n' in file_contents




if __name__ == '__main__':
    unittest.main()
