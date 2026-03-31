# RMTDataPro 文档

本目录包含 RMTDataPro 软件的 Sphinx 文档源码。

## 在线文档

访问 [RMTDataPro 在线文档](https://emwpj.github.io/RMTDataPro-docs) 获取最新文档。

## 本地构建

```bash
# 安装依赖
pip install -r requirements.txt

# 构建 HTML 文档
sphinx-build -b html source _build/html

# 预览文档
cd _build/html && python -m http.server 8000
```

## 文档结构

```
source/
├── intro/          # 入门指南
├── chapters/       # 核心章节
├── gallery/        # 实例展示
├── tutorial/       # 高级教程
├── appendices/     # 附录 A-F
└── appendix/      # 其他附录
```

## 贡献指南

欢迎贡献文档！请参阅 [贡献指南](source/appendix/contributing.md)。

---

**最后更新**: 2026年3月
**版本**: v0.1.0
