# gita-py

**Bhagavad Gita in Python** — all 700 verses across 18 chapters, in both English and Sanskrit (Devanagari), with a clean integer-keyed API.

## Install

```bash
pip install gita-py
```

## Quick start

```python
from gita import get_verse, get_sanskrit_verse, get_verse_full, get_chapter_summary

# English meaning
print(get_verse(2, 47))
# "You have a right to perform your prescribed duties, but you are not
#  entitled to the fruits of your actions …"

# Sanskrit (Devanagari)
print(get_sanskrit_verse(2, 47))
# कर्मण्येवाधिकारस्ते मा फलेषु कदाचन।
# मा कर्मफलहेतुर्भूर्मा ते सङ्गोऽस्त्वकर्मणि॥

# Both at once
v = get_verse_full(4, 7)
# {"chapter": 4, "verse": 7, "chapter_name": "…", "sanskrit": "…", "english": "…"}

# Chapter summary
print(get_chapter_summary(18))

# Search
results = search_english("renunciation")
for r in results[:3]:
    print(r["chapter"], r["verse"], r["text"][:60])

# Random verse
print(get_random_verse())
```

## API reference

| Function | Returns |
|---|---|
| `get_verse(ch, v)` | English meaning |
| `get_sanskrit_verse(ch, v)` | Sanskrit Devanagari text |
| `get_verse_full(ch, v)` | Dict with both + metadata |
| `get_chapter(ch)` | All verses + summary for chapter |
| `get_chapter_summary(ch)` | Chapter summary string |
| `get_chapter_name(ch)` | Chapter title (Sanskrit/English) |
| `get_all_chapters()` | Metadata for all 18 chapters |
| `search_english(query)` | List of matching verse dicts |
| `get_random_verse()` | Random full verse dict |
| `get_quotes()` | Curated list of notable quotes |
| `verse_count(ch)` | Number of verses in chapter |

All chapter/verse keys are plain **integers** — no float keys, no collisions.

## Coverage

- **18 chapters**, **700 verses**
- English: scholarly translations
- Sanskrit: traditional Devanagari text
- Chapter summaries for all 18 chapters
