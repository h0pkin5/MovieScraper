import requests
from bs4 import BeautifulSoup as soup
from models import movie_dict, Movie

class ImdbScraper(object):
    def __init__(self, url):
        self.request_response = requests.get(url)
        self.page_soup = soup(self.request_response.content, 'html.parser')
        self.movie_dictionary = movie_dict

    def getVital(self):
        self.movie_dictionary['imdb'] = [i.strong.text for i in self.page_soup.find_all('div', class_='ratingValue')][0]
        self.movie_dictionary['title'] = [i.h1.text.replace('\xa0','') for i in self.page_soup.find_all('div', class_='title_wrapper')][0]
        self.movie_dictionary['plot'] = self.page_soup.find_all('div', class_='summary_text')[0].text.replace('\n','').replace('  ', '')
        self.movie_dictionary['director'] = self.page_soup.find_all('div', class_='credit_summary_item')[0].a.text
        self.movie_dictionary['cast'] = self.page_soup.find_all('div', class_='credit_summary_item')[-1].text.split('|')[0].replace('\n','').split(':')[1]

    def getSubtextInfo(self):
        genre_release_raw = [ i.find_all('a') for i in self.page_soup.find_all('div', class_='subtext')][0]
        genre_release_clean = [i.text.replace('\n', '') for i in genre_release_raw]
        
        self.movie_dictionary['runtime'] = [i.text.replace('\n','').replace(' ','') for i in self.page_soup.find_all('time')][0]
        self.movie_dictionary['genre'] = genre_release_clean[0]
        self.movie_dictionary['release'] = genre_release_clean[1]

    def getRottenTomatos(self,url):
        data_raw = requests.get(url)
        data_souped = soup(data_raw.content, 'html.parser')
        percentage = data_souped.find_all('div', class_='mop-ratings-wrap__half audience-score')[0].find(class_='mop-ratings-wrap__percentage').text.replace('\n','').replace(' ','')
        user_ratings = data_souped.rm_soup.find_all('div', class_='mop-ratings-wrap__half audience-score')[0].strong.text
        self.movie_dictionary['rotten tomatos'] = f'{percentage} {user_ratings}'

    def saveToJson(self):
        movie = Movie(moviedata=self.movie_dictionary)
        movie.movieToJson()

    def saveToCsv(self, outfile, mode='w'):
        movie = Movie(moviedata=self.movie_dictionary)
        movie.movieToCsv(outfile, mode=mode)
        

    
