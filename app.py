from scraper import ImdbScraper

def main(imdburl):
    movie = ImdbScraper(imdburl)
    movie.getVital()
    movie.getSubtextInfo()
    movie.saveToJson()

