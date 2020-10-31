import pytest

import pythonbible as bible
from pythonbible import InvalidVerseError


def test_get_verse_id(book, chapter, verse, verse_id):
    # Given a book of the Bible, a chapter number, and a verse number

    # When the get_verse_id() function is called
    actual_verse_id = bible.verses.get_verse_id(book, chapter, verse)

    # Then the verse id is the appropriate integer value
    assert verse_id == actual_verse_id


def test_get_verse_id_invalid_chapter(book, invalid_chapter, verse):
    # Given a book of the Bible, a chapter number, and a verse number that is not valid

    # When the get_verse_id() function is called, Then an exception is raised.
    with pytest.raises(bible.InvalidChapterError):
        bible.verses.get_verse_id(book, invalid_chapter, verse)


def test_get_verse_id_invalid_verse(book, chapter, invalid_verse):
    # Given a book of the Bible, a chapter number, and a verse number that is not valid

    # When the get_verse_id() function is called, Then an exception is raised.
    with pytest.raises(bible.InvalidVerseError):
        bible.verses.get_verse_id(book, chapter, invalid_verse)


def test_get_max_verse_number(book, chapter):
    # Given a book of the Bible and a chapter number
    # When we get the maximum verse number for that book and chapter
    max_verse_number = bible.get_max_number_of_verses(book, chapter)

    # Then the maximum verse number is the expected value
    assert max_verse_number == 31


def test_get_max_verse_number_invalid_chapter(book, invalid_chapter):
    # Given a book of the Bible and an invalid chapter number
    # When we attempt to get the maximum verse number for that book and chapter
    # Then an exception is raise.
    with pytest.raises(bible.InvalidChapterError):
        bible.get_max_number_of_verses(book, invalid_chapter)


def test_get_book_chapter_verse(verse_id, book, chapter, verse):
    # Given a valid verse id
    # When using that verse id to get the book, chapter, and verse
    actual_book, actual_chapter, actual_verse = bible.get_book_chapter_verse(verse_id)

    # Then the results match the expected book, chapter, and verse
    assert actual_book == book
    assert actual_chapter == chapter
    assert actual_verse == verse


def test_get_book_chapter_verse_invalid(invalid_verse_id):
    # Given an invalid verse id
    # When attempting to get the book, chapter, and verse
    # Then an error is raised.
    with pytest.raises(bible.InvalidVerseError):
        bible.get_book_chapter_verse(invalid_verse_id)


def test_get_book(verse_id, book):
    # Given a valid verse id
    # When using that verse id to get the book
    book_number = bible.get_book_number(verse_id)

    # Then the resulting book matches the expected book
    assert bible.Book(book_number) == book


def test_get_chapter(verse_id):
    # Given a valid verse id
    # When using that verse id to get the chapter
    chapter_number = bible.get_chapter_number(verse_id)

    # Then the resulting chapter number matches the expected chapter number (1)
    assert chapter_number == 1


def test_get_verse(verse_id):
    # Given a valid verse id
    # When using that verse id to get the verse
    verse_number = bible.get_verse_number(verse_id)

    # Then the resulting verse number matching the expected verse number (1)
    assert verse_number == 1


def test_get_verse_text(verse_id, verse_text_no_verse_number):
    # Given a valid verse id
    # When using that verse to get the verse text
    verse_text = bible.get_verse_text(verse_id, version=bible.Version.KING_JAMES)

    # Then the verse text is the appropriate verse text.
    assert verse_text == verse_text_no_verse_number


def test_get_verse_text_invalid(invalid_verse_id):
    # Given an invalid verse id
    # When attempting to get the verse text for that verse id
    # Then an error is raised.
    with pytest.raises(InvalidVerseError):
        bible.get_verse_text(invalid_verse_id)
