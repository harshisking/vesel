import pytest

from vesel.exceptions import CorruptedFileError
from vesel.io import VeselIO


def test_checksum_mismatch(tmp_path):
    path = tmp_path / "corrupt.vesel"

    path.write_bytes(
        b"HBVSL\x00\x03\x00\x04none\x00\x00\x00\x05HelloChecksum"
    )

    with pytest.raises(CorruptedFileError):
        VeselIO.read(path)