"""
剪映批量复制143次（纯复制，无转场）
使用PyAutoGUI模拟键盘操作

使用前提：
  1. 剪映已打开，视频已放在主轨上（只放一次）
  2. 用鼠标单击选中该视频片段（变成白色边框）
  3. 脚本运行后5秒内切换到剪映窗口

依赖：pip install pyautogui
"""

import time
import pyautogui

# 安全设置
pyautogui.FAILSAFE = True  # 鼠标移至左上角紧急停止
pyautogui.PAUSE = 0.1      # 每次操作后暂停0.1秒

COPY_COUNT = 143             # 复制次数

def main():
    print("=" * 50)
    print("剪映批量复制143次（纯复制，无转场）")
    print("=" * 50)
    print("\n⚠️ 请确认：")
    print("  1. 剪映已打开，视频片段已在主轨上")
    print("  2. 该片段已被选中（白色边框）")
    print("  3. 剪映窗口已最大化")
    print("\n脚本将在 5 秒后开始，请立即切换到剪映窗口！")
    for s in range(5, 0, -1):
        print(f"  {s}...")
        time.sleep(1)
    
    print("\n开始执行...\n")

    # 第一步：复制原始片段
    print("  复制原始片段...")
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)

    # 第二步：循环粘贴143次
    for i in range(1, COPY_COUNT + 1):
        # 按End键跳到时间线末尾
        pyautogui.press('end')
        time.sleep(0.3)

        # 按Ctrl+V粘贴一次
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.3)

        if i % 10 == 0:
            print(f"  已完成 {i}/{COPY_COUNT}")

    print(f"\n✅ 完成！共复制粘贴 {COPY_COUNT} 次（加上原始共 {COPY_COUNT+1} 个片段）")


if __name__ == "__main__":
    main()