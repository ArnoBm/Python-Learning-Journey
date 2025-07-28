albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of Life"),
         (4, "She Used Me Up"),
     ]),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]),
]

for name, artist, year, songs in albums:
    print(f"Album: {name} by {artist} ({year})")
    for song_number, song_name in songs:
        print(f"  Track {song_number}: {song_name}")
    print()  # Print a blank line for better readability

print("-" * 30)

print()

# album = albums[3] # Accessing the fourth album
# print(album) # Output: ('More Mayhem', 'Imelda May', 2011, [(1, 'Pulling the Rug'), (2, 'Psycho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz')])
#
# songs = album[3]  # Accessing the list of songs in the fourth album
# print(songs)  # Output: [(1, 'Pulling the Rug'), (2, 'Psycho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz')]
#
# song = songs[1] # Accessing the second song in the fourth album
# print(song)  # Output: (2, 'Psycho')
# print(song[1])  # Output: 'Psycho'
#
# mayhem = albums[3][3][2][1] # Accessing the name of the third song in the fourth album
# print(mayhem)  # Output: 'Mayhem'
#
# print(albums[3]) # Output: ('More Mayhem', 'Imelda May', 2011, [(1, 'Pulling the Rug'), (2, 'Psycho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz')])

print(albums[1][3][5][1])  # Output: 'The Way I Choose'
print(albums[2][2]) # Output: 1981
print(albums[0][3][3][0]) # Output: 4
print(albums[2][3][1])  # Output: '(2, 'Keeping a Rendezvous')'