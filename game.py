#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""猜数字小游戏 —— 由 AI Coding Agent 辅助开发"""
import random


def ask(prompt):
    print(prompt)
    val = input()
    print(val)
    return val


def play():
    print("=" * 40)
    print("        欢迎来到猜数字小游戏！")
    print("=" * 40)
    print("请选择难度：")
    print("  1. 简单 (1-50)")
    print("  2. 中等 (1-100)")
    print("  3. 困难 (1-200)")
    choice = ask("请输入难度编号(默认2):").strip() or "2"
    if choice == "1":
        low, high = 1, 50
    elif choice == "3":
        low, high = 1, 200
    else:
        low, high = 1, 100

    target = random.randint(low, high)
    count = 0
    print(f"我已经想好了一个 {low}~{high} 之间的数字，快来猜吧！")
    while True:
        guess = int(ask("请输入你的猜测:"))
        count += 1
        if guess < target:
            print("太小了，再大一点~")
        elif guess > target:
            print("太大了，再小一点~")
        else:
            print(f"恭喜你，猜对了！就是 {target}，共猜了 {count} 次。")
            break
    if ask("再来一局？(y/n):").strip().lower() == "y":
        play()


if __name__ == "__main__":
    play()

