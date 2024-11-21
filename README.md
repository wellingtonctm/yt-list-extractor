
# YouTube Playlist Link Extractor

YouTube Playlist Link Extractor is a Python script that automates the process of extracting all video links from a given YouTube Music playlist. It uses Selenium with an undetected Chrome WebDriver to handle authentication and navigate the YouTube Music interface.

---

## Features

- Automates Google login for accessing private playlists.
- Extracts all video links from a specified YouTube Music playlist.
- Saves the links to a `.txt` file named after the playlist.

---

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Usage](#usage)
4. [License](#license)

---

## Requirements

- Python 3.7 or newer.
- The following Python libraries:
  - `undetected-chromedriver`
  - `selenium`
- Google Chrome browser installed.
- A YouTube Music account.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yt-list-extractor.git
   cd yt-list-extractor
   ```

2. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure Google Chrome is installed and up-to-date.

---

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. Provide your Google account credentials when prompted:
   - **User**: Your Google email.
   - **Password**: Entered securely without echoing.

3. Enter the URL of the YouTube Music playlist you wish to extract links from.

4. The script will:
   - Login to your Google account.
   - Open the playlist.
   - Extract all video links.
   - Save the links in a file named after the playlist title (e.g., `My Playlist.txt`).

---

## Example

1. Run the script:
   ```bash
   python main.py
   ```

2. Input:
   ```
   User: example@gmail.com
   Password: (hidden)
   Playlist: https://music.youtube.com/playlist?list=PLXXXXXX
   ```

3. Output:
   - A file named `My Playlist.txt` containing all the video links.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to contribute or report issues in the repository.
