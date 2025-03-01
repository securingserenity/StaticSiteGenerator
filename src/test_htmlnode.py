import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_propstohtml(self):
        node = HTMLNode(value="test",props={"href": "https://test.com", "target": "test"})
        expected_prop_string = " href=\"https://test.com\" target=\"test\""
        self.assert_propstringEqTest(node, expected_prop_string)
      
      
    def assert_propstringEqTest(self, node, expected_prop_string):
        if node.props_to_html() == expected_prop_string:
            print(f"{node.props_to_html()} is equal to {expected_prop_string}. The test passes.")
        else:
            print(f"{node.props_to_html()} is not equal to {expected_prop_string}. The test fails.")

if __name__ == "__main__":
    unittest.main()