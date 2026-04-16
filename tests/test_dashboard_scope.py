import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DashboardScopeTests(unittest.TestCase):
    def test_repo_config_contains_requested_repos_and_goals(self):
        cfg = json.loads((ROOT / 'config' / 'repos.json').read_text(encoding='utf-8'))
        repos = cfg['repos']
        enabled_paths = [repo['path'] for repo in repos if repo.get('enabled', True)]
        self.assertEqual(enabled_paths, ['cann/ge', 'cann/hixl', 'Ascend/torchair'])
        goals = {repo['path']: repo['goals'] for repo in repos}
        self.assertEqual(goals['cann/ge'][0]['target'], 500)
        self.assertEqual(goals['cann/ge'][1]['target'], 1000)
        self.assertEqual(goals['cann/hixl'][0]['target'], 700)
        self.assertEqual(goals['Ascend/torchair'][0]['target'], 700)

    def test_repos_json_only_contains_requested_repos(self):
        repos = json.loads((ROOT / 'data' / 'repos.json').read_text(encoding='utf-8'))
        paths = [repo['path'] for repo in repos]
        self.assertEqual(paths, ['cann/ge', 'cann/hixl', 'Ascend/torchair'])

    def test_collector_uses_config_file_for_repo_scope(self):
        collector = (ROOT / 'collector.py').read_text(encoding='utf-8')
        self.assertIn('config/repos.json', collector)
        self.assertIn('load_repo_config', collector)
        self.assertIn('active_repo_paths', collector)

    def test_dashboard_reads_goals_from_config_data_not_hardcoded_constant(self):
        html = (ROOT / 'index.html').read_text(encoding='utf-8')
        self.assertIn("loadJSON('config/repos.json')", html)
        self.assertNotIn('const REPO_GOALS = {', html)
        self.assertIn('repoConfigMap', html)
        self.assertIn('运营目标', html)

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
