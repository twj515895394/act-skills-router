# Emotion Director（包内子能力）

**触发**：情绪发生转变、克制、爆发、哭戏、复杂表里不一或跨镜头情绪承接。

## 必须读取：完整原始资料
- `../references/vendor/act-skill/skills/direct-ai-actor-performance/SKILL.md`
- `../references/vendor/omniailab/references/EMOTION SKILL.md`
- `../references/vendor/act-skill/knowledge-base/情绪/情绪表演知识库-v1.md`

## 关联资料
- `../references/vendor/act-skill/skills/direct-ai-actor-performance/references/emotion-retrieval.md`
- `../references/vendor/omniailab/references/emotion_curve.md`
- `../references/vendor/omniailab/references/shot-emotion-engine.md`
- `../references/vendor/omniailab/references/performance-palette.md`
- 需检索情绪库时可用 `../references/vendor/act-skill/skills/direct-ai-actor-performance/scripts/search_emotion_library.py`（先检查脚本实际路径参数，默认不自动执行）。
- 需检查时间轴时可用 `../references/vendor/act-skill/skills/direct-ai-actor-performance/scripts/validate_timeline.py`（输入格式须符合上游约定）。

## 输出
同一个共享 `beat_id` 的触发源、角色解读、克制/泄漏、强度起止、反应延迟、可见情绪信号以及禁止提前出现的表演。情绪强度 0–5 是策划标尺，不代表所有视频模型支持精确数值控制。
