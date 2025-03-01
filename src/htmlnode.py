class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Class not implemented")

    def props_to_html(self):
        propstring = ""
        for prop in self.props:
            propstring += f" {prop}=\"{self.props[prop]}\""
        return propstring
    
    def __repr__(self):
        return f"HTMLNode(Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Properties: {self.props})"