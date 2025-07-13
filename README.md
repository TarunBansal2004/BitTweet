# BitTweet - A Nostalgic Twitter

BitTweet is a Django-based web application inspired by the early days of Twitter (circa 2006) and the aesthetic of 1980s/1990s computing. Designed to serve as a personal tweet scrapbook, it allows users to post short messages with mood tags, view them in a retro-styled timeline, and filter them using a memory lane feature. The project highlights Django backend development and pixelated frontend design, offering a unique nostalgic experience.

## Features
- **User Authentication**: Secure signup and login to create private tweet timelines.
- **Tweet Management**: Post tweets (up to 140 characters) with mood tags (Happy, Sad, Nostalgic) accompanied by a retro sound effect.
- **Timeline View**: Display user tweets in a CRT-style interface, sorted by date (newest first).
- **Memory Lane**: Filter tweets by mood or date range in a terminal-inspired layout.
- **Retro Bot**: Provides predefined, nostalgic responses (e.g., "Great tweet!") on post submission.
- **Design**: Utilizes pixel fonts, a black/green color scheme, and CRT scanline effects for an authentic vintage look.

## Technical Stack
- **Backend**: Django framework with a database.
- **Frontend**: HTML, CSS, and JavaScript for pixelated UI implementation.
- **Resources**: Google Fonts ("Press Start 2P"), Freesound.org (audio effects).

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/bittweet.git
   cd bittweet
   ```
2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```
   python manage.py migrate
   ```
5. Start the development server:
   ```
   python manage.py runserver
   ```
6. Access the application at `http://127.0.0.1:8000/`.

## Project Structure
- `bittweet/`: Main Django project configuration files.
- `bitTweet/`: Application directory containing models, views, and templates.
- `templates/bitTweet/`: HTML templates (e.g., `index.html`, `timeline.html`).
- `static/`: Static assets including CSS, JavaScript, images, and audio files.

## Usage
- **Homepage**: Initial page with a header and login/signup form.
- **Main Interface**: Post-login view includes a navigation bar (logout/search), a header, a tweet form (left), a profile section (right), a tweets list, and a "Memory Lane" button below.
- **Demonstration**: A 3-minute video showcasing signup, tweet posting, and filtering is recommended for presentation.

## Contributing
Contributions are welcome. Please fork the repository and submit pull requests with detailed descriptions of changes. Ensure adherence to the project’s coding standards and retro design guidelines.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Inspired by the simplicity of early Twitter and the visual style of 1980s/1990s computers.
- Audio assets sourced from Freesound.org.
- Developed with dedication as of 11:41 AM IST on Sunday, July 13, 2025.

