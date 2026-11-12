# 架构设计说明 v1

## 为什么采用多个标准 Skill
主 Skill 是编排层；每个子 Skill 有独立 `name`、`description` 和工作边界，既能组合，也可以独立调用。与“一个巨大的 Prompt”相比，减少无关规则加载和模块职责冲突。

## 依赖与职责
```text
用户/剧本/分镜
   ↓
act-skills-router 解析约束 → route_decision
   ↓
acting-director → 人物动机与共享行为锚点
   ↓
emotion-director（条件启用）→ 统一节拍/情绪触发
   ↓
facial-performance / body-performance / dialogue-acting（按需）
   ↓
performance-qa → 修复反馈至责任模块 → 交付
```
每个模块都使用 `references/data-contract.md` 的 `beat_id` 合并，而非生成独立的时间轴。分镜系统是上游，视频提示词系统是下游；本项目不干预镜头、场景资产和生成引擎。

## 决策表
- 剧情表演→Acting 必选；概念咨询可以单独选择专项 Skill。
- 情绪改变→Emotion；眼部/表情特写→Facial；走位/手/动作→Body；台词和聆听→Dialogue；完成设计后→QA。
- 可用 `config/routing.yaml` 的 profiles 做默认建议，再由用户在单次任务显式启用/关闭。
- 对于无对白但情绪变化的镜头，不强制 Dialogue；动作戏不能只做情绪和面部。

## 未来扩展接口
新的 Skill 只需遵守 `beat_id`、输入锁定、输出字段、边界和 QA 归属协议，可增加 `fight-performance`、`comedy-timing`、`crowd-acting`、`performance-to-prompt`，但不在 v1 中假装已有实现。真正的自动化配置读取、Schema 校验、模型适配器和 API 接入属于后续程序层开发。

## 安装说明
标准 Skill 的最小单位是一个包含 `SKILL.md`（YAML frontmatter 必含 name 和 description）的独立目录。某些客户端不会递归扫描任意仓库里的 `skills/`，应将七个 Skill 目录分别安装/软链到受支持的技能目录，或从可读取本仓库相对路径的工作区手动调用主入口。主 Skill 的相对路径以仓库当前布局为前提。

## 验收用例
1. 普通双人对白：加载 Acting + Dialogue + QA；如有冲突递进再加 Emotion。
2. 单人默戏：加载 Acting + Body + QA，含情绪转变则 Emotion。
3. 面部特写哭戏：加载 Acting + Emotion + Facial + QA；检查哭泣触发。
4. 打斗：加载 Acting + Body + QA；不自动增补台词。
5. 有真实视频再评：QA 切换 post_generation，引用可用帧/时间戳，不能编造观测。
6. 用户锁定台词：各模块不改词，超时只警告。
