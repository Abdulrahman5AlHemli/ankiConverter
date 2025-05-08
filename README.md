# anki\_converter

`anki_converter.py` is a simple script to convert a CSV of questions and answers into an Anki flashcard deck (`.apkg`) using the [genanki](https://github.com/kerrickstaley/genanki) library.

---

## Requirements

* Python 3.6 or newer
* [genanki](https://pypi.org/project/genanki/)

## Installation

1. (Optional) Create & activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```
2. Install genanki:

   ```bash
   pip install genanki
   ```

## Usage

```bash
python anki_converter.py <input.csv> -o <output.apkg> -d "<Deck Name>"
```

**Positional arguments**:

* `<input.csv>`: Path to your CSV file. Must include headers `question` and `answer` (case-insensitive).

**Options**:

* `-o`, `--output`: Output file name for the generated Anki deck (default: `output.apkg`).
* `-d`, `--deck-name`: Name of the Anki deck inside the package (default: `My Deck`).

### Example

Given `questions.csv`:

```csv
question,answer
What is 2+2?,4
Capital of France?,Paris
```

Run:

```bash
python anki_converter.py questions.csv -o math_and_geo.apkg -d "Math & Geo"
```

Import `math_and_geo.apkg` into Anki to see your new flashcards.

## CSV Format Details

* **Headers**: `question` & `answer` (case-insensitive).
* Rows missing a field are skipped with a warning.

## Error Handling

If `genanki` is not installed, the script will exit with:

```
Error: The 'genanki' module is not installed. Run 'python -m pip install genanki' and try again.
```
