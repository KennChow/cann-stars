import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DashboardScopeTests(unittest.TestCase):
    def test_repos_json_only_contains_requested_repos(self):
        repos = json.loads((ROOT / 'data' / 'repos.json').read_text(encoding='utf-8'))
        paths = [repo['path'] for repo in repos]
        self.assertEqual(paths, ['cann/ge', 'cann/hixl', 'Ascend/torchair'])

    def test_collector_targets_only_requested_repos(self):
        collector = (ROOT / 'collector.py').read_text(encoding='utf-8')
        self.assertIn('TARGET_REPOS', collector)
        self.assertIn('cann/ge', collector)
        self.assertIn('cann/hixl', collector)
        self.assertIn('Ascend/torchair', collector)

    def test_dashboard_contains_operation_goals(self):
        html = (ROOT / 'index.html').read_text(encoding='utf-8')
        self.assertIn('运营目标', html)
        self.assertIn('2026年上半年达到700', html)
        self.assertIn('2026年上半年达到500', html)
        self.assertIn('2026年底达到1000', html)


if __name__ == '__main__':
    unittest.main()
