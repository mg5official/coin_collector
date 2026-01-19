import json

import pytest
from pydantic import ValidationError

from coin_collector.config import load_level


def test_invalid_level_raises_validation_error(tmp_path):
    bad_level = {
        "width": "not-a-number",
        "height": 600,
        "player_start": {"x": 50, "y": 50},
        "coins": [{"x": 100, "y": 100, "r": 12}],
        "walls": [],
    }

    p = tmp_path / "bad_level.json"
    p.write_text(json.dumps(bad_level), encoding="utf-8")

    with pytest.raises(ValidationError):
        load_level(str(p))
