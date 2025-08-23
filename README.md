# 123

## 任务管理系统

这个仓库包含一个简单的任务管理系统，帮助你组织和跟踪各种任务。

### 文件说明

- `tasks.md` - 任务列表的 Markdown 格式，便于查看和编辑
- `tasks.json` - 任务数据的 JSON 格式，包含详细的任务信息
- `task_manager.py` - Python 脚本，用于管理任务

### 使用方法

#### 查看任务
```bash
python task_manager.py list
```

#### 按状态筛选任务
```bash
python task_manager.py list pending    # 查看待办任务
python task_manager.py list in_progress    # 查看进行中任务
python task_manager.py list completed    # 查看已完成任务
```

#### 按优先级筛选任务
```bash
python task_manager.py list "" high    # 查看高优先级任务
python task_manager.py list "" medium    # 查看中优先级任务
python task_manager.py list "" low    # 查看低优先级任务
```

#### 添加新任务
```bash
python task_manager.py add "任务标题" "任务描述" "优先级" "截止日期"
```

#### 更新任务状态
```bash
python task_manager.py update 1 completed    # 将任务1标记为已完成
python task_manager.py update 2 in_progress    # 将任务2标记为进行中
```

### 任务状态

- `pending` - 待办
- `in_progress` - 进行中  
- `completed` - 已完成

### 优先级

- `high` - 高优先级 🔴
- `medium` - 中优先级 🟡
- `low` - 低优先级 🟢

### 示例任务

系统已经预设了一些示例任务，包括：

1. **高优先级任务**
   - 完成项目文档编写
   - 实现用户认证功能
   - 修复数据库连接问题

2. **中优先级任务**
   - 优化页面加载速度
   - 添加单元测试

3. **低优先级任务**
   - 美化界面设计

你可以根据需要修改这些任务或添加新的任务。