from talon.voice import Key, press, Str, Context
# Commands for annotating pdfs.

ctx = Context('skim', func=lambda app, window:  'com.apple.Preview' in app.bundle or  'net.sourceforge.skim-app.skim' in app.bundle)

keymap = {
    'highlight': Key('cmd-ctrl-h'),
    'anchor': Key('cmd-alt-n'),
    'note': Key('cmd-ctrl-n'),

}

ctx.keymap(keymap)
