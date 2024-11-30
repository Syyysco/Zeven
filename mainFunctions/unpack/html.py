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

def init(input_file: str, tags: bool = True, indent: int=4) -> str:
    from bs4 import BeautifulSoup
    import re

    def format_html(html_content):
        html_content = re.sub(r'\s+', ' ', html_content).strip()
        soup = BeautifulSoup(html_content, 'html.parser')

        if tags:
            from .css import init as csser
            from .js import init as javascripter
            
            for style_tag in soup.find_all('style'):
                if style_tag.string:  
                    css_formated = csser(style_tag.string, indent=indent) 
                    style_tag.string.replace_with(css_formated)  
        
            for script_tag in soup.find_all('script'):
                if script_tag:
                    javascript_formated = javascripter(script_tag.string, indent=indent)
                    script_tag.string.replace_with(javascript_formated)

        html_formated = soup.prettify()
        return html_formated

    def format_html_file(input_file):
        html_formated = format_html(input_file)
        return html_formated
    
    html_formated = format_html_file(input_file=input_file)
    return html_formated



