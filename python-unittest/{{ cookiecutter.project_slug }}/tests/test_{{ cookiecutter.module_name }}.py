import unittest

from {{ cookiecutter.project_slug }}.{{ cookiecutter.module_name }} import inc

{%- set data = {
                  'name' : 'node.Name',
                  'id' : 'node.id',
               }
-%}


{% set test_case = 'it worked' %}
{% set another = testing %}

# class Test{{ test_case.name }}(unittest.TestCase):
#     def test_inc(self):
#         self.assertEqual(inc(2), 3)
# 
# {% for test in test_case.tests -%}
#     def test_{{ test.name }}(self):
# TODO: """{{ test.docstring }}"""
# TODO: # {{ test.comment }}
# TODO: for assertion in test.assertions:
# TODO: if{{ assertion.comment }}
# TODO: if assertion.invocation  invocation_str;  code_invocation;  code_to_invoke:  code_action: "fib(5)" 
# TODO: test.fn & test.args
#         self.{{ test.assertMethod }}({{ (test.args) }}, {{ test.expected }})
#     {% endfor %}
# {% endfor %}
#
#     def test_{{ test_name }}(self):
#         self.assertEqual('foo'.upper(), 'FOO')
# 
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
# 
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

class TestStringMethods(unittest.TestCase):
    def test_inc(self):
        self.assertEqual(inc(2), 3)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
