import re

VAR_TOKEN_START = "{{"
VAR_TOKEN_END = "}}" 
BLOCK_TOKEN_START = "{%"
BLOCK_TOKEN_END = "%}"

VAR_FRAGMENT = 0
OPEN_BLOCK_FRAGMENT = 1
CLOSE_BLOCK_FRAGMENT = 2
TEXT_FRAGMENT = 4

TOK_REGEX = re.compile(r"(%s.*?%s|%s.*?%s)" % (
    VAR_TOKEN_START,
    VAR_TOKEN_END,
    BLOCK_TOKEN_START,
    BLOCK_TOKEN_END
))

class _Node(object):
    def __init__(self, fragment=None):
        self.children = []
        self.creates_scope = False
        self.process_fragment(fragment)

    def process_fragment(self, fragment):
        pass

    def enter_scope(self):
        pass

    def render(self, context):
        pass

    def exit_scope(self):
        pass

    def render_children(self, context, children=None):
        if children is None:
            children = self.children

        def render_child(child):
            child_html = child.render(context)
            return '' if not child_html else str(child_html)

        return ''.join(map(render_child, children))

class _Variable(_Node):
    def process_fragment(self, fragment):
        self.name = fragment

    def render(self, context):
        return resolve_in_context(self.name, context)