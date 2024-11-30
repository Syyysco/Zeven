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

'''
This module will handle all operations related to calculations
'''
def convert_size(size_bytes) -> str:
    '''
    ## Converting size to readable units (B, KB, MB, GB, TB)
    To get the size in a more readable unit.
    '''
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB")
    i = int((len(str(size_bytes)) - 1) / 3)
    p = 1024 ** i
    s = round(size_bytes / p, 2)
    
    return f"{s} {size_name[i]}"


def convert_time(seconds: float) -> float:
    '''
    ## Converting float(seconds) to readable units (days, hours, minutes, seconds)
    To get the time in a more readable unit.
    '''
    intervals = [
        ('days', 86400.0),
        ('hours', 3600.0),
        ('minutes', 60.0),
        ('seconds', 1.0)
    ]

    total_time_str = ""
    remaining_time = seconds

    for name, count in intervals:
        if remaining_time >= count:
            value = remaining_time // count
            remaining_time -= value * count
            total_time_str += f"{int(value)} {name} "

    remaining_time_rounded = round(remaining_time, 2)
    if not total_time_str.strip():
        total_time_str = f"{remaining_time_rounded} seconds"
    else:
        total_time_str = total_time_str.strip()

    return total_time_str