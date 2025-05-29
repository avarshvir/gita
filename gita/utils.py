# utils.py

from .data import summaries, verses
from .constant import CHAPTER_TITLES, TOTAL_CHAPTERS


def get_summary(chapter: int) -> str:
    """Return the summary of the given chapter if available."""
    return summaries.get(chapter, "Summary not available for this chapter.")


def get_verse(chapter: int, verse_number: float) -> str:
    """Return the specific verse from the chapter if it exists."""
    try:
        return verses[chapter][verse_number]
    except KeyError:
        return "Verse not available."


def get_all_verses(chapter: int) -> dict:
    """Return all verses from the given chapter."""
    return verses.get(chapter, {})


def list_available_summaries() -> list:
    """Return a list of chapter numbers that have summaries."""
    return list(summaries.keys())


def is_valid_chapter(chapter: int) -> bool:
    """Check if a given chapter number is valid."""
    return 1 <= chapter <= TOTAL_CHAPTERS


def is_valid_verse(chapter: int, verse_number: float) -> bool:
    """Check if the given verse exists in the chapter."""
    return chapter in verses and verse_number in verses[chapter]


def get_chapter_title(chapter: int) -> str:
    """Return the title of the chapter if available."""
    #from constant import CHAPTER_TITLES
    return CHAPTER_TITLES.get(chapter, f"Chapter {chapter}")
