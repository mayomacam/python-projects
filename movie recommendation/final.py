import requests_with_caching
import json
def get_movies_from_tastedive(name):
    parameters = {"q": name, "type": "movies", "limit": 5}
    tastedive_response = requests_with_caching.get("https://tastedive.com/api/similar", params=parameters)
    py_data = json.loads(tastedive_response.text)
    return py_data
def extract_movie_titles(d):
    lst = []
    for i in d['Similar']["Results"]:
        lst.append(i['Name'])
    return lst
def get_related_titles(c):
    lst = list()
    for title in c:
        a = get_movies_from_tastedive(title)
        b = extract_movie_titles(a)
        for movie in b:
            if movie not in lst:
                lst.append(movie)
    return lst
def get_movie_data(name):
    p = {"t": name, "r": "json"}
    response = requests_with_caching.get("http://www.omdbapi.com/", params=p)
    data = json.loads(response.text)
    return data

def get_movie_rating(d):
    if len(d['Ratings']) > 1:
        if d['Ratings'][1]['Source'] == 'Rotten Tomatoes':
            v = int(d['Ratings'][1]['Value'][:2])
    else:
        v = 0
    return v

def getkey(item):
    return item[1]
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
def get_sorted_recommendations(lst):
    related_movies = get_related_titles(lst)
    ratings = list()
    sorted_list = list()
    for movie in related_movies:
        a = get_movie_data(movie)
        ratings.append(get_movie_rating(a))

    tuple1 = zip(related_movies, ratings)
    tuple2 = sorted(tuple1, key=getkey, reverse=True)
    for i in range(len(tuple2) - 1):
        if tuple2[i][0] not in sorted_list:
            if tuple2[i][1] == tuple2[i + 1][1]:
                if tuple2[i][0] < tuple2[i + 1][0]:
                    sorted_list.append(tuple2[i + 1][0])
                    sorted_list.append(tuple2[i][0])
            else:
                sorted_list.append(tuple2[i][0])

    return sorted_list
print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"]))
