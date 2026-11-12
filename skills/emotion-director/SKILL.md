---
name: emotion-director
description: 设计表演情绪因果、克制与爆发、转折触发、情绪强度和可观察的时间节拍，适合哭戏、紧张、冲突、惊讶与复杂情绪层次。
---

# Emotion Director
**边界：** 情绪是角色行动的结果，不将情绪词堆满提示词；不能新增剧情事件。

## 工作步骤
1. 从 Acting 的目标、阻力和事件抽取情绪起点及想隐藏的东西。
2. 每个转折标注 `trigger`（刺激原文/动作及发生时间），`appraisal`（角色如何理解），`resistance`（如何控制），`leak`（失控泄露迹象），`new_state`。
3. 定义强度 0–5：0 近中性、1 极细微、2 自然、3 明确可读、4 高强度、5 风格化夸张；这是设计尺而非生成模型参数。
4. 标出抑制→松动→失控或其他合乎情境的非线性情绪曲线；不要每次都线性升级。
5. 为每个 beat 保留起止状态、时长及触发延迟。禁止“先哭再被告知坏消息”。
6. 给 Facial、Body、Dialogue 分别输出优先可观察信号，避免同时让脸、手、声音都夸张。
7. 在短镜头里以一个主要转折为佳，复杂情绪用跨镜头承接。

## 输出字段
`beat_id, time_range, trigger, felt_state, displayed_state, resistance, intensity_in, intensity_out, reaction_latency, visible_cues, forbidden_premature_reaction`。

## 质量门槛
无触发的强烈情绪不得通过；矛盾情绪可保留但须解释“外表克制 vs 内心波动”；无对白戏优先眼线、呼吸、身体停顿表现。
