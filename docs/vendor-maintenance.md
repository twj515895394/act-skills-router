# 上游镜像维护

镜像目录属于本仓库单一 Skill 的内部参考内容，不是独立可安装 Skill。

`manifest.json` 记录 **44 个**上游文档、脚本和各自 LICENSE 的路径，原仓库保持其目录结构。

维护步骤：

```bash
python scripts/sync_upstreams.py --check
python scripts/sync_upstreams.py --sync --yes
git diff -- references/vendor
python scripts/sync_upstreams.py --check
```

同步使用上游 `main` 当前内容且会覆盖镜像文件，请先检查许可证、上游的新增依赖及接口变化再提交。**该脚本不自动发现新加入的上游文件**；若上游新增引用，应人工检查、更新 `manifest.json` 和模块依赖声明；不要将通过检查等同于完整依赖闭包验证。脚本不需要 MCP，仅更新文本与脚本资源，不自动执行上游代码。

当前镜像中的上游原文有些链接指向不在表演 Skill 范围的额外视频生产系统，保留为外部参考；不假装整个 Higgsfield、OmniAiLab 全仓已同步。
