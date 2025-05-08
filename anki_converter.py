#!/usr/bin/env python3
"""
anki_converter.py: Convert a CSV of questions and answers into an Anki .apkg deck using genanki.

Usage:
    # Install the genanki library if you haven't already:
    #    python -m pip install --upgrade pip
    #    python -m pip install genanki
    #
    python anki_converter.py mwah.csv -o my_deck.apkg -d "My Deck Name"

The CSV must have headers 'question' and 'answer' (case-insensitive).
"""
import sys

try:
    import genanki
except ImportError:
    sys.exit("Error: The 'genanki' module is not installed. Run 'python -m pip install genanki' and try again.")

import csv
import argparse
import random


def main():
    parser = argparse.ArgumentParser(description='Convert Q&A CSV to Anki .apkg')
    parser.add_argument('csv_file', help='Path to the CSV file with questions and answers (e.g., psps.csv)')
    parser.add_argument('-o', '--output', default='output.apkg', help='Output .apkg file name')
    parser.add_argument('-d', '--deck-name', default='My Deck', help='Name of the Anki deck')
    args = parser.parse_args()

    # Generate random unique IDs for deck and model
    deck_id = random.randrange(1 << 30, 1 << 31)
    model_id = random.randrange(1 << 30, 1 << 31)

    # Define a simple two-field model
    model = genanki.Model(
        model_id,
        'Simple QA Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ],
    )

    deck = genanki.Deck(deck_id, args.deck_name)

    # Read CSV and add notes
    with open(args.csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Normalize header lookup
            q = row.get('question') or row.get('Question') or row.get('Q')
            a = row.get('answer')   or row.get('Answer')   or row.get('A')
            if not q or not a:
                print(f"Skipping row with missing Q/A: {row}", file=sys.stderr)
                continue
            note = genanki.Note(model=model, fields=[q, a])
            deck.add_note(note)

    # Write to .apkg
    genanki.Package(deck).write_to_file(args.output)
    print(f"✔️ Anki deck saved to {args.output}")


if __name__ == '__main__':
    main()
