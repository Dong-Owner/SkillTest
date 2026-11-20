---
name: word-count-demo
description: 用于测试 Skill 加载和脚本执行，统计 UTF-8 文本文件的行数、词数和字符数。
---

# 文本统计 Demo

使用 Python 3 运行本目录下的 `scripts/count_text.py`，将用户指定的文件路径作为参数。用户要求试跑示例时，使用本目录下的 `assets/sample.txt`。

脚本输出 JSON。将其中的行数、词数和字符数告诉用户。词按空白字符分隔，字符数包含换行符。