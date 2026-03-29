# CANN GitCode 数据分析

对 [gitcode.com/cann](https://gitcode.com/cann) 组织下所有仓库的 Star 用户群体进行数据采集与可视化分析，帮助了解 CANN 社区的用户构成与参与深度。

## 功能概览

- **组织概览**：仓库 Star / Fork / Issue 数量、全组织 Star 用户类型分布、各仓库非开发者占比、Star 数分布、多仓库 Star 用户统计
- **仓库详情**：切换单个仓库，查看用户类型饼图、Star 时间分布、各类用户 Star 时间对比、可筛选的用户列表

## 用户分类标准

| 类型 | 判断依据 |
|------|----------|
| **贡献者** | 在 CANN 任意仓库提交过 MR/PR |
| **提问者** | 在 CANN 任意仓库提过 Issue，无 MR |
| **开发者** | 在 GitCode 有贡献活动（年贡献 ≥ 1），但无 CANN 特定 MR/Issue |
| **Star 爱好者** | 无贡献活动，Star 了多个 CANN 仓库 |
| **铁粉** | 无贡献活动，只 Star 了某一个 CANN 仓库 |

## 数据采集

```bash
# 依次执行所有采集步骤
python collector.py all

# 或分步执行
python collector.py repos        # 采集仓库基本信息
python collector.py stars        # 采集各仓库 Star 用户列表
python collector.py users        # 采集用户画像（贡献数、仓库数等）
python collector.py activities   # 采集各仓库 MR / Issue 作者
python collector.py reclassify   # 重新分类（更新 activity 数据后执行）
python collector.py report       # 输出文字报告
```

**环境要求**：Python 3.8+，无需第三方依赖。

## 本地预览

```bash
python -m http.server 8080
# 浏览器打开 http://localhost:8080
```

## 免责声明

- 本项目仅用于**学习、研究与社区分析**目的，不用于任何商业用途。
- 所有数据均来源于 [gitcode.com](https://gitcode.com) 的公开页面与公开 API，未涉及任何需要登录授权才能访问的私有数据。
- 数据采集遵循合理频率限制（请求间隔 ≥ 0.2 秒），不对目标服务器造成额外负担。
- 本项目展示的用户分类（贡献者、提问者等）基于公开行为数据的统计推断，**不代表对任何个人的评价**，仅供参考。
- 如相关数据涉及隐私问题或违反平台使用条款，请联系作者删除。
