from pathlib import Path

from lark import Lark

grammar = Path("source/http_request_in_editor/grammar.lark").read_text()

parser = Lark(grammar)

text = """GET http://example.com/auth

> {% client.global.set("auth", response.body.token);%}
"""

print(parser.parse(text).pretty())