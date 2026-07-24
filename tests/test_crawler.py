import os
import json
import csv
from undergraves.crawler import SCAN_LEVELS
from undergraves.cli import is_valid_url
from undergraves.exporter import save_to_json, save_to_csv

def test_scan_levels_configuration():
    assert SCAN_LEVELS["T1"] == 50
    assert SCAN_LEVELS["T2"] == 200
    assert SCAN_LEVELS["T3"] == 500
    assert SCAN_LEVELS["T4"] == 2000
    assert SCAN_LEVELS["T5"] is None

def test_url_validation():
    assert is_valid_url("https://example.com") is True
    assert is_valid_url("http://sub.domain.org/path") is True
    assert is_valid_url("not_a_url") is False
    assert is_valid_url("ftp://invalid-scheme.com") is False

def test_exporter_json(tmp_path):
    sample_data = [{"url": "https://example.com", "title": "Example"}]
    file_path = tmp_path / "test_output.json"
    
    save_to_json(sample_data, str(file_path))
    
    assert os.path.exists(file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data == sample_data

def test_exporter_csv(tmp_path):
    sample_data = [{"url": "https://example.com", "title": "Example"}]
    file_path = tmp_path / "test_output.csv"
    
    save_to_csv(sample_data, str(file_path))
    
    assert os.path.exists(file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
        assert len(reader) == 1
        assert reader[0]["url"] == "https://example.com"
        assert reader[0]["title"] == "Example"