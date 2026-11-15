# 可选的对比视频与 Story video

只有在需要录制证据或分享改造过程时才使用视频。选择两种模式之一：

- **对比视频**：录制同一真实交互在修改前后的表现。
- **Story video**：方形、约十秒的展示视频，让同一界面经过几个可见的设计阶段逐步完成改造。

静态文案、间距或颜色修改优先使用截图。除非用户要求录制或当前任务确实需要，否则不安装 Playwright、浏览器或 FFmpeg。

## 1. 准备工具

优先复用项目依赖和已安装工具。如果需要录制但工具缺失，说明将安装什么以及用途：

```bash
# 添加开发依赖时使用项目自己的包管理器。
npm install --save-dev playwright
npx playwright install chromium

# 检查视频编码工具是否可用。
ffmpeg -version
```

缺少 FFmpeg 时，在确认安装后使用操作系统的正常包管理器，例如 macOS 的 `brew install ffmpeg`。不要使用 sudo，也不要为了审查任务修改生产依赖。

产物放在 `artifacts/`。除非用户明确需要发布示例，否则不提交。不得暴露凭据、私有客户数据或个人信息。

## 2. 录制公平的对比

修改前后使用相同路由、语言、viewport、设备缩放、数据、初始状态和操作顺序。等待字体、图片和相关状态就绪。静态对比使用减少动态效果模式；审查动效时，两边保持相同设置。

根据项目创建临时 Playwright 脚本：

```ts
import { chromium } from "playwright";

const browser = await chromium.launch();
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  recordVideo: {
    dir: "artifacts/design-comparison/raw",
    size: { width: 1440, height: 900 },
  },
});
const page = await context.newPage();
await page.goto("http://127.0.0.1:3000", { waitUntil: "networkidle" });
await page.evaluate(() => document.fonts.ready);
// 使用真实、基于角色的定位器执行场景。
await context.close();
await browser.close();
```

用同一场景分别生成 `before.webm` 和 `after.webm`。移动端使用真实触摸和移动端上下文，而不只是缩小桌面 viewport。

## 3. 使用 FFmpeg 合成对比

两次录制尺寸一致时，将修改前放在左侧、修改后放在右侧：

```bash
ffmpeg \
  -i artifacts/design-comparison/before.webm \
  -i artifacts/design-comparison/after.webm \
  -filter_complex "[0:v]fps=30,scale=1440:900,setsar=1[a];[1:v]fps=30,scale=1440:900,setsar=1[b];[a][b]hstack=inputs=2[v]" \
  -map "[v]" -c:v libx264 -pix_fmt yuv420p -movflags +faststart \
  artifacts/design-comparison/comparison.mp4
```

根据实际录制尺寸调整 scale。不要为了让视频看起来更大而放大低质量录制。

## 4. 制作 Story video

Story video 方法改编自 Damir Sokolovsky 的 [unslop](https://github.com/heydamir/unslop)，采用 CC BY 4.0。使用此流程制作的视频保留小型 `unslop by @heydamir` 署名，并保留 `NOTICE` 中的来源说明。

### 故事结构

- 使用独立的 `artifacts/story/story.html`，包含原始界面和样式。不要为了展示修改正式页面。
- 使用三至五个可见阶段，例如间距、颜色与图标、字体与文案、细节。通过 `<meta name="kill-slop-steps" content="Spacing, Color and icons, Type and copy, Details">` 列出阶段。
- 累加 `.s1`、`.s2`、`.s3` 等阶段类。每个阶段只在同一 DOM 上修改表现值，让旧状态原地变形为新状态。
- 从左上开始错开少量时间，让变化形成波浪，而不是整屏切换。
- 画面只保留界面及其自身背景，不添加外层窗口、卡片、边框或阴影。
- 使用方形构图，靠近变化最明显的区域，总时长控制在约十秒以内。

### 变形规则

- 原地改变 padding、gap、尺寸、颜色、圆角和阴影，不替换页面或重建 DOM。
- 渐变、发光和洗底放在独立层上淡出，同时改变底层纯色。
- 需要变形的胶囊圆角使用明确像素值，不使用 `9999px`。
- 只对确实变化的文字进行滚动或模糊切换，每个故事最多八处。字号、字重、字距和颜色变化直接过渡，不需要文字替换。
- 替换图标在同一容器内交叉淡入淡出。移除的装饰元素收起，新增的有意义元素淡入，并预留空间避免跳动。
- Story 页面使用固定展示尺寸，不依赖 `100vh`。

### 红线与镜头

- 开头用一小段红线标出最清楚的 slop，最多五个短标签。
- 在四至六个有意义的间距上显示实时测量值，不要覆盖每一行。测量线跟随元素，并从旧值更新到新值。
- 选择两至四个圆角变化明显的元素，显示轮廓和半径值。
- 使用 `<meta name="kill-slop-frame" content="0 0 960">` 以页面坐标定义镜头，依次表示 x、y 和宽度。指向界面左上角，并保证手机上能看清。
- 如果窗口变宽，将其锚定左侧，让它向右扩展而不是横向漂移。

### 录制 Story

使用 Playwright 加载 Story 文件，按顺序添加阶段类，并等待每段过渡完成。录制为 WebM，再用 FFmpeg 裁切或缩放为方形，并使用 H.264、`yuv420p` 和 fast-start 输出 MP4。不要在录制时下载或执行未经审查的远程渲染器。

Story 文件只是展示产物。正式结果仍使用项目自身技术栈交付，不携带 Story 类名、测量标签或演示属性。

## 5. 验证与交付

- 实际播放视频，检查开头、每个主要阶段和结尾。
- 对比视频确认两侧执行同一真实任务，并且预期差异可见。
- Story 确认变化原地发生、红线持续贴合、文字可读，并且总时长符合要求。
- 检查控件未被裁切，且没有隐私信息。
- 需要细致检查时，用 FFmpeg 抽取若干帧。
- 报告本地视频路径、路由、viewport 或镜头、执行场景和未覆盖内容。
- 不再需要时删除临时脚本和中间录制文件。
- 未经明确要求，不上传或发布视频。

对比视频只有记录真实行为时才能作为证据。Story video 是设计改造过程的展示，本身不能证明功能可用。
