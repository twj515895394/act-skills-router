# 路由表（解释性规则，无运行时引擎）

| 输入条件 | 选用模块 |
|---|---|
| 一般剧情表演 | acting-director → performance-qa |
| 抑制/爆发/情绪反转 | +emotion-director |
| 面部特写/眼神/哭戏特写 | +facial-performance |
| 走位/动作/手势/道具/无对白行动 | +body-performance |
| 台词/倾听/冲突对话/数字人口播 | +dialogue-acting |
| 现有成片质量诊断 | performance-qa + 被发现问题的责任模块 |

顺序：Acting → Emotion（可选）→ Facial/Body/Dialogue（必要者）→ QA。用户明确指定模块时，不必为了“完整性”调用所有模块。上游原件有互相引用，模块各自提供 required 和 conditional 文件清单；一次任务读取内容以需求为准，但不把正文摘要当成完整来源。

## 用户临时路由控制
允许用户说：“仅 facial-performance”、“开启 dialogue-acting、关闭 body-performance”、“跳过 QA”、“强制读取 Higgsfield 的完整 Acting 与 FACS 资料”。如果关闭模块会破坏基本时序，应提示风险但尊重选择。

## 集成
上游提供分镜与角色锁定条件，本 Skill 只输出表演层，不生成视频。传递下游：角色身份锚点 / 逐 beat 细节 / 负面约束 / 起止连续性 / 模型适配提醒。
