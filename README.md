# 算法与数据结构知识体系整理

## 1. 基础数据结构

| 中文名词 | 英文翻译 | 备注 |
|--------|---------|------|
| 普通数组 | Array | 有时也叫 Standard Array |
| 矩阵 | Matrix | 复数形式为 Matrices |
| 链表 | Linked List | 单链表为 Singly Linked List |
| 栈 | Stack | 特点是后进先出（LIFO） |
| 队列 | Queue | 特点是先进先出（FIFO） |
| 堆 | Heap | 如 Max Heap（大顶堆）、Min Heap（小顶堆） |
| 哈希 | Hash | 常指 Hash Table（哈希表）或 Hash Map |

---

## 2. 字符串与序列

| 中文名词 | 英文翻译 | 备注 |
|--------|---------|------|
| 字符串 | String | 对应题目中的文字处理 |
| 子串 | Substring | 强调**连续**；不连续的叫子序列（Subsequence） |

---

## 3. 高级数据结构与图论

| 中文名词 | 英文翻译 | 备注 |
|--------|---------|------|
| 二叉树 | Binary Tree | 搜索二叉树为 BST |
| 图论 | Graph Theory | 涉及节点（Nodes / Vertices）和边（Edges） |

---

## 4. 核心算法思想与技巧

| 中文名词 | 英文翻译 | 备注 |
|--------|---------|------|
| 双指针 | Two Pointers | 常用于数组或链表的优化 |
| 滑动窗口 | Sliding Window | 处理连续子数组 / 子串问题的利器 |
| 二分查找 | Binary Search | 在有序序列中快速定位 |
| 回溯 | Backtracking | 搜索算法，常用于全排列或组合 |
| 贪心算法 | Greedy Algorithm | 每一步都采取局部最优解 |
| 动态规划 | Dynamic Programming | 简称 DP |
| 多维动态规划 | Multidimensional DP | 通常指二维或三维的状态转移方程 |
| 技巧 | Techniques / Tips | 刷题时的特定手段 |

---

# 说明与使用建议

- **第 1 部分**：是刷题的地基（数组、哈希、栈队列）
- **第 2 部分**：LeetCode 高频（字符串 + 子串/子序列）
- **第 3 部分**：中高难度题核心（树、图）
- **第 4 部分**：真正拉开差距的算法思想

👉 实际刷题时，**第 4 部分往往比第 3 部分更重要**。



# some confusions
1. 归并排序和和快速排易搞混
2. 递归和迭代在在一些情况下的转换是否需要都掌握



# git
| 指令 | 作用 | 形象理解 |
| --- | --- | --- |
| `git init` | 在当前文件夹初始化一个新的 Git 仓库 | 给这个项目装上“行车记录仪” |
| `git status` | 查看当前文件的状态（哪些改了还没存） | 检查哪些照片还没进相册 |
| `git add <文件名>` | 将文件添加到暂存区 | 把要拍的照片选好，摆在镜头前 |
| `git add .` | 将所有修改过的文件都添加到暂存区 | 选好全场所有的照片 |
| `git commit -m "说明"` | 提交暂存区内内容到本地仓库 | 按下快门，并给这组照片写个备注 |
| `git log` | 查看提交历史 | 翻看以前的相册记录 |
| `git push` | 将本地代码推送到远程仓库（GitHub/GitLab） | 把相册同步到云端网盘 |
| `git pull` | 从远程仓库拉取最新代码到本地 | 把云端最新的照片下载到本地 |





总结：关于 Git 的“空”逻辑
空文件夹不上传：Git 追踪的是内容（Blob），不是目录。如果 StringsAndSequences 为空，它在 Git 眼中是不存在的。

单一路径合并：如果一层目录只有一个子目录，GitHub 会将其路径合并显示以节省空间。

time: 260125
git各种命令本质上是在维护.git文件夹，带有.git文件夹的目录就是本地仓库





## 开源项目贡献流程（一页速查版）

### 前提
- 你没有目标仓库（A/repo）的写权限
- 通过 **Fork + Pull Request** 方式贡献代码

---

### 1. Fork 原仓库
- GitHub：进入 `A/repo`
- 点击右上角 **Fork**
- 得到你自己的仓库：`B/repo`

---

### 2. Clone 自己的 Fork
```bash
git clone https://github.com/B/repo.git
cd repo
```

---

### 3. 添加 upstream（指向原仓库 A）
```bash
git remote add upstream https://github.com/A/repo.git
git remote -v
```

---

### 4. 同步原仓库最新代码
```bash
git fetch upstream
git switch main
git merge upstream/main
```

---

### 5. 新建分支进行开发（不要在 main 上改）
```bash
git switch -c my-branch
```

---

### 6. 本地提交修改
```bash
git add .
git commit -m "fix: concise description"
```

---

### 7. Push 分支到自己的仓库（B/repo）
```bash
git push -u origin my-branch
```

---

### 8. 发起 Pull Request（GitHub）
- base repo：`A/repo`
- base branch：`main`
- head repo：`B/repo`
- head branch：`my-branch`
- 填写标题和说明，创建 PR

---

### 9. 根据 Review 更新 PR（如需要）
```bash
git add .
git commit -m "address review comments"
git push
```

> PR 会自动更新，无需新建

---

### 10. PR 合并后同步 fork（可选）
```bash
git switch main
git fetch upstream
git merge upstream/main
git push origin main
```

---
ps: git pull=git fetch+git merge


