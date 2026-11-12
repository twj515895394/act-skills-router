# 上游资料镜像（vendored references）

这是随单一 Skill 安装的**原版参考资料副本**，不是 6 个独立可安装的 Skill。原始版权属于各上游作者；保留每个来源的 LICENSE 和原始相对目录，以便维持大部分内部引用关系。本仓库不宣称拥有上游的所有附属工具及生态。

| 镜像目录 | 原仓库 | 导入范围 |
|---|---|---|
| higgsfield/ | https://github.com/OSideMedia/higgsfield-ai-prompt-skill | acting、facs、seedance/scene/character/audio 关联规则、shared、模板 |
| act-skill/ | https://github.com/yuyolin/act-skill | direct-ai-actor-performance 原版、4 references、2 Python scripts、Markdown 情绪库 |
| performance-direction/ | https://github.com/calesthio/generative-media-skills | 表演 Skill、EVAL |
| dialogue/ | https://github.com/nolanx-ai/nolanx.ai | dialogue-performance-blocking |
| omniailab/ | https://github.com/tomatoparkdao/omniailab-ai-director | ACTING/EMOTION 原版和关联生成护栏/情绪/制作资料 |
| acting-system/ | https://github.com/zlbigger/story-video-director | ACTING SYSTEM 参考全文 |

每个上游源码与资料均为 MIT 授权，镜像目录的 `LICENSE` 保留原文及版权声明。上述文件是按表演核心依赖复制的 **selected snapshot**，不代表整仓库镜像。部分外部引用继续指向上游资源，例如广泛的视频生成技能及模型能力数据库；运行无需联网，但需要这些扩展资料时再自行检查来源。引用与来源归属不会因为本仓库重新包装而改变。

上游镜像须按其版本/变更记录维护；不建议直接手工修改镜像原文件。修改调度策略请编辑 `modules/`、`references/router/`。升级原版时同步复查关联依赖并运行完整路径与许可证审查。
