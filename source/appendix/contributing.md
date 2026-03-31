# 贡献指南

感谢您对 RMTDataPro 文档的贡献！本文档介绍如何参与文档改进。

## 🤝 贡献方式

### 1. 文档纠错

发现文档中的错误时，欢迎提交纠正：

- 拼写错误
- 事实错误
- 表述不清
- 代码示例错误

### 2. 内容完善

补充或扩展现有内容：

- 添加遗漏的步骤
- 补充更多示例
- 完善参数说明
- 丰富故障排除指南

### 3. 翻译贡献

帮助翻译文档到其他语言：

- 英文翻译
- 其他语言翻译

## 📝 提交流程

### 1. Fork 仓库

访问 [RMTDataPro 文档仓库](https://github.com/EMWPJ/RMTDataPro-docs)，点击 Fork 按钮。

### 2. 克隆本地

```bash
git clone https://github.com/你的用户名/RMTDataPro-docs.git
cd RMTDataPro-docs
```

### 3. 创建分支

```bash
git checkout -b docs/你的修改内容
```

### 4. 修改文档

使用 Markdown 编辑器修改 `.md` 文件。

### 5. 提交更改

```bash
git add .
git commit -m "docs: 简要描述你的修改"
git push origin docs/你的修改内容
```

### 6. 创建 Pull Request

在 GitHub 上创建 PR，描述你的修改内容和原因。

## 📋 编写规范

### 文件命名

- 使用小写字母和连字符
- 示例: `new-feature.md`, `quick-start.md`

### 标题层级

```markdown
# 一级标题（页面标题，只有一个）
## 二级标题（章节）
### 三级标题（子章节）
#### 四级标题（较少使用）
```

### 中文排版

- 中文与英文/数字之间加空格
- 正确: `RMTDataPro v0.1.0`
- 错误: `RMTDataProv0.1.0`
- 使用中文标点符号
- 专有名词使用官方翻译

### 代码块

````markdown
```语言
代码内容
```
````

### 表格

使用 Markdown 表格，保持列对齐。

### 图片

- 图片放在 `source/_static/images/` 目录
- 使用相对路径引用
- 添加 alt 文本描述

## ✅ 检查清单

提交前请确认：

- [ ] 内容准确无误
- [ ] 格式符合规范
- [ ] 链接有效
- [ ] 无错别字
- [ ] 测试文档构建

## 🧪 本地测试

构建文档并检查：

```bash
pip install -r requirements.txt
sphinx-build -b html source _build/html
```

## 📧 联系

如有 questions，请联系维护者或提交 Issue。

## 📄 许可证

贡献的内容将采用与项目相同的许可证发布。

---

**返回**: [文档索引](../index)
