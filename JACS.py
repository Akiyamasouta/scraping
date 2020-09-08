import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    terms = '+'.join(sys.argv[1:])
else:
    terms = pyperclip.paste()

webbrowser.open("https://pubs.acs.org/action/doSearch?AllField=" + terms + "&SeriesKey=jacsat")