from scraper import ImdbScraper

def main(imdburl, rmurl=None):
    movie = ImdbScraper(imdburl)
    movie.getVital()
    movie.getSubtextInfo()
    if rmurl: movie.getRottenTomatos(rmurl)
    movie.saveToJson()

