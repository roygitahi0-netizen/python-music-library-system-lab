from typing import List, Dict

class Song:
    """
    A class to represent a musical song and track aggregate music library statistics.
    
    This class uses class attributes to maintain a global state across all Song 
    instances, allowing for real-time analytics on the library's composition.
    """

    # --- Class Attributes (Global State) ---
    # Shared across all instances to track the library's total state.
    count: int = 0
    genres: List[str] = []
    artists: List[str] = []
    genre_count: Dict[str, int] = {}
    artist_count: Dict[str, int] = {}

    def __init__(self, name: str, artist: str, genre: str):
        """
        Initializes a Song instance and automatically updates global library statistics.
        """
        self.name = name
        self.artist = artist
        self.genre = genre

        # Trigger class-level updates immediately upon instantiation
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    # --- Class Methods (Global State Management) ---

    @classmethod
    def add_song_to_count(cls):
        """Increments the total number of songs in the registry."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre: str):
        """Registers a unique genre. Ensures no duplicates in the genres list."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist: str):
        """Registers a unique artist. Ensures no duplicates in the artists list."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre: str):
        """Updates the tally of songs for a specific genre."""
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, artist: str):
        """Updates the tally of songs for a specific artist."""
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1

    # --- Data Accessor Class Methods ---

    @classmethod
    def get_count(cls) -> int:
        """Returns the total number of songs created."""
        return cls.count

    @classmethod
    def get_artists(cls) -> List[str]:
        """Returns a list of all unique artists in the library."""
        return cls.artists

    @classmethod
    def get_genres(cls) -> List[str]:
        """Returns a list of all unique genres in the library."""
        return cls.genres

    @classmethod
    def get_artist_count(cls) -> Dict[str, int]:
        """Returns a dictionary mapping artists to their song counts."""
        return cls.artist_count

    @classmethod
    def get_genre_count(cls) -> Dict[str, int]:
        """Returns a dictionary mapping genres to their song counts."""
        return cls.genre_count
