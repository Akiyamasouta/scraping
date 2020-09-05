import requests, sys, webbrowser, bs4

print('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
print(res)

soup = bs4.BeautifulSoup(res.text, 'html.parser')
link_elems = soup.select('.r a')

num_open = min(5, len(link_elems))
print(num_open)
for i in range(num_open):
    webbrowser.open('http://google.com' + link_elems[i].get('href'))

