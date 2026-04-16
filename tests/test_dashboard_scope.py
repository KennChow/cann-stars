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

    def test_dashboard_uses_d_level_labels_and_meaning_text(self):
        html = (ROOT / 'index.html').read_text(encoding='utf-8')
        self.assertIn('D0 关注者', html)
        self.assertIn('D1 贡献者', html)
        self.assertIn('D2 PR贡献者', html)
        self.assertIn('Star / Watch / Fork 仓库', html)
        self.assertIn('提交 Issue / 评论 issue / 提交 PR', html)
        self.assertIn('至少合入了 1 个 PR', html)

    def test_dlevel_summary_contains_expected_structure(self):
        summary = json.loads((ROOT / 'data' / 'dlevel_summary.json').read_text(encoding='utf-8'))
        self.assertEqual(sorted(summary['global_counts'].keys()), ['d0', 'd1', 'd2', 'total'])
        self.assertEqual(sorted(summary['repo_counts'].keys()), ['Ascend/torchair', 'cann/ge', 'cann/hixl'])
        self.assertIn('repo_users', summary)
        self.assertIn('star_timeline', summary)


if __name__ == '__main__':
    unittest.main()
