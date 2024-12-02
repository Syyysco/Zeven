# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import re

class TypeScriptFormatter:
    """
    A comprehensive TypeScript code formatter that handles extremely compacted code.
    """
    def __init__(self, indent_size: int = 4):
        """
        Initialize the TypeScript formatter.

        Args:
            indent_size (int): Number of spaces for each indentation level
        """
        self.indent_size = indent_size


class VersatileTypeScriptFormatter(TypeScriptFormatter):
    """
    Final and versatile TypeScript formatter capable of handling various scenarios.
    """

    def _advanced_preprocess(self, code: str) -> str:
        """
        Improved preprocessing to expand compact TypeScript code for better formatting.
        """

        '''def handle_dict_commas(match):
            block = match.group(0)
            # Add indentation for lines following a comma
            return re.sub(r',\s*', ',\n' + ' ' * self.indent_size, block)'''

        code = re.sub(r'([{}()[\]\-*/&|!:])([^\s])', r'\1 \2', code)
        code = re.sub(r'([^\s])([{}()[\]\-*/&|!:])', r'\1 \2', code)

        # Remove spaces before semicolons
        code = re.sub(r'\s+;', ';', code)

        # Add newlines after commas, semicolons and around braces
        #code = re.sub(r',\s*', ',\n', code)

        code = re.sub(r';\s*', ';\n', code)
        code = re.sub(r'([^\s])\{', r'\1\n{', code)
        code = re.sub(r'\}([^\s])', r'}\n\1', code)

        # Normalize arrow functions
        code = re.sub(r'=>\s*', '=> ', code)

        # Handle edge cases in nested blocks
        code = re.sub(r'\{\s+', r'{\n', code)
        code = re.sub(r'\s+\}', r'\n}\n', code)
        # Ensure a blank line after '}'
        code = re.sub(r'\}\s*', r'}\n\n', code)
        
        '''code = re.sub(r'\{[^{}]*?\}', handle_dict_commas, code)
        code = re.sub(r'^ (\S.*)', r'\1', code, flags=re.MULTILINE)'''

        return code

    def _tokenize_code(self, code: str) -> list:
        """
        Tokenize the code into manageable chunks for formatting.

        Args:
            code (str): TypeScript code to tokenize

        Returns:
            list: Tokens of code
        """
        # Tokenize preserving structure

        return [line for line in code.split('\n') if line.strip()]


    def _format_block(self, tokens: list) -> str:
        """
        Enhanced formatting for tokens with consistent and intelligent indentation.
        """
        formatted_lines = []
        indent_level = 0

        for token in tokens:
            if token.startswith(('}', ']', ')')):
                indent_level = max(0, indent_level - 1)

            formatted_lines.append(' ' * (indent_level * self.indent_size) + token)

            if token.endswith(('{', '[', '(')):
                indent_level += 1

        return '\n'.join(formatted_lines)

    def format_typescript(self, code: str) -> str:
        """
        Fully process and format the TypeScript code.
        """
        preprocessed_code = self._advanced_preprocess(code)
        tokens = self._tokenize_code(preprocessed_code)
        return self._format_block(tokens)


def init(input_file: str, indent: int = 4) -> str:
    versatile_formatter = VersatileTypeScriptFormatter(max(2, indent))
    formatted_result = versatile_formatter.format_typescript(input_file)
    return formatted_result