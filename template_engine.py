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

def compile(self):
    root = _Root()
    scope_stack = [root]
    
    for fragment in self.each_fragment():
        if not scope_stack:
            raise TemplateError('nesting issues')

        parent_scope = scope_stack[-1]

        if fragment.type == CLOSE_BLOCK_FRAGMENT:
            parent_scope.exit_scope()
            scope_stack.pop()
            continue

        new_node = self.create_node(fragment)

        if new_node:
            parent_scope.children.append(new_node)
            if new_node.creates_scope:
                scope_stack.append(new_node)
                new_node.enter_scope()

    return root