def album_with_most_top_songs():
    songs = list(map(lambda song: song['name'], songlist))

    album_tracks = {}

    for album in tracks_data:
        album_tracks[album['album']] = 0
        for track in album['tracks']:
            if track in songs:
                album_tracks[album['album']] += 1
    topalbum = max(album_tracks, key=album_tracks.get)
    for album in tracks_data:
        if album['album'] == topalbum:
            topartist = album['artist']

    return topalbum + " by " + topartist

def artist_most_top_albums(album_list):
    artist_list = all_artists_map(album_list)
	#this is a list of all artists from the top-500-album dictionary
    artist_frequency = {}
    for artist in artist_list:
         if artist in artist_frequency:
                artist_frequency[artist] += 1
         else:
                artist_frequency[artist] = 1
    highest = max(artist_frequency.values())
    return[key for key, value in artist_frequency.items() if value == highest]



def artist_with_most_albums_or_songs(list_of_albums):
		artistlist = all_artists_map(album_list)
		return max(artistlist, key=artistlist.count)



list_years = []
for record in records:
    list_years.append(record['year'])
print(min(sorted(list_years)))
print(max(sorted(list_years)))

fifties = []
sixties = []
seventies = []
eighties = []
nineties = []
two_thou = []
two_ten = []

for year in list_years:
    if year in rank_range(0, 1959):
        fifties.append(year)
    if year in rank_range(1960, 1969):
        sixties.append(year)
    if year in rank_range(1970, 1979)):
        seventies.append(year)
    if year in rank_range(1980, 1989):
        eighties.append(year)
    if year in rank_range(1990, 1999)):
        nineties.append(year)
    if year in rank_range(2000, 2009):
        two_thou.append(year)
    if year in rank_range(2010, 2019):
        two_ten.append(year)



def most_popular_word():
    empty_list = []

    for record in albums:
        album_name = record['album']
        album_names_split = album_name.split()
        empty_list.append(album_names_split)

    flattened = [val for sublist in empty_list for val in sublist]

    counter_dict = {}

    for word in flattened:
        if word in counter_dict:
            counter_dict[word] += 1
        else:
            counter_dict[word] = 1

    to_tuples = counter_dict.items()
    max_tuple_value = max(to_tuples, key=lambda x: x[1])[1]

    output = []

    for tuple_item in to_tuples:
        if tuple_item[1] == max_tuple_value:
            output.append(tuple_item[0])

    return output

def most_common(dataset):
   artists = all_artists(dataset)
   return max(set(artists), key=artists.count)
# since this does not have for loop, it will only return the first match.
# Can’t get it to return all top artist. Same with top word










Audrey refactoring help 2 –

import plotly
from collections import Counter

plotly.offline.init_notebook_mode(connected=True)

def genres():

    list_of_genres = [record['genre'] for record in albums]
    empty_list = []
    empty_list2 = []
    empty_list3 = []

    for record in albums:
        genre = record['genre']
        genres_split = genre.split(",")
        empty_list.extend(genres_split)

    for genre in empty_list:
        spaces = genre.strip()
        empty_list2.append(spaces)

    for genre in empty_list2:
        if "& Country" in genre:
            empty_list3.append("Country")
        else:
            empty_list3.append(genre)

    count = Counter(empty_list3)
    most_popular = count.most_common()

    genres = []
    counts = []

    for genre in most_popular:
        genres.append(genre[0])
        counts.append(genre[1])

    trace = {'type': 'bar', 'x': genres, 'y': counts}

    return plotly.offline.iplot([trace])
