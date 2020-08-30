import webbrowser, sys

#コマンドラインにmapIt.pyのあとに地名を打てばそれを読み込める
#sys.argvの１つめはmapIt.pyとなる(sys.argv[1:]で省く)
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

