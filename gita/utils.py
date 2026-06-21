"""Legacy helper API wrappers for gita-py."""

from .data import summaries, verses, sanskrit_verses, quotes
from .constant import CHAPTER_NAMES, CHAPTER_TITLES, TOTAL_CHAPTERS, VERSE_COUNTS

def get_summary(chapter: int) -> str:
    """Return the summary for *chapter* (1-18), or None if invalid."""
    if not _valid_chapter(chapter):
        return None
    return summaries.get(chapter, "Summary not available for this chapter.")


def get_verse(chapter: int, verse):
    """Return the English meaning of *chapter*:*verse*, or None."""
    if isinstance(verse, float) and verse.is_integer():
        verse = int(verse)
    if not _valid_verse(chapter, verse):
        return None
    return verses.get(chapter, {}).get(verse)


def get_all_verses(chapter: int) -> dict:
    """Return all verses for the requested chapter."""
    return verses.get(chapter, {})


def list_available_summaries() -> list:
    """Return a list of chapters that have summaries available."""
    return list(summaries.keys())


def is_valid_chapter(chapter: int) -> bool:
    """Return True if the chapter exists."""
    return 1 <= chapter <= TOTAL_CHAPTERS


def is_valid_verse(chapter: int, verse_number) -> bool:
    """Return True if the requested verse exists in the given chapter."""
    if isinstance(verse_number, float) and verse_number.is_integer():
        verse_number = int(verse_number)
    return chapter in verses and verse_number in verses[chapter]


def get_chapter_title(chapter: int) -> str:
    """Return the chapter title if available."""
    if not _valid_chapter(chapter):
        return None
    return CHAPTER_TITLES.get(chapter) or CHAPTER_NAMES.get(chapter) or f"Chapter {chapter}"


def _valid_chapter(chapter: int) -> bool:
    return isinstance(chapter, int) and 1 <= chapter <= 18


def _valid_verse(chapter: int, verse: int) -> bool:
    return (
        _valid_chapter(chapter)
        and isinstance(verse, int)
        and 1 <= verse <= VERSE_COUNTS.get(chapter, 0)
    )


def get_sanskrit_verse(chapter: int, verse: int):
    """Return the Sanskrit (Devanagari) text of *chapter*:*verse*, or None."""
    if not _valid_verse(chapter, verse):
        return None
    return sanskrit_verses.get(chapter, {}).get(verse)


def get_verse_full(chapter: int, verse: int):
    """
    Return a dict with all data for *chapter*:*verse*::

        {
            "chapter": 2,
            "verse":   47,
            "chapter_name": "Sankhya Yoga ...",
            "sanskrit": "कर्मण्येवाधिकारस्ते ...",
            "english":  "You have a right to ...",
        }

    Returns None if chapter or verse is invalid.
    """
    if not _valid_verse(chapter, verse):
        return None
    return {
        "chapter":      chapter,
        "verse":        verse,
        "chapter_name": CHAPTER_NAMES.get(chapter, ""),
        "sanskrit":     sanskrit_verses.get(chapter, {}).get(verse, ""),
        "english":      verses.get(chapter, {}).get(verse, ""),
    }


def get_chapter(chapter: int):
    """
    Return all data for *chapter*::

        {
            "chapter": 2,
            "name":    "Sankhya Yoga ...",
            "summary": "...",
            "verses": {1: {"english": "...", "sanskrit": "..."}, ...},
        }
    """
    if not _valid_chapter(chapter):
        return None
    ch_en = verses.get(chapter, {})
    ch_sa = sanskrit_verses.get(chapter, {})
    all_verses = {
        v: {"english": ch_en.get(v, ""), "sanskrit": ch_sa.get(v, "")}
        for v in sorted(ch_en.keys())
    }
    return {
        "chapter": chapter,
        "name":    CHAPTER_NAMES.get(chapter, ""),
        "summary": summaries.get(chapter, ""),
        "verses":  all_verses,
    }


def get_all_chapters() -> dict:
    """Return lightweight metadata (no verse text) for all 18 chapters."""
    return {
        ch: {
            "name":        CHAPTER_NAMES[ch],
            "verse_count": VERSE_COUNTS[ch],
            "summary":     summaries[ch],
        }
        for ch in range(1, 19)
    }


def search_english(query: str, case_sensitive: bool = False) -> list:
    """
    Search English verse meanings for *query*.
    Returns a list of ``{"chapter", "verse", "text"}`` dicts.
    """
    q = query if case_sensitive else query.lower()
    results = []
    for ch, ch_verses in verses.items():
        for v, text in ch_verses.items():
            haystack = text if case_sensitive else text.lower()
            if q in haystack:
                results.append({"chapter": ch, "verse": v, "text": text})
    return results


def get_random_verse() -> dict:
    """Return a random verse (full data dict)."""
    import random
    ch = random.choice(list(verses.keys()))
    v  = random.choice(list(verses[ch].keys()))
    return get_verse_full(ch, v)


def get_quotes() -> list:
    """Return the curated list of notable Gita quotes."""
    return list(quotes)


def verse_count(chapter: int):
    """Return the number of verses in *chapter*, or None if invalid."""
    if not _valid_chapter(chapter):
        return None
    return VERSE_COUNTS.get(chapter)
