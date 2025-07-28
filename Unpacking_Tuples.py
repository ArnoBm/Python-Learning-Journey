albums = [("Welcome to my Night", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
           ("Night fight", "Budgie", 1981),
            ("More Mayhem", "Imelda May", 2011),
             ("Ride the Lightning", "Metallica", 1984),
          ]

print(len(albums))

for name, artist, year in albums:
    print(f"Album: {name}, Artist: {artist}, Year: {year}")