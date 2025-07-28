from SupportJukeBox import albums

while True:
    print("Welcome to the JukeBox!")
    print("-" * 23)
    print("Available Albums: ")

    for index, (title, artist, year, songs) in enumerate(albums):
        print(f"{index + 1}. {title} by {artist} ({year})")

    try:
        choice = int(input("\nPlease select an album (1-4) or 0 to exit: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 0:
        print("Goodbye!")
        break
    elif 1 <= choice <= len(albums):
        album = albums[choice - 1]
        print(f"\nYou selected: {album[0]} by {album[1]} ({album[2]})")
        print("Songs:")
        print("~" * 6)

        for song in album[3]:
            print(f"{song[0]}. {song[1]}")

        try:
            song_choice = int(input("\nEnter the song number to play (or 0 to go back): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if song_choice == 0:
            continue

        selected_song = next((song for song in album[3] if song[0] == song_choice), None)

        if selected_song:
            print(f"\n🎵 Now Playing: {selected_song[1]} 🎶\n")
        else:
            print("Invalid song number.")
    else:
        print("Invalid album selection.")
