# 表演设计数据契约 v1

本项目以 Markdown 为交付格式，字段名用于不同 Skill 对齐；未实现任何强制 JSON Schema 校验器。

## 场景上下文
`scene_context`:
- `scene_id`, `shot_id`, `duration_seconds`, `cast`, `story_facts`
- `dialogue_exact`（原文及说话人）、`shot_constraints`（景别、镜头等）、`model_target`（可空）
- `locked_constraints`（用户明确锁定项）
- `evidence`（剧本文本、分镜图、视频帧、主观反馈及来源）

## 路由决策
`route_decision`: `selected_skills[]`, `skipped_skills[]`, `why`, `overrides`。

## 角色档案
`character_performance_profile`: `character_id`, `stable_traits`, `body_rhythm`, `eye_habit`, `voice_identity`, `pressure_trigger`, `mask_crack`, `scene_goal`, `obstacle`, `tactic`, `subtext`。

## 共享节拍
`beat_sheet[]`: `beat_id`, `start_seconds`, `end_seconds`, `trigger`, `actor_goal`, `tactic`, `emotion_in`, `emotion_out`, `reaction_latency`, `face_cues`, `body_cues`, `line_exact`, `listener_action`, `end_state`, `locks`。
- beat 必须不重叠或明确声明可重叠的不同角色轨道；时间总范围必须在镜头时长内。
- 同一 `beat_id` 的情绪/脸/身体/对白共享一段时间，不能各自建立独立绝对时间。
- `trigger` 需可追溯到剧情或画面事实；没有触发时使用 `none`，不虚构。
- 输出 `shot_performance_prompts` 时，只把视频模型容易观察和执行的动作写入提示词；导演内心动机保留在备注。

## 连续性
`continuity_handoff`: `shot_id`, `character_id`, `entry_state`, `exit_state`, `eye_line`, `hand_occupancy`, `prop_ownership`, `position`, `emotional_carryover`。

## QA
`qa_report`: `mode=pre_generation|post_generation`, `evidence_available`, `issues[]`, `recheck_status`。每条 issue 参见 `performance-qa`。不可把生成前 QA 写成“视频真实效果评分”。

## 优先级
用户锁定 > 脚本与分镜约束 > 共享节拍事实 > 子技能可调整建议。冲突先显式记录后选择最小变更。
