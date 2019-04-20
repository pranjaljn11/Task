#Logic for Random Music Player

import os, random, sys

playlist_full= (r"C:\Users\user_000\Media") #location for playlist

all_playlist = []
playlist_ = []

#creating playlist from the location/source with file extensions '.mkv' and '.mp4'
def create_playlist():
    for path, subdirs, files in os.walk(playlist_full):
        for file in files:
            if file.lower().endswith(('.mkv', '.mp4')):
                all_playlist.append(os.path.join(path, file))  #add only those files in playlist with extensions '.mkv' and '.mp4'

#random selection of song fromplaylist
def random_selection_from_playlist():
    random_selection = random.choice(all_playlist)
    if random_selection not in playlist_:
        playlist_.append(random_selection)
    else:
        pass

#creating random song selection and asking the user for confirmation
def get_selections():
    for i in range(number):
        random_selection_from_playlist()
    playlist_confirmation()


def number_of_selections():
    while True:
        try:
            global number
            number = int(input('How many files would you like to add to playlist? >>> '))
            break
        except ValueError:
            print('Enter a number.')


def remove_selection():
    while True:
        try:
            to_remove = int(input('To remove a selection enter the number of the selection you want removed here. >>> '))
            if to_remove <= len(playlist_):
             break
        except ValueError:
            print('Enter a number.')
            remove_selection()
        try:
            playlist_.pop((to_remove - 1))
            break
        except (IndexError, UnboundLocalError):
            print('Enter a vaild number')
            remove_selection()
    clear()
    playlist_confirmation()


def playlist_confirmation():
    ok = input('This list ok? >>> ').lower()
    if ok in ('yes', 'y'):
        play_playlist_()
    elif ok == 'no' or ok == 'n':
        while True:
            new = input('Get new list or remove a specific selection? >>> ').lower()
            if new == 'new list' or new == 'n':
                del playlist_[:]
                clear()
                get_selections()
                break
            elif new == 'specific selection' or new == 's':
                remove_selection()
                break
            else:
                 print('Enter \'new\' or \'selection\'')
    else:
        playlist_confirmation()


#play songs from playlist
def play_playlist_():
    for i in playlist_:
        play_cmd = "rundll32 url.dll,FileProtocolHandler \"" + i + "\""
        os.system(play_cmd)

def clear():
    os.system('cls')

def main():
    create_playlist()
    number_of_selections()
    get_selections()

if __name__=="__main__":
    main()