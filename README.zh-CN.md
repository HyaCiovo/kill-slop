# Kill Slop

[English documentation](README.md)

一个中英双语的 Agent Skill，用于新建、审查和改造官网与营销落地页。它把受众、场景、证据、转化、移动端阅读和交付质量放在模板与装饰效果之前。

## 为什么需要这个 Skill

- **决策先于装饰**：先确认页面类型和唯一主转化动作，再选择视觉。
- **证据先于承诺**：使用真实产品界面、可验证案例、第三方背书和有口径的数据。
- **明确取舍**：删除重复、重排不合理结构、重做不匹配的区域，而不是畏手畏脚地逐字修补。
- **移动端独立设计**：对同类功能分层，同时保留手动滚动、触摸操作和可读字号。
- **内容保护**：不擅自修改用户提供的法律条款、技术限制、安全边界或合同承诺。
- **真实验收**：检查桌面和移动端的实际交互，而不只检查代码或静态截图。

## 语言版本

英文和中文版本是两个独立可安装的 Skill，引用结构保持一致。

| 语言 | Skill | 路径 |
|---|---|---|
| English | `kill-slop` | [`skills/kill-slop`](skills/kill-slop) |
| 中文 | `kill-slop-zh` | [`skills/kill-slop-zh`](skills/kill-slop-zh) |

每个版本都包含精简的 `SKILL.md` 路由和五份按需读取的参考文件：

- `strategy.md`：受众、转化、文案和信息架构。
- `evidence.md`：真实证据、第三方背书和证据缺口。
- `visual.md`：设计 token、组件、动效、素材授权和性能。
- `interaction.md`：移动端、可访问性、交互状态、SEO 和交付。
- `review.md`：审查输出和 agent 自检清单。

## 安装

仓库地址：[github.com/HyaCiovo/kill-slop](https://github.com/HyaCiovo/kill-slop)。

### Skills CLI

```bash
npx skills add HyaCiovo/kill-slop --list
npx skills add HyaCiovo/kill-slop
```

出现选择提示时，英文选择 `kill-slop`，中文选择 `kill-slop-zh`。

### 手动安装

克隆仓库，然后把所需语言的整个目录复制到 Agent 支持的 Skills 目录：

```bash
git clone https://github.com/HyaCiovo/kill-slop.git
```

具体 Skills 目录请查阅对应 Agent 的文档。每个语言版本都包含完整的 `references/` 目录，可以独立使用。

## 使用示例

```text
审查这个落地页，只报告转化问题、证据缺口和移动端阅读问题，不修改文件。
```

```text
重做移动端功能展示区，让切换控件和对应内容尽量同屏。保留全部技术限制和事实信息。
```

```text
为一个科研数据平台新建落地页。先确定受众、预约演示这个主 CTA、现有证据和移动端策略。
```

## 仓库结构

```text
.
├── skills/
│   ├── kill-slop/       # English skill
│   └── kill-slop-zh/    # 中文 Skill
├── scripts/validate.py           # 无第三方依赖的仓库校验
├── .github/workflows/validate.yml
├── CONTRIBUTING.md
├── CONTRIBUTING.zh-CN.md
├── README.md
├── README.zh-CN.md
└── LICENSE
```

## 本地开发

需要 Python 3.9 或更高版本，无需安装第三方包。

```bash
python3 scripts/validate.py
```

校验脚本检查两个语言版本、必需引用文件、frontmatter、相对链接和结构一致性。

## 参与贡献

阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 或[贡献指南](CONTRIBUTING.zh-CN.md)。优先提交范围小、容易审查的改进。新增文案模式规则时，需要同时提供一个确实需要修改的示例和一个不应修改的保护示例。

## 致谢

部分语境判断和事实保护思路参考了 [unslop](https://github.com/theclaymethod/unslop)。本仓库不包含 unslop 的扫描器、评测或代码。

对 shadcn/ui、Base UI、ReactBits、Motion、GSAP 和 Pexels 的引用仅用于实现与授权建议，不代表这些项目对本仓库的认可。

## 许可证

基于 [MIT 许可证](LICENSE)发布。
