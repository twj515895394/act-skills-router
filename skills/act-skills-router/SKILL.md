---
name: act-skills-router
description: AI影视表演总导演与子Skill路由器。用于剧本、分镜、角色资料进入视频生成提示词之前，选择角色动机、情绪、脸部、身体、对白与质检模块，并输出逐镜表演指令。适用哭戏、对手戏、动作戏、无对白戏和角色连续性优化。
---

# Act Skills Router · 主表演调度

## 任务定位
只做“表演层”，不擅自重写剧情、不替代分镜镜头设计、不承诺视频生成。使用本仓库的子 Skill 工作：每个子 Skill 是标准 `SKILL.md`，可单独调用。读 `../../references/data-contract.md` 获取输入输出约定；路由参考 `../../config/routing.yaml`，以本文件为最终优先级。

## 输入采集
优先使用已有内容；缺省项可标为“待定”，不要为了缺少非关键参数停工。最少识别：`scene_id`、角色、剧情事实、画面/分镜、时长、台词、场景类型、输出目标。用户明示锁定项不可覆盖：台词原文、角色造型与身份、镜头时长、起止姿态、位置关系、视频模型限制。

## 动态路由
1. 凡剧情表演：先加载 `../acting-director/SKILL.md`，建立角色目标、阻力、策略与表演锚点。
2. 有情绪状态改变、克制或爆发：加载 `../emotion-director/SKILL.md`；无变化时不要硬造情绪高潮。
3. 面部特写、眼神、哭笑或面部质量问题：加载 `../facial-performance/SKILL.md`。
4. 有走位、身体动作、道具、格斗或肢体协调：加载 `../body-performance/SKILL.md`。
5. 有台词、旁白同步、对手戏、聆听或沉默应答：加载 `../dialogue-acting/SKILL.md`。
6. 最终交付前运行 `../performance-qa/SKILL.md` 做静态指令校验；有生成视频证据再做观察性 QA。针对纯概念讨论可跳过正式 QA。
7. 默认只读取命中的子 Skill；复杂任务先产一个共享节拍表，再让各模块对同一 beat_id 增补信息，绝不各自改写时间线。

## 调度依赖
`acting-director → emotion-director → (facial-performance / body-performance / dialogue-acting 可并行设计) → performance-qa`。依赖是逻辑顺序而非必须调用全部模块。

## 合并规则与冲突仲裁
- 事实优先级：用户锁定内容 > 剧本/镜头硬约束 > 主路由共享节拍 > 子 Skill 建议。
- 角色目标由 Acting 主导；情绪转折时间由 Emotion 主导；面部细节由 Facial 主导；走位由 Body 主导；实际台词与出声时机由 Dialogue 主导；QA 只能提出问题与修复提案，不能静默篡改事实。
- 一个 beat 使用同一 `beat_id`、起止时间和触发源。反应不得早于刺激；跨镜头必须承接眼线、手、道具、站位和情绪。
- “可观察行为”与“角色内在意图”分开写。无法有效生成的细节移入导演备注或 QA，而不是塞进一条超长提示词。
- 模块冲突时报告冲突位置、两种建议与选用依据；不隐藏歧义。
- 短镜头原则：优先 1 个主动作、至多 1–2 个显著转折；密集戏拆成多个 beat/镜头。

## 标准工作流程
1. Parse: 场景输入与约束，生成 `scene_context`。
2. Route: 列出选中/跳过的技能及依据。
3. Anchor: 表演档案 + 每角色的当前目标、阻碍、策略。
4. Beat: 统一时间轴；每个 beat 写明触发→意图→可见反应→结束状态。
5. Enrich: 由命中模块增补面部、身体、对白；保持时间点不变。
6. QA: 按“阻断/重要/建议”分级审查；修复后再查一次。
7. Deliver: 输出 `route_decision`、`character_performance_profile`、`beat_sheet`、`shot_performance_prompts`、`continuity_handoff`、`qa_report`。无视频时 `qa_report.mode=pre_generation`。

## 表演场景快捷路由
- 克制哭戏：Acting + Emotion + Facial + QA，若有台词再加 Dialogue。
- 对手戏/争吵：Acting + Emotion + Dialogue + Body + QA，若特写再加 Facial。
- 无对白：Acting + Body + Facial(有特写时) + Emotion(有转折时) + QA。
- 动作戏：Acting + Body + Emotion(需要时) + QA；危险动作只描述安全的影视呈现，不写现实伤害操作指南。
- 数字人口播：Acting + Dialogue + Facial(面部驱动时) + QA。

按 `../../templates/performance-plan.md` 输出结构；必要时只输出用户指定的部分。禁止将所有技能机械拼接为一个提示词。
