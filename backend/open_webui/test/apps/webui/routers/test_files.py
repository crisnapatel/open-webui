import pytest
from fastapi import HTTPException, status

from open_webui.routers.files import _validate_file_extension


class TestFileExtensionValidation:
    def test_allows_case_insensitive_matches(self):
        _validate_file_extension("PDF", ["pdf", "doc"])
        _validate_file_extension("pdf", ["PDF", "DOC"])

    def test_rejects_disallowed_extensions(self):
        with pytest.raises(HTTPException) as exc_info:
            _validate_file_extension("exe", ["pdf", "doc"])

        assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST
        assert "File type exe is not allowed" in exc_info.value.detail
