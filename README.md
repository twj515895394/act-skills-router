# Act Skills Router

面向个人 AI 视频制作的 **1 个主 Skill + 6 个可独立调用的表演子 Skill**。无 MCP、无视频模型 API 依赖。所有产物可以直接用于剧本、分镜、Seedance/Kling/ComfyUI 等提示词准备阶段。

## 能力

| Skill | 负责什么 | 默认触发 |
|---|---|---|
| `act-skills-router` | 分析任务、选择技能、协调产物、冲突检测 | 用户请求表演设计 |
| `acting-director` | 目标、阻碍、策略、潜台词、角色表演档案 | 所有剧情表演 |
| `emotion-director` | 情绪因果、抵抗、触发、节拍与递进 | 有情绪变化 |
| `facial-performance` | 面部、眼神、微表情，必要时 AU 参考 | 表情特写 |
| `body-performance` | 姿态、重心、手势、走位及道具 | 有动作或走位 |
| `dialogue-acting` | 台词、停顿、呼吸、聆听、对手戏 | 有对白 |
| `performance-qa` | 指令一致性、可生成性、成片观察与修复 | 交付前/视频生成后 |

## 目录

```text
skills/
  act-skills-router/SKILL.md        # 主入口
  acting-director/SKILL.md
  emotion-director/SKILL.md
  facial-performance/SKILL.md
  body-performance/SKILL.md
  dialogue-acting/SKILL.md
  performance-qa/SKILL.md
config/
  routing.yaml                      # 可编辑路由策略（说明性配置，非自动执行器）
references/
  data-contract.md                  # 统一数据约定
  sources-and-licenses.md           # 参考来源与许可证
templates/
  performance-plan.md               # 可复制产物模板
examples/
  confrontation.md                   # 双人冲突示例
docs/
  architecture.md                    # 架构、运行规则和扩展
```

## 使用方法

将整个仓库放在 Agent 能读取的工作空间，并按客户端的标准 Skill 发现机制安装 `skills/` 下的技能。**不能假设客户端会因为仓库内存在嵌套目录而自动发现所有 Skill**；如使用 Codex，可将每个子目录链接/复制到其 Skills 搜索目录。单独安装主 Skill 时，应把本仓库保持在可访问的相对路径，否则它无法读取子 Skill。

对支持仓库内 Skill 发现的客户端，直接调用 `act-skills-router`；否则先让 Agent 读取 `skills/act-skills-router/SKILL.md`。

示例任务：
- “用 act-skills-router 设计这段 12 秒冲突戏的表演，输出每 2 秒的情绪和动作。”
- “只使用 facial-performance，优化这段克制哭戏的面部表演。”
- “用 dialogue-acting + performance-qa，检查这段双人对白。”

## 重要边界
- 主 Skill 的路由为 **Agent 根据文档执行的逻辑**；`config/routing.yaml` 是人可读策略，不是已经实现的自动运行时代码。
- 不修改原台词、不伪造视频生成结果；长镜头复杂动作应拆段；FACS AU 是描述性提示，不代表生成模型可精确执行。
- 参考项目并非被作为源码原样打包；这里是新的统一实现。详见 `references/sources-and-licenses.md`。
