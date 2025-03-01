import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        node = TextNode("This is a text node", TextType.ITALIC, "http://test.com")
        node2 = TextNode("This is a text node", TextType.ITALIC, "http://test.com")
        node = TextNode("Text changed for test", TextType.ITALIC, "http://test.com")
        node2 = TextNode("Text changed for test", TextType.ITALIC, "http://test.com")
        self.assertEqual(node, node2)


    def assertEqual(self, node, node2):
        if node.__eq__(node2):
            print(f"{node} is equal to {node2}. The test passes.")
        else:
            print(f"{node} is not equal to {node2}. The test fails.")
        
    def assertNotEqual(self, node, node2):
        if not node.__eq__(node2):
            print(f"{node} is not equal to {node2}. The test passes.")
        else:
            print(f"{node} is equal to {node2}. The test fails.")

    def test_noteq(self):
        node = TextNode("This is a text node.", TextType.ITALIC)
        node2 = TextNode("This is a text node.", TextType.ITALIC, "http://test.com")
        self.assertNotEqual(node, node2)
        node = TextNode("This is a text node.", TextType.ITALIC)
        node2 = TextNode("This is a text node.", TextType.BOLD)
        self.assertNotEqual(node, node2)
        node = TextNode("This is a text node.", TextType.ITALIC, "http://test.com")
        node2 = TextNode("Text changed for test", TextType.ITALIC, "http://test.com")
        self.assertNotEqual(node, node2)

    def test_empty_url(self):
        node = TextNode("This is a text node.", TextType.NORMAL)
        self.assertURLEmpty(node)

    def assertURLEmpty(self, node):
        if node.url == None:
            print(f"{node} has an empty URL. The test passes.")
        else:
            print(f"{node} has a URL not equal to none. The test fails.")



if __name__ == "__main__":
    unittest.main()