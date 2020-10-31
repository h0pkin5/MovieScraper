import json, csv

movie_dict = {
        'title': None,
        'runtime': None,
        'cast': None,
        'plot': None,
        'release': None,
        'imdb': None,
        'genre': None,
        'director': None    
        }


class Movie(object):
    def __init__(self, moviedata=movie_dict):

        self.dictionary = moviedata
        self.title = moviedata['title']
        self.runtime = moviedata['runtime']
        self.cast = moviedata['cast']
        self.plot =moviedata['plot']
        self.release = moviedata['release']
        self.imdb = moviedata['imdb']
        self.genre = moviedata['genre']

    def movieToJson(self):
        title = str(self.title).replace(' ', '_')
        with open(title + '.json', 'w') as json_file:
            json.dump(self.dictionary, json_file)

    def movieToCsv(self, outfile, mode='w'):
        if mode == 'w': fieldnames = [k for k, _ in self.dictionary.items()]
        
        with open(outfile, mode=mode) as csv_file:
            
            if fieldnames: 
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writeheader()
                csv_writer.writerow(self.dictionary)
            else: 
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([v for k,v in self.dictionary])

