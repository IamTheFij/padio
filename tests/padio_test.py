# -*- coding: utf-8 -*-
from pathlib import Path

import pytest

import padio


@pytest.mark.parametrize(
    "value,expected",
    (
        ("file123", "123"),
        ("123file", "123"),
        ("123file456", "123"),
        ("file", ""),
    ),
)
def test_extract_numbers(value, expected):
    assert padio.extract_numbers(value) == expected


@pytest.mark.parametrize(
    "file_paths,expected",
    (
        ([Path("/path/to/file.a123.txt"), Path("/path/to/file.b123.txt")], 3),
        ([Path("/path/to/file.a023.txt"), Path("/path/to/file.b023.txt")], 3),
        ([Path("/path/to/file.a123.txt"), Path("/path/to/file.b12.txt")], 3),
    ),
)
def test_calc_pad_length(file_paths, expected):
    assert padio.calc_pad_length(file_paths) == expected


@pytest.mark.parametrize(
    "files,ignore_files,ignore,expected",
    (
        (
            [
                "file.a123.txt",
                "file.b123.txt",
            ],
            [],
            "",
            [
                Path("./file.a123.txt"),
                Path("./file.b123.txt"),
            ],
        ),
        (
            [
                "file.a123.txt",
                "file.b123.txt",
            ],
            [
                "file.a123.txt",
            ],
            "",
            [
                Path("./file.b123.txt"),
            ],
        ),
        (
            ["file.a123.txt", "file.b123.txt", "ignore.txt"],
            [
                "file.a123.txt",
            ],
            "ignore.*",
            [
                Path("./file.b123.txt"),
            ],
        ),
    ),
)
def test_get_files(files, ignore_files, ignore, expected):
    assert padio.get_files(files, ignore_files, ignore) == expected


@pytest.mark.parametrize(
    "files,pad_len,expected",
    (
        ([Path("./file.a12")], 1, []),
        ([Path("./file.a12")], 2, []),
        ([Path("./file.a12")], 3, [Path("./file.a012")]),
    ),
)
def test_pad_files(files, pad_len, expected):
    assert list(padio.pad_files(files, pad_len)) == list(zip(files, expected))
