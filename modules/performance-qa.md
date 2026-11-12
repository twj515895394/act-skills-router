# Performance QA（包内子能力）

**触发**：生成前交付审查、已生成视频表演质量诊断、表演提示词失败修复。

## 必须读取：完整原始资料
- `../references/vendor/performance-direction/skills/production/creative-direction/performance-direction/SKILL.md` 的 validation / iterate / QA 段落。
- `../references/vendor/performance-direction/skills/production/creative-direction/performance-direction/EVAL.md`
- `../references/vendor/higgsfield/skills/higgsfield-acting/SKILL.md` 中 bad acting atlas / check。
- `../references/vendor/omniailab/references/generation-guardrails.md`

## 关联资料
- `../references/vendor/higgsfield/skills/higgsfield-seedance/FAILURE-MODES.md`
- `../references/vendor/act-skill/skills/direct-ai-actor-performance/scripts/validate_timeline.py`
- `../references/vendor/omniailab/references/seedance-production.md`

## 双模式
1. `pre_generation`：静态检查事实/台词锁定、反应时序、可生成动作量、角色与道具一致性；不声称实际视频已经通过 QA。
2. `post_generation`：必须收到帧/视频或用户标明的错误观察，逐条定位时间与证据；不可从提示词幻想结果。

输出阻断(blocker)、重要(major)、建议(minor)，对每项说明证据、根因、责任模块、最小修复和复查结果。优先修最小失败层，不要一出问题就重写整个镜头。
