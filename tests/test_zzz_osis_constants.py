import pytest

import pythonbible as bible
from pythonbible.bible.osis.constants import get_book_by_id


def test_get_book_by_id():
    assert get_book_by_id("Gen") == bible.Book.GENESIS


def test_get_book_by_id_null():
    with pytest.raises(bible.InvalidBookError):
        get_book_by_id("blah")
