anki_converter

anki_converter.py is a simple script to convert a CSV of questions and answers into an Anki flashcard deck (.apkg) using the genanki library.

Requirements

Python 3.6 or newer

genanki

Installation

Create (and activate) a virtual environment (optional but recommended):

python3 -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate

Install genanki:

pip install genanki

Usage

python anki_converter.py <input.csv> -o <output.apkg> -d "<Deck Name>"

Positional arguments:

<input.csv>: Path to your CSV file. Must include headers question and answer (case-insensitive).

Options:

-o, --output: Output file name for the generated Anki deck (default: output.apkg).

-d, --deck-name: Name for the Anki deck inside the package (default: My Deck).

Example

Given a CSV file (for instance, questions.csv):

question,answer
What is 2+2?,4
Capital of France?,Paris

Run:

python anki_converter.py questions.csv -o math_and_geo.apkg -d "Math & Geo"

Import math_and_geo.apkg into Anki to see your new flashcards.

CSV Format Details

Headers: Must include question and answer. You may also use Q and A.

Rows missing either field will be skipped with a warning.

Error Handling

If genanki is not installed, the script will exit with a message:

Error: The 'genanki' module is not installed. Run 'python -m pip install genanki' and try again.

