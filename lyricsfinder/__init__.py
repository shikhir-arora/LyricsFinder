"""Searches lyrics."""

from .lyrics import LyricsManager
from .models import exceptions

extract_lyrics = LyricsManager.extract_lyrics
search_lyrics = LyricsManager.search_lyrics
