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

def init(input_file: str) -> str:
    import sqlparse

    def compact_sql(content: str) -> str:
        formatted_code = sqlparse.format(
            content,
            reindent=False,                  # Don't indent
            keyword_case='upper',            # Convert Keywords to uppercase
            strip_comments=True,             # Remove comments
            use_space_around_operators=True  # Añadir espacios alrededor de operadores
        )

        compacted_code = ' '.join(formatted_code.split())
        return compacted_code
    
    sql_comacted = compact_sql(content=input_file)
    return sql_comacted