import argparse
import requests
import json


parser = argparse.ArgumentParser(prog='def-cli', description='serves as a terminal based dictionary')
parser.add_argument('word', help='the word to define')
args = parser.parse_args()

response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{args.word}")
data = response.json()


# important parts - meanings, definition a synonym an antonym
# partOfSpeech definitions 

for entry in data:
    for meaning in entry["meanings"]:
        print(f"\n{meaning['partOfSpeech']}")
        for d in meaning["definitions"]:
            print(f"  - {d['definition']}")
        
    print("\n", entry["sourceUrls"][0])
