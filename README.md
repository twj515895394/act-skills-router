# act-skills-router — 单个可安装的 Codex 表演 Skill

**一个路由 Skill，六个包内子能力，连同它们的上游原版参考文档和部分关联脚本一起维护。** 目标是个人 AI 剧情视频表演设计，不要求 MCP、API、ComfyUI 或某指定厂商。

## 现在的架构
```text
act-skills-router/
├── SKILL.md                   # Codex 只识别这一个入口
├── agents/openai.yaml
├── modules/                   # 6 个内部子能力（不是独立 SKILL.md）
│   ├── acting-director.md
│   ├── emotion-director.md
│   ├── facial-performance.md
│   ├── body-performance.md
│   ├── dialogue-acting.md
│   └── performance-qa.md
├── references/
│   ├── router/                # 路由、契约、冲突裁决
│   └── vendor/                # 上游原版内容/依赖/许可证/脚本
└── assets/performance-plan.md
```

## Codex 安装：个人全局（推荐）
在 **PowerShell** 中执行（Windows）：
```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
git clone https://github.com/twj515895394/act-skills-router.git "$HOME\.agents\skills\act-skills-router"
```
若安装目录已经存在，用 `git -C "$HOME\.agents\skills\act-skills-router" pull --ff-only` 升级。

Linux/macOS：
```bash
mkdir -p ~/.agents/skills
git clone https://github.com/twj515895394/act-skills-router.git ~/.agents/skills/act-skills-router
```
升级：`git -C ~/.agents/skills/act-skills-router pull --ff-only`。

确保文件路径为 `~/.agents/skills/act-skills-router/SKILL.md`，**不能多套一层目录**。在 Codex CLI 输入 `/skills`，或输入 `$act-skills-router` 点名调用。必要时重启 Codex。

在 Codex 中也可以请求内置 `$skill-installer` 从 GitHub 仓库安装本 Skill，但具体实现会随 Codex 版本变化，手动 clone 的路径最直观。

## 也可安装到单个项目
把整个 `act-skills-router` 目录置于该项目 `.agents/skills/act-skills-router/`，不要仅复制 `SKILL.md`，否则引用的 modules、references 和脚本会缺失。

## 测试
输入：“`$act-skills-router` 这段剧情中 A 在 0–3 秒怀疑 B，3–6 秒听到隐瞒的证据，6–10 秒试图保持冷静。设计克制表演，优先加载 Acting/Emotion/Facial，保留原台词并做生成前质检。”
核实：只出现一个可选 Skill；能读取包内 vendor 文档；情绪不会在 3 秒之前提前响应；QA 不声称见过视频。

## 开发与来源
上次的 7 个平铺 `skills/*/SKILL.md` 已由这一单入口结构取代。包内模块用于路由，原始资料的版权和许可证单独保留，详情见 `references/vendor/README.md`。现阶段仍属于“Agent 按文档执行的路由”，没有自动运行时管理或对视频效果的实测承诺。
