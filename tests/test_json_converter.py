import json
import os

import pytest

import pythonbible as bible
from pythonbible.bible.json_converter import JSONConverter

TEST_DATA_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")


def test_json_converter(
    kjv_parser, short_verse_id_list, short_verse_data_json, short_book_title_data_json
):
    _run_json_converter_test_for_version(
        kjv_parser,
        short_verse_id_list,
        short_verse_data_json,
        short_book_title_data_json,
    )


def test_json_converter_blank_verse(
    asv_parser,
    short_verse_id_list,
    short_verse_data_json_asv,
    short_book_title_data_json_asv,
):
    _run_json_converter_test_for_version(
        asv_parser,
        short_verse_id_list,
        short_verse_data_json_asv,
        short_book_title_data_json_asv,
    )


def _run_json_converter_test_for_version(
    parser, short_verse_id_list, short_verse_data_json, short_book_title_data_json
):
    # Given a parser, a data folder, a list of verse ids, and no existing json file.
    version_folder = os.path.join(TEST_DATA_FOLDER, parser.version.value.lower())
    verses_filename = os.path.join(version_folder, "verses.json")
    books_filename = os.path.join(version_folder, "books.json")
    remove_file_if_exists(verses_filename)
    remove_file_if_exists(books_filename)

    # When we use the json converter to generate the json file
    json_converter = JSONConverter(
        parser, data_folder=TEST_DATA_FOLDER, verse_ids=short_verse_id_list
    )
    json_converter.generate_verse_file()
    json_converter.generate_book_file()

    # Then the json files exists.
    assert os.path.exists(verses_filename)
    assert os.path.exists(books_filename)

    # And the data in the file correctly contains the verse data.
    with open(verses_filename) as json_file:
        verse_data = json.load(json_file)

    assert verse_data == short_verse_data_json

    # And the data in the books file correctly contains the book title data.
    with open(books_filename) as json_file:
        book_title_data = json.load(json_file)

    assert book_title_data == short_book_title_data_json

    # Clean Up (remove the file)
    remove_file_if_exists(verses_filename)
    remove_file_if_exists(books_filename)


def test_json_converter_null_parser():
    # Given a null parser
    json_converter = JSONConverter(None)

    # When we attempt to generate the JSON file
    # Then an error is raised.
    with pytest.raises(bible.InvalidBibleParserError):
        json_converter.generate_verse_file()


def test_json_converter_invalid_parser_type():
    # Given a parser instance that is not a valid type
    json_converter = JSONConverter("invalid parser")

    # When we attempt to generate the JSON file
    # Then an error is raised.
    with pytest.raises(bible.InvalidBibleParserError):
        json_converter.generate_verse_file()


def remove_file_if_exists(filename):
    try:
        os.remove(filename)
    except OSError:
        pass