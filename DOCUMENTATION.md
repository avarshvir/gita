# gita-py Documentation

## Overview

`gita-py` is a lightweight Python package that provides programmatic access to the **Bhagavad Gita**.

It includes:

* Chapter summaries
* English translations
* Sanskrit (Devanagari) verses
* Chapter metadata
* Search functionality
* Random verse generator
* Curated quotes
* Validation helpers

---

# Installation

```bash
pip install gita-py
```

---

# Importing

Import individual functions:

```python
from gita.utils import (
    get_summary,
    get_verse,
    get_sanskrit_verse,
    get_verse_full,
    get_chapter,
    get_all_chapters,
    get_all_verses,
    get_chapter_title,
    get_random_verse,
    search_english,
    get_quotes,
    verse_count,
    is_valid_chapter,
    is_valid_verse,
)
```

---

# API Reference

## get_summary()

Returns the summary of a chapter.

```python
get_summary(chapter: int)
```

### Example

```python
summary = get_summary(2)
print(summary)
```

Returns:

```text
A string containing the chapter summary.
```

Returns `None` if the chapter number is invalid.

---

## get_verse()

Returns the English translation of a verse.

```python
get_verse(chapter: int, verse: int)
```

### Example

```python
print(get_verse(2, 47))
```

Returns:

```text
You have a right to perform your prescribed duty...
```

Returns `None` if the verse does not exist.

---

## get_sanskrit_verse()

Returns the Sanskrit (Devanagari) text.

```python
get_sanskrit_verse(chapter: int, verse: int)
```

### Example

```python
print(get_sanskrit_verse(2, 47))
```

---

## get_verse_full()

Returns complete information about a verse.

```python
get_verse_full(chapter: int, verse: int)
```

### Example

```python
verse = get_verse_full(2, 47)
```

Example output:

```python
{
    "chapter": 2,
    "verse": 47,
    "chapter_name": "Sankhya Yoga",
    "sanskrit": "...",
    "english": "..."
}
```

---

## get_chapter()

Returns an entire chapter.

```python
get_chapter(chapter: int)
```

Example:

```python
chapter = get_chapter(1)

print(chapter["name"])
print(chapter["summary"])
print(chapter["verses"])
```

Returns:

```python
{
    "chapter": 1,
    "name": "...",
    "summary": "...",
    "verses": {
        1: {
            "english": "...",
            "sanskrit": "..."
        }
    }
}
```

---

## get_all_verses()

Returns every English verse in a chapter.

```python
get_all_verses(chapter: int)
```

Example:

```python
verses = get_all_verses(3)
```

---

## get_all_chapters()

Returns metadata for all 18 chapters.

```python
get_all_chapters()
```

Example output:

```python
{
    1: {
        "name": "...",
        "verse_count": 47,
        "summary": "..."
    }
}
```

---

## get_chapter_title()

Returns the title of a chapter.

```python
get_chapter_title(chapter: int)
```

Example:

```python
print(get_chapter_title(18))
```

---

## search_english()

Searches English verse translations.

```python
search_english(query: str)
```

Example:

```python
results = search_english("duty")

for verse in results:
    print(verse)
```

Example output:

```python
[
    {
        "chapter": 2,
        "verse": 47,
        "text": "You have a right..."
    }
]
```

---

## get_random_verse()

Returns a random verse.

```python
get_random_verse()
```

Example:

```python
print(get_random_verse())
```

---

## get_quotes()

Returns curated Bhagavad Gita quotes.

```python
quotes = get_quotes()

for quote in quotes:
    print(quote)
```

---

## verse_count()

Returns the number of verses in a chapter.

```python
verse_count(chapter: int)
```

Example:

```python
print(verse_count(18))
```

Returns:

```text
78
```

---

## is_valid_chapter()

Checks whether a chapter exists.

```python
is_valid_chapter(chapter: int)
```

Example:

```python
print(is_valid_chapter(5))
```

Returns:

```python
True
```

---

## is_valid_verse()

Checks whether a verse exists.

```python
is_valid_verse(chapter: int, verse: int)
```

Example:

```python
print(is_valid_verse(2, 47))
```

Returns:

```python
True
```

---

# Error Handling

Most lookup functions return `None` when an invalid chapter or verse is requested.

Example:

```python
print(get_verse(20, 1))
```

Output:

```python
None
```

---

# Complete Example

```python
from gita.utils import *

print(get_summary(2))
print()

print(get_verse(2, 47))
print()

print(get_sanskrit_verse(2, 47))
print()

verse = get_verse_full(2, 47)

print("Chapter:", verse["chapter"])
print("Verse:", verse["verse"])
print("Title:", verse["chapter_name"])
print("Sanskrit:", verse["sanskrit"])
print("English:", verse["english"])
print()

print("Random Verse")
print(get_random_verse())
```

---

# Notes

* The Bhagavad Gita contains **18 chapters**.
* Sanskrit verses are provided in **Devanagari script**.
* English translations are indexed by chapter and verse number.
* All helper functions are designed to be lightweight and require no internet connection.

---

# License

This project is licensed under the MIT License.
