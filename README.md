# RhythmFlow : Python Desktop Music Player

![Music player UI1](https://github.com/mohit-thakur09/RhythmFlow/assets/82665617/5191f77f-592b-4f65-9d43-e25a1995d54e)


This Python Desktop Music Player is a simple yet powerful music player built using the Tkinter library for the user interface and several third-party libraries such as Pygame, Mutagen, Multithreading, os, and cx_Oracle to provide a seamless music listening experience. This player allows you to play, pause, and create playlists of your favorite songs with an attractive and user-friendly graphical user interface.

## Features

- Play, Pause, and Control Music Playback
- Create and Manage Playlists
- Attractive User Interface
- Support for Various Audio Formats
- Multithreaded Design for Smooth Performance
- Integrated Database for Storing Song Information
- Oracle Database Connectivity for Song Information Retrieval

## Requirements

Before running the application, make sure you have the following dependencies installed:

- Python 3.7+
- Tkinter
- Pygame
- Mutagen
- cx_Oracle
- Pillow (PIL)

You can install these dependencies using pip:

```bash
pip install tkinter pygame mutagen cx_Oracle pillow
```

## Getting Started

1. Clone or download this repository to your local machine.

2. Make sure you have Oracle Database installed and configured properly.

3. Set up your Oracle Database connection parameters in the `config.py` file:

   ```python
   # Database Configuration
   DB_USERNAME = "your_username"
   DB_PASSWORD = "your_password"
   DB_HOST = "your_host"
   DB_PORT = "your_port"
   DB_SERVICE_NAME = "your_service_name"
   ```

4. Run the `create_tables.sql` script to create the necessary database tables.

5. Launch the application by running `music_player.py`:

   ```bash
   python music_player.py
   ```

6. You can now use the music player to play, pause, and create playlists of your favorite songs.

## Usage

- **Adding Music**: Click the "+" button to add songs to your library. The player will automatically retrieve song information from the Oracle database if available.

- **Creating Playlists**: Use the "Create Playlist" button to create a new playlist. You can add songs to a playlist by selecting them from your library and clicking "Add to Playlist."

- **Playing Music**: Double-click a song in your library or playlist to start playing it. You can use the play and pause buttons to control playback.

- **Managing Playlists**: Use the playlist dropdown menu to switch between playlists. You can also rename or delete playlists using the respective buttons.

- **Searching for Songs**: Use the search bar to quickly find songs in your library or playlists.

- **Volume Control**: Adjust the volume slider to control the playback volume.

## Screenshots

![Music player UI2](https://github.com/mohit-thakur09/RhythmFlow/assets/82665617/c0202a55-32e8-4334-9863-aa716253df17)

## Error Handling

![Music player UI error](https://github.com/mohit-thakur09/RhythmFlow/assets/82665617/b9bd842c-770b-4cbf-85ad-3ed6d9f0b603)



## Contributing

Contributions to this project are welcome. You can contribute by opening issues, providing feedback, or submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Enjoy your music with the Python Desktop Music Player!
