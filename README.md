# 📖 gita

`gita` is a lightweight Python package providing access to **summaries and verses** from the **Bhagavad Gita**. It allows you to retrieve summaries, verses, chapter titles, and validate content programmatically.

---

## 🌟 Features

- 📚 Get summary of a chapter
- 🔍 Fetch a specific verse
- 📖 Get all verses in a chapter
- ✅ Validate chapters and verses
- 🏷️ Retrieve chapter titles

---

## 📦 Installation

Clone this repository and install locally using:

```bash
git clone https://github.com/avarshvir/gita.git
cd gita
```
## 🧠 Usage
1. Import the functions
```
from gita.utils import (
    get_summary,
    get_verse,
    get_all_verses,
    list_available_summaries,
    is_valid_chapter,
    is_valid_verse,
    get_chapter_title
)
```
2. Get Chapter Summary
```
print(get_summary(1))

```
3. Get a Specific Verse
```
print(get_verse(1, 1))
```
4. Get All Verses from a Chapter
```
verses = get_all_verses(1)
for verse_number, verse_text in verses.items():
    print(f"{verse_number}: {verse_text}")
```
5. List Available Summaries
```
print(list_available_summaries())
# Output: [1, 2, 3, 4]
```
6. Validate Chapter or Verse
```
print(is_valid_chapter(1))  # True
print(is_valid_verse(1, 1))  # True or False
```
7. Get Chapter Title
```
print(get_chapter_title(1))
# Output: Arjuna Vishada Yoga - The Yoga of Arjuna's Dejection
```

## 🧪 Running Tests
To run the unit tests, from the project root:
```
python -m unittest discover tests
```

## 📁 Project Structure
```
gita/
│
├── gita/
│   ├── __init__.py
│   ├── utils.py
│   ├── data.py
│   └── constant.py
│
├── tests/
│   └── test_gita.py
│
├── setup.py
├── README.md
├── pyproject.toml
└── MANIFEST.in
```

## 📜 License
This project is licensed under the MIT License.

## 🙏 Acknowledgements
- Inspired by the sacred Bhagavad Gita
- Developed with ❤️ by Arshvir

## 🚀 Future Plans
- Add all 18 chapter summaries
- Include all verses from all chapters
- Add audio and image support
- Build a Streamlit/Flask interface



