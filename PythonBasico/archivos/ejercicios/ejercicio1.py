def read_file(path):
    songs_list=[]
    with open(path, 'r') as file:
          songs_list = file.readlines()
    return songs_list

def create_ordered_file(list):
    with open('ordered_list.txt', 'w', encoding='utf-8') as file :
        for item in list:
            file.write(item)

songs_list = read_file('song_list.txt')
ordered_songs = sorted(songs_list)
create_ordered_file(ordered_songs)
