#!/usr/bin/env python3
"""
简单的任务管理脚本
用于管理和查看任务列表
"""

import json
import sys
from datetime import datetime

class TaskManager:
    def __init__(self, tasks_file="tasks.json"):
        self.tasks_file = tasks_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.tasks_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('tasks', [])
        except FileNotFoundError:
            return []

    def save_tasks(self):
        metadata = {
            "total": len(self.tasks),
            "pending": len([t for t in self.tasks if t['status'] == 'pending']),
            "in_progress": len([t for t in self.tasks if t['status'] == 'in_progress']),
            "completed": len([t for t in self.tasks if t['status'] == 'completed']),
            "high_priority": len([t for t in self.tasks if t['priority'] == 'high']),
            "medium_priority": len([t for t in self.tasks if t['priority'] == 'medium']),
            "low_priority": len([t for t in self.tasks if t['priority'] == 'low'])
        }
        
        data = {
            "tasks": self.tasks,
            "metadata": metadata
        }
        
        with open(self.tasks_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def list_tasks(self, status=None, priority=None):
        filtered_tasks = self.tasks
        
        if status:
            filtered_tasks = [t for t in filtered_tasks if t['status'] == status]
        
        if priority:
            filtered_tasks = [t for t in filtered_tasks if t['priority'] == priority]
        
        if not filtered_tasks:
            print("没有找到符合条件的任务。")
            return
        
        print(f"\n{'='*60}")
        print(f"{'任务列表':^56}")
        print(f"{'='*60}")
        
        for task in filtered_tasks:
            status_icon = {
                'pending': '⏳',
                'in_progress': '🔄',
                'completed': '✅'
            }.get(task['status'], '❓')
            
            priority_icon = {
                'high': '🔴',
                'medium': '🟡',
                'low': '🟢'
            }.get(task['priority'], '⚪')
            
            print(f"\n{status_icon} [{task['id']:02d}] {task['title']}")
            print(f"   {priority_icon} 优先级: {task['priority']}")
            print(f"   📅 截止时间: {task['dueDate']}")
            if task['description']:
                print(f"   📝 描述: {task['description']}")
            if task['tags']:
                print(f"   🏷️  标签: {', '.join(task['tags'])}")

    def add_task(self, title, description="", priority="medium", due_date=""):
        new_id = max([t['id'] for t in self.tasks], default=0) + 1
        today = datetime.now().strftime("%Y-%m-%d")
        
        new_task = {
            "id": new_id,
            "title": title,
            "description": description,
            "priority": priority,
            "status": "pending",
            "assignee": "",
            "dueDate": due_date or today,
            "tags": [],
            "createdAt": today,
            "updatedAt": today
        }
        
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"✅ 任务 '{title}' 已创建，ID: {new_id}")

    def update_task_status(self, task_id, new_status):
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = new_status
                task['updatedAt'] = datetime.now().strftime("%Y-%m-%d")
                self.save_tasks()
                print(f"✅ 任务 {task_id} 状态已更新为: {new_status}")
                return
        print(f"❌ 未找到ID为 {task_id} 的任务")

def main():
    tm = TaskManager()
    
    if len(sys.argv) < 2:
        print("使用方法:")
        print("  python task_manager.py list [status] [priority]")
        print("  python task_manager.py add <title> [description] [priority] [due_date]")
        print("  python task_manager.py update <id> <status>")
        print("\n状态: pending, in_progress, completed")
        print("优先级: high, medium, low")
        return
    
    command = sys.argv[1]
    
    if command == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else None
        priority = sys.argv[3] if len(sys.argv) > 3 else None
        tm.list_tasks(status, priority)
    
    elif command == "add":
        if len(sys.argv) < 3:
            print("❌ 请提供任务标题")
            return
        
        title = sys.argv[2]
        description = sys.argv[3] if len(sys.argv) > 3 else ""
        priority = sys.argv[4] if len(sys.argv) > 4 else "medium"
        due_date = sys.argv[5] if len(sys.argv) > 5 else ""
        
        tm.add_task(title, description, priority, due_date)
    
    elif command == "update":
        if len(sys.argv) < 4:
            print("❌ 请提供任务ID和新状态")
            return
        
        try:
            task_id = int(sys.argv[2])
            new_status = sys.argv[3]
            tm.update_task_status(task_id, new_status)
        except ValueError:
            print("❌ 任务ID必须是数字")

if __name__ == "__main__":
    main()