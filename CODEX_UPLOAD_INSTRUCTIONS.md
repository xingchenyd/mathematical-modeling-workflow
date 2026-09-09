# CODEX_UPLOAD_INSTRUCTIONS.md

## Goal

Upload this package to GitHub and keep it installable as an Agent Skill.

- GitHub account: `xingchenyd`
- Repository name: `数学建模工作流`
- Default branch: `main`
- Suggested visibility: Public
- Suggested commit: `release: V4.6 Skill化与出版级可视化版`

## Important

The GitHub repository may keep the Chinese repository name. For Agent Skills installation, copy/clone the contents into a local folder named exactly:

`mathematical-modeling-workflow`

because the Agent Skills specification requires the directory name to match the `name` in `SKILL.md`.

## Before push

Run:

```bash
python scripts/validate_skill.py .
pytest -q
python scripts/build_visual_gallery.py
python scripts/build_sklearn_gallery.py
```

All tests must pass.

## Do not

- flatten `references/`, `assets/`, `scripts/`, or `tests/`;
- delete B1–B5 branches;
- replace `SKILL.md` with a long combined manual;
- upload current contest-specific data, answers, team identity, or private files.
