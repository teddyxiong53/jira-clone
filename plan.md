# Jira UI 像素级克隆项目说明文档（Vue 3 + TailwindCSS 纯前端版）

**版本**：v1.0  
**创建日期**：2026年3月  
**作者**：AI 生成（基于用户需求）  
**目标**：通过纯前端技术实现 Jira 当前版本（2026 年最新界面风格）的**像素级视觉 + 交互还原**。不涉及任何后端、数据库或真实 API，所有数据均为本地 Mock。

---

## 1. 项目概述

本项目旨在使用 **Vue 3 + TailwindCSS** 完整复刻 Jira 的核心用户界面，包括：

- 全局布局（顶部导航栏 + 左侧可折叠边栏 + 主内容区）
- 项目切换与导航
- 看板（Kanban Board）
- 待办列表（Backlog）
- 问题列表（Issue List）
- 问题详情弹窗（Issue View Modal）
- 仪表盘（Dashboard）
- 搜索、创建、通知、用户菜单等全局交互

**核心要求**：
- **像素级还原**：颜色、圆角、阴影、间距、字体、hover 效果、active 状态必须与真实 Jira（2026 年版本）完全一致（误差 ≤ 1px）。
- **纯前端**：无后端，使用本地 JSON Mock 数据 + Pinia 状态管理。
- **高交互性**：支持拖拽看板、模态框、实时过滤、搜索高亮等。
- **可扩展**：后续可轻松接入真实后端（REST API）。

**适用场景**：
- 前端学习 / 面试作品
- Jira 二次开发原型
- UI 组件库演示

---

## 2. 技术栈（精确版本推荐）

| 类别         | 技术                     | 版本要求          | 用途 |
|--------------|--------------------------|-------------------|------|
| 框架         | Vue 3                    | ^3.5.0            | 核心 |
| 构建工具     | Vite                     | ^6.0.0            | 开发/打包 |
| 样式         | TailwindCSS              | ^3.4.0+           | 像素级样式 |
| 路由         | Vue Router               | ^4.4.0            | 多视图切换 |
| 状态管理     | Pinia                    | ^2.2.0            | 全局 Mock 数据 |
| 图标         | Lucide Vue               | ^0.400.0          | Jira 风格图标（可替换为 Heroicons） |
| 拖拽         | vue-draggable-plus       | ^0.3.0            | 看板拖拽（轻量，无额外依赖） |
| 日期         | dayjs                    | ^1.11.0           | 时间格式化 |
| 富文本模拟   | @tiptap/vue-3 + starter-kit | ^2.0.0         | 问题描述编辑（可选） |
| 工具         | TypeScript               | ^5.0.0            | 类型安全 |
| 其他         | vueuse                   | ^11.0.0           | 鼠标事件、拖拽辅助 |

**Tailwind 配置关键**（`tailwind.config.js`）：
```js
module.exports = {
  content: ["./index.html", "./src/**/*.{vue,js,ts}"],
  theme: {
    extend: {
      colors: {
        // Atlassian Design System (Jira 2026 官方配色)
        atlassian: {
          blue: {
            50: '#deebff',
            100: '#bfe3ff',
            200: '#7ac3ff',
            300: '#2684ff',
            400: '#0052cc',     // Primary Button / Accent
            500: '#0747a6',
          },
          neutral: {
            0: '#ffffff',
            10: '#f4f5f7',
            20: '#ebecf0',
            30: '#dfe1e6',
            40: '#c1c7d0',
            50: '#b3bac5',
            60: '#97a0af',
            70: '#7a869a',
            80: '#6b778c',
            90: '#5e6c84',
            100: '#42526e',
            200: '#344563',
            300: '#253858',
            400: '#172b4d',
          },
          red: { 400: '#ff5630' },   // High priority
          yellow: { 400: '#ffab00' },
          green: { 400: '#36b37e' },
        }
      },
      fontFamily: {
        sans: ['-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'sans-serif'],
      },
      boxShadow: {
        'jira-card': '0 1px 3px rgba(9,30,66,0.15), 0 0 1px rgba(9,30,66,0.1)',
        'jira-modal': '0 10px 40px -10px rgba(9,30,66,0.3)',
      }
    }
  }
}
```

---

## 3. 项目目录结构（推荐）

```
jira-clone/
├── public/
│   └── mock-data/          # 可选静态 JSON
├── src/
│   ├── assets/
│   │   └── icons/          # 自定义 SVG（若 Lucide 不够）
│   ├── components/
│   │   ├── layout/
│   │   │   ├── TopNav.vue
│   │   │   ├── SideNav.vue
│   │   │   └── ProjectHeader.vue
│   │   ├── common/
│   │   │   ├── IssueCard.vue
│   │   │   ├── Avatar.vue
│   │   │   ├── PriorityIcon.vue
│   │   │   └── StatusBadge.vue
│   │   ├── board/
│   │   │   ├── KanbanBoard.vue
│   │   │   ├── KanbanColumn.vue
│   │   │   └── KanbanCard.vue
│   │   └── modal/
│   │       └── IssueModal.vue
│   ├── stores/
│   │   ├── issues.ts       # Pinia store
│   │   └── ui.ts           # 侧边栏折叠、模态框状态
│   ├── views/
│   │   ├── DashboardView.vue
│   │   ├── BoardView.vue
│   │   ├── BacklogView.vue
│   │   ├── IssuesListView.vue
│   │   └── ProjectSettings.vue
│   ├── router/
│   │   └── index.ts
│   ├── mock/
│   │   └── issues.json     # 初始数据（100+ 条）
│   ├── utils/
│   │   ├── formatIssueKey.ts
│   │   └── dragUtils.ts
│   └── App.vue
├── tailwind.config.js
├── vite.config.ts
└── package.json
```

---

## 4. 核心界面拆解（像素级还原要点）

### 4.1 全局布局（App.vue）
- **顶部导航栏**（固定 48px 高）：
  - 左侧：Jira 云图标（#0052cc）+ 项目名称下拉（带搜索）
  - 中间：全局搜索框（宽度 320px，带快捷键提示 `/`）
  - 右侧：+ 创建按钮（下拉菜单：创建问题、创建项目、创建子任务）、通知铃铛（带红点）、帮助（?）、用户头像（带下拉：Profile、Settings、Log out）
- **左侧边栏**（可折叠，宽度 240px → 48px）：
  - 固定顶部：Your work / Projects / Filters / Dashboards
  - 动态部分：Recent projects + Starred
  - 底部：Apps / Marketplace / Settings
- **主内容区**：`router-view` + 右侧可展开的 Issue 预览面板（可选）

### 4.2 看板页面（BoardView.vue）
- 顶部：Board 名称 + 筛选器（Assignee、Epic、Label）+ 三点菜单
- 主体：水平滚动容器（`overflow-x-auto`），每列宽度固定 280px
- 每列头部：状态名称 + 数量徽章 + “+” 添加按钮
- 卡片：
  - 背景 #ffffff，圆角 3px，阴影 `jira-card`
  - 上方：Issue Key（蓝色）+ Summary（单行省略）
  - 下方：标签（小圆角标签）、Assignee 头像（32px）、Priority 图标、Story Points（灰色圆角）
  - Hover：背景 #f4f5f7，边框 #0052cc

### 4.3 问题详情模态框（IssueModal.vue）
- 宽度 960px，居中，圆角 8px，阴影 `jira-modal`
- 左侧（70%）：Summary 可编辑、Description（Tiptap 编辑器）、Comments（带头像 + 时间）
- 右侧（30%）：固定面板
  - Status 下拉
  - Assignee / Reporter / Labels
  - Priority / Epic / Sprint
  - Dates（Created / Updated）
  - Attachments（模拟上传）
- 右上角关闭按钮 + 全屏切换

### 4.4 其他页面（简要）
- **Backlog**：左侧 Epic/Story 列表 + 右侧 Sprint 看板
- **Issues List**：表格模式（可排序），支持批量操作
- **Dashboard**：Grid 布局小部件（Assigned to me、Recent updated）

---

## 5. Mock 数据设计（stores/issues.ts）

```ts
interface Issue {
  id: string;
  key: string;
  summary: string;
  description: string;
  status: 'todo' | 'inprogress' | 'done';
  priority: 'highest' | 'high' | 'medium' | 'low' | 'lowest';
  assignee: { id: string; name: string; avatar: string };
  reporter: { ... };
  labels: string[];
  storyPoints: number;
  created: string;
  updated: string;
}

export const useIssueStore = defineStore('issues', {
  state: () => ({
    issues: [] as Issue[],     // 从 mock/issues.json 加载
    columns: ['todo', 'inprogress', 'done']
  }),
  actions: {
    moveIssue(fromColumn: string, toColumn: string, issueId: string) { ... }
  }
})
```

初始数据建议包含：
- 至少 50 个真实风格的问题（不同状态、优先级、标签）
- 10 个不同用户头像（使用 unsplash 或 placeholder.co）

---

## 6. 像素级实现技巧（重点）

1. **颜色与间距**：
   - 所有颜色必须使用 `text-atlassian-blue-400`、`bg-atlassian-neutral-10` 等
   - 间距统一使用 Tailwind `p-3`、`gap-2`、`space-x-2`，必要时使用 `arbitrary value` 如 `gap-[11px]`

2. **字体与排版**：
   - 标题：font-semibold text-[15px]
   - 正文：text-[14px] leading-tight
   - Issue Key：text-[#0052cc] font-medium

3. **图标与 Avatar**：
   - 优先使用 Lucide `Plus`、`Bell`、`Search` 等
   - Avatar 使用 `<img class="w-6 h-6 rounded-full ring-2 ring-white">`

4. **拖拽实现**：
   ```vue
   <KanbanColumn @dragover.prevent @drop="onDrop">
     <Draggable v-model="columnIssues" group="issues">
   ```

5. **模态框动画**：
   - 使用 Vue Transition + Tailwind `scale-95 opacity-0` → `scale-100 opacity-100`

6. **响应式**：
   - 主要为桌面（1280px+），移动端仅做最小适配（侧边栏自动折叠）

---

## 7. 开发流程（推荐使用 AI 辅助）

**步骤 0**：创建项目 + 配置 Tailwind（参考第 2 节）

**步骤 1**：搭建全局布局（TopNav + SideNav + App.vue）

**步骤 2**：实现 Pinia store + Mock 数据加载

**步骤 3**：逐个组件开发（建议顺序）：
1. IssueCard.vue
2. KanbanColumn.vue + 拖拽
3. IssueModal.vue
4. TopNav + SideNav

**AI 提示词模板**（直接复制给任意 AI 使用）：
```
你现在是 Jira UI 专家。请使用 Vue 3 + TailwindCSS（使用 atlassian 颜色扩展）生成像素级还原的组件：
组件名称：IssueCard.vue
要求：
- 完全使用 Tailwind class（无自定义 CSS）
- 包含 key、summary、labels、avatar、priority、story points
- hover 效果、拖拽 cursor
- 完全匹配 Jira 2026 视觉（提供截图描述或直接写 class）
- 使用 TypeScript + <script setup>
```

**步骤 4**：路由 + 视图切换

**步骤 5**：测试所有交互（拖拽、模态框、搜索过滤）

**步骤 6**：优化性能（`v-memo`、`keep-alive`）

---

## 8. 运行与打包

```bash
npm install
npm run dev          # http://localhost:5173
npm run build        # dist 文件夹
npm run preview
```

**部署**：Vercel / Netlify（纯静态，零配置）

---

## 9. 后续扩展建议（可选）

- 接入真实 Jira REST API（使用官方 OAuth）
- 添加 Dark Mode（Tailwind `dark:`）
- Timeline / Roadmap 视图
- 权限模拟（不同角色不同菜单）
- 导出 PDF / CSV
- PWA 支持

---

## 10. 注意事项与常见坑

- **像素级检查**：打开真实 Jira → Chrome DevTools → 右键“检查” → 复制所有 class + computed styles，然后在 Tailwind 中精确还原。
- **字体渲染**：macOS 与 Windows 字体渲染差异，建议在两端测试。
- **拖拽兼容**：移动端使用 touch 事件（vue-draggable-plus 已支持）。
- **性能**：100+ 卡片时使用虚拟列表（后续可加 `vue-virtual-scroller`）。
- **图标一致性**：所有 icon 必须 16px 或 20px，与 Jira 完全一致。

---

