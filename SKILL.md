---
name: act-skills-router
description: AI视频表演总导演与单入口路由Skill。把剧本/分镜转换为角色动机、情绪节拍、面部眼神、身体动作、对白对手戏和表演质检；按需加载内置的6个子能力及其完整关联参考资料，适用于Seedance、Kling、ComfyUI等AI影视流程。
---

# Act Skills Router — 单入口表演系统

**本仓库的顶层 `SKILL.md` 是唯一可安装入口。** 六个子能力是包内 `modules/*.md` 文件，**不是六个独立安装的 Skill**。它们可以被主路由调度；也允许用户点名要求主路由只执行某一模块。

## 硬性工作约定
- 开始先读 `references/router/routing.md` 和 `references/router/contracts.md`；根据任务场景只加载命中的 `modules/*.md`。
- **模块说明不是替代原始上游 Skill**：每个模块列明必须按需读取的完整镜像文件（`references/vendor/...`）。用户要求“充分使用上游能力”时，必须打开对应原版正文及其关联参考，不得仅凭模块概述执行。
- 上游引用的路径相对于其镜像文件位置读取。不同来源的冲突按本文和 `references/router/conflict-rules.md` 仲裁；外部服务/API/平台特定说明为可选能力，不作为离线表演规划前置条件。
- 默认 `acting-director` 建角色意图锚点，`emotion-director` 处理有触发的情绪转折，按需加脸、身体、对白，最后 `performance-qa` 做生成前检查；不要机械全选。
- 用户约束（台词、参考人物、角色外观、分镜、镜头时长与模型）优先级最高；所有子能力共用 `beat_id`、时间区间与镜头连续性。
- 对生成前设计只报告 **pre_generation QA**，没有生成视频不得声称实测清晰度、口型或表演效果。
- 本 Skill **无 MCP 和视频生成 API 依赖**；原上游文档可能描述某模型专用流程，应在提示词转换前进行能力匹配，不可擅自假定用户在使用该平台。

## 路由执行
1. **Scene input**：固定剧情事实、角色、台词、镜头时长、景别、动作与锁定条件；缺失字段标 `unknown`，能继续则继续。
2. **Route**：查看 `references/router/routing.md` 选择子模块并说明原因；若用户指定子模块优先遵守。
3. **Read source**：先读选中的 `modules/<name>.md`，再读其 `required` 原版文件和任务命中的 `conditional` 关联资料。长参考用分段读取，**但不能假装没读过的内容已经研究**。
4. **Character anchor**：Actor 的角色目标、障碍、策略、潜台词、行为锚点；从原版角色 master profile 方法借鉴稳定表演档案。
5. **Shared beat sheet**：只有一个时序真源；情绪、脸、身体、声音都以同一时间段和触发事件设计，不得提前反应。
6. **Merge & QA**：对来源建议做术语映射、消除矛盾与生成能力过滤；阻断问题交回负责模块修正。
7. **Deliver**：输出角色表演档案、启用子模块、节拍表、分镜表演提示词、跨镜连续性记录以及带证据分级的 QA。

## 子模块
- `modules/acting-director.md`：角色目标 / 压力下行为 / 潜台词 / master profile。
- `modules/emotion-director.md`：情绪触发 / 双层状态 / 抵抗 / 时序。
- `modules/facial-performance.md`：眼神任务 / 微表情 / FACS AU 可选标注。
- `modules/body-performance.md`：姿态 / 道具 / 重心 / 空间距离 / 走位。
- `modules/dialogue-acting.md`：台词、停顿、倾听、对手戏和音画同步。
- `modules/performance-qa.md`：文本 QA / 成片 QA 分离、最小修复策略。

输出模板：`assets/performance-plan.md`；上游镜像文件及版权：`references/vendor/README.md`。
