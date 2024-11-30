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
This module simply plays a sound.
'''
import os, threading
if 'PYGAME_HIDE_SUPPORT_PROMPT' not in os.environ:
    import contextlib
    with contextlib.redirect_stdout(None):
        import pygame
else: import pygame; os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

pygame.mixer.init()


SOUNDS_FOLDER = file_path = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__))), '..', 'src')

def play(sound: str, index: int=None) -> None:
    '''
    Play a sound within the SOUND_PATHS list

    Args:
        sound (str): Indicates the name of the .wav file to play
        index (int): If a sound requires an index, this will be considered.
        
    List: 
    ```['error', 'success', 'turn', 'switch_option', 'switch_panel', 'toggle']
    '''
    SOUND_PATHS = {
        'error': os.path.join(SOUNDS_FOLDER, 'notification_sounds', 'error', f'error{index}.wav'),
        'success': os.path.join(SOUNDS_FOLDER, 'notification_sounds', 'success', f'success{index}.wav'),
        'turn': os.path.join(SOUNDS_FOLDER, 'settings_sounds', 'turn.wav'),
        'switch_option': os.path.join(SOUNDS_FOLDER, 'settings_sounds', 'switch_option.wav'),
        'switch_panel': os.path.join(SOUNDS_FOLDER, 'settings_sounds', 'switch_panel.mp3'),
        'toggle': os.path.join(SOUNDS_FOLDER, 'settings_sounds', 'toggle.wav'),
    }
    
    def play_bg():
        nonlocal sound
        sound = pygame.mixer.Sound(SOUND_PATHS[sound])
        sound.play()
        
    threading.Thread(target=play_bg, daemon=True).start()
