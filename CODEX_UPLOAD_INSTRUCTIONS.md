# CODEX_UPLOAD_INSTRUCTIONS.md

## 任务

请将本文件夹完整上传到 GitHub。

### GitHub 账号
`xingchenyd`

### 仓库名称
`数学建模工作流`

### 默认分支
`main`

### 建议可见性
Public

## 上传要求

1. 保留当前目录结构，不要把所有 Markdown 文件摊平。
2. 根目录必须保留 README、SKILL、AGENTS、START_HERE、MASTER_ROUTER、M0-M7、LICENSE、CHANGELOG、CONTRIBUTING、CITATION。
3. 保留 `.github/`、`branches/`、`docs/`、`templates/`。
4. 不上传缓存、临时文件或无关运行产物。
5. 不修改 V4.3.3 的规则内容，除非只是修复明显链接/路径错误。
6. 若仓库已存在：先拉取远端并保留 Git 历史，再用本包更新。
7. 若仓库不存在：创建仓库并以 `main` 为默认分支。
8. 建议提交信息：
   `release: 数学建模工作流 V4.3.3 湖南赛区定制版`
9. 上传后检查 README、SKILL、MASTER_ROUTER、M0-M7 和各子目录是否都能正常访问。
10. 不要上传具体竞赛赛题、参赛论文、个人身份信息或私密数据。

## 仓库定位

这是面向数学建模竞赛的 AI Workflow / Skill，主流程为：

`M0 → M1 → M2 → (M3 ↔ M4) → M5 → M6 → M7`

包含：
- 题意与数据取证
- Pitfall / Wrong-Path Analysis
- Modeling Eligibility Gate
- Baseline / Bound / Search Space Engineering
- 求解与优化
- 独立 Validator
- 消融、收敛、稳定性、敏感性
- 逐节论文工程
- 真实参考文献与正文 `[n]` 引用
- 湖南赛区 2026 提交规则
- LaTeX-native PDF 规范
- 答辩与评委审查
