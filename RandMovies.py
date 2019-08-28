import requests,bs4,webbrowser,sys,time,random,os


def main ():
	movies=['interstellar','her']
	im_feeling_luck(get_movies(movies))

def get_movies(movies):
	movie=movies[random.randint(0,len(movies)-1)]
	os.system("say'looks like we are going to watch " + movie + "tonight")
	return movie


def im_feeling_luck(movie):
	sterm = 'watch' + movie + 'online free solarmovie'
	res=requests.get('https://www.google.co.in/search?q='+sterm)
	res.raise_for_status()
	bso=bs4.BeautifulSoup(res.text,'lxml')
	linkeles = bso.select('.r a')
	webbrowser.open('https://www.google.com' + linkeles[0].get('href'))

main()