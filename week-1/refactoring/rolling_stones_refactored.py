def all_titles():
    titles = [record['album'] for record in albums]
    return titles


def all_artists():
    artists = [record['artist'] for record in albums]
    return artists


def find_album(name):
    # answer= list(filter(lambda album: album["album"]==name, albums))
    return list(filter(lambda album: album["album"]==name, albums))
    # (old)for i in albums:
     #   (old)if album==i["album"]:
      #      (old)return i
       #(old) else:
        #    (old)return "None"




def findByNameRankYear(val):
    # first im doing this
    # then im doing this
    if (isinstance (val,str)):
        return list(filter(lambda album: album['album'] == val,albums))

    if (isinstance (val,int)):
        newVal = str(val)
        length = len(newVal)
        # is_it_x?()
        if (length == 4):
            return list(filter(lambda album: album['year'] == val, albums))
        if (length < 4):
            return list(filter(lambda album: album['number'] == val, albums))

# Before
def find_rank(rank):
    for i in albums2:
        if rank == i['number']:
        	return (i)
# After
def find_by_rank_2(rank):
    found_rank = list(filter(lambda album: rank == album['number'] , albums))
    return (found_rank)



def artist_list(library):
    return list(map(lambda album: album['artist'], library))
#(got this instead of creating a list and appending iterations in library!)

# Find the artist with the most number of albums in the top 500
def most_album(album_list):
# BEFORE:
   all_list = all_artists(albums)
   uniq_artist = {}
   for x in all_list:
       if x in uniq_artist:
           uniq_artist[x] += 1
       else:
           uniq_artist[x] = 1
   highest_count = max(uniq_artist.values())
   return [key for key, value in uniq_artist.items() if value == highest_count]

# AFTER (Got rid of the first line)
def most_album2(album_list):
   uniq_artist = {}
   for x in all_artists(albums):
       if x in uniq_artist:
           uniq_artist[x] += 1
       else:
           uniq_artist[x] = 1
   highest_count = max(uniq_artist.values())
   return ', '.join([key for key, value in uniq_artist.items() if value == highest_count])


#creates a dictionary with count of albums in each decade using earlier "find by year" function we wrote
songs_per_decade = dict(fifties = len(find_by_years(1950, 1959)),
sixties = len(find_by_years(1960, 1969)),
seventies = len(find_by_years(1970, 1979)),
eighties = len(find_by_years(1980, 1989)),
nineties = len(find_by_years(1990, 1999)),
twenties = len(find_by_years(2000, 2009)),
twentiones = len(find_by_years(2010, 2019)))

# Example 1:Before:
def search_by_rank(rank, data_set):
    for album in data_set:
        if rank == album['rank']:
                return album
# Example 1 After:
def search_by_rank_2(rank, data_set):
    return [album['name'] for album in data_set if rank == album['rank']][0]


all_artists(data_set):
#     artists = []
#     for data in data_set:
#         artists.append(data['artist'])
#     return list(set(artists))
    list_wrepeated = list(map(lambda data: data['artist'], data_set))
    return list(set(list_wrepeated))
