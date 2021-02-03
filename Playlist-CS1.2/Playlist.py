from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    # New song instance (node)
    new_song = Song(title)

    # Setting title
    new_song.set_title(title)

    # Assigns next song to the head
    new_song.set_next_song(self.__first_song)

    # head point at new song
    self.__first_song = new_song

  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    song_counter = 0
    current_song = self.__first_song

    while current_song.get_title() != title:
      #Counter is index, as it moves through the linked list, so does the counter
      song_counter += 1 
      #Goes to next element
      current_song = current_song.get_next_song()

      if current_song.get_title() == title:
        #Returns iteration
        return song_counter


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    pass



  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    song_counter = 0
    current_song = self.__first_song
    while current_song != None:
      song_counter += 1 
      # Next Node
      current_song = current_song.get_next_song()
    return song_counter


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    song_counter = 1
    current_song = self.__first_song

    if current_song == None:
      print(f"Playlist is empty")

    while current_song.get_title() != None:
      print(f"{song_counter}. {current_song.get_title()}")
      song_counter += 1 
      # Go to next node
      current_song = current_song.get_next_song()

      #If reached tail
      if current_song == None:
        break 

  