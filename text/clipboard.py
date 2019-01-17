# An indexed clipboard.
# If a keyword is included it will save under that keyword,
# otherwise behaves as normal copy and paste.
from talon.voice import Key, press, Str, Context
from talon import clip
from user.utils import *

ctx = Context('clipboard')

indices = {}

def copy_selection(m):
    with clip.capture() as sel:
        press('cmd-c')
    if len(m._words) > 1:
        words = ' '.join(parse_words(m))
        indices[words] = sel.get()
    else:
        clip.set(sel.get())

def paste_selection(m):
    if len(m._words) > 1:
        words = ' '.join(parse_words(m))
        return Str(indices[words])(None)
    else:
        press('cmd-v', wait=0)

ctx.keymap({
    'paste [<dgndictation>]': paste_selection,
    'clip [<dgndictation>]': copy_selection,
})
