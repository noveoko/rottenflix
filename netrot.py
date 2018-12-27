from bs4 import BeautifulSoup as bs


def getMovieRanking():
    movie_rankings = {}
    rankings = open('topmovies.html').read()
    soup = bs(rankings, 'html.parser')
    movies = soup.find_all("div",{"class":"film "})
    for movie in movies:
        try:
            title = movie.find("div",{"class":"film__original"}).text
            rating = movie.find("span",{"class":"rate__value"}).text
            movie_rankings[title] = rating
        except AttributeError as ee:
            continue
    return movie_rankings

def getRottenData():
    movie_data = {}
    data = open('rotten.html').read()
    soup = bs(data, 'html.parser')
    movies = soup.find_all("div", {"class":"mb-movie"})
    for movie in movies:
        try:
            title = movie.find("h3",{"class":"movieTitle"}).text
            tomScore = movie.find("span",{"class":"tMeterScore"}).text
            movie_data[title] = tomScore
        except AttributeError as ee:
            print(ee)
    return movie_data


def getNetflixMovies():
    movies = []
    page = open('netflix.html').read()
    soup = bs(page, 'html.parser')
    links = soup.find_all("a")
    for link in links:
        try:
            link_text = link['href']
            if 'watch' in link_text:
                movie_title = link.text.strip().lower()
                movies.append(movie_title)
            else:
                continue
        except Exception as ee:
            continue
    return movies

def extractAndRankMovies():
    top_movies = []
    netflix_list = getNetflixMovies()
    #movie_rankings = getMovieRanking() --old method to get rank
    movie_rankings = getRottenData() #using Rotten Tomatoe Netflix Data
    for movie, rank in movie_rankings.items():
        if movie.lower() in netflix_list:
            top_movies.append([movie, rank])

    top_movies.sort(key=lambda x: x[1], reverse=True)
    return top_movies

def saveMoviesToFile():
    movies_to_save = extractAndRankMovies()
    with open('top_movies_today.txt','w') as outfile:
        for movie, rank in movies_to_save:
            outfile.write(f"{movie:.<30}\t{rank:.5}\n")

if __name__ == "__main__":
    saveMoviesToFile()
