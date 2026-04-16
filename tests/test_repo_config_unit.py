import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import collector


class RepoConfigUnitTests(unittest.TestCase):
    def test_active_repo_paths_only_returns_enabled_repos(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg = Path(tmp) / 'repos.json'
            cfg.write_text(json.dumps({
                'repos': [
                    {'path': 'foo/a', 'enabled': True, 'goals': []},
                    {'path': 'foo/b', 'enabled': False, 'goals': []},
                    {'path': 'foo/c', 'goals': []},
                ]
            }), encoding='utf-8')
            with patch.object(collector, 'CONFIG_PATH', cfg):
                self.assertEqual(collector.active_repo_paths(), ['foo/a', 'foo/c'])

    def test_load_repo_config_fails_fast_when_missing(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg = Path(tmp) / 'missing.json'
            with patch.object(collector, 'CONFIG_PATH', cfg):
                with self.assertRaises(FileNotFoundError):
                    collector.load_repo_config()


if __name__ == '__main__':
    unittest.main()
