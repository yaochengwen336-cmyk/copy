"""
剪映批量复制 143 次。

使用 PyAutoGUI 模拟键盘操作：
1. 先复制当前选中的片段。
2. 每次跳到时间线末尾。
3. 粘贴一次。

运行前准备：
1. 安装依赖：pip install pyautogui
2. 打开剪映，把视频片段放在主轨上。
3. 用鼠标单击选中该片段，让它出现白色边框。
4. 运行脚本后，5 秒内切回剪映窗口。
"""

import time
import pyautogui


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1

COPY_COUNT = 143


def main():
    print("=" * 50)
    print("剪映批量复制143次")
    print("=" * 50)
    print("\n请确认：")
    print("  1. 剪映已经打开，视频片段已经在主轨上")
    print("  2. 该片段已经被选中，出现白色边框")
    print("  3. 剪映窗口已经最大化")
    print("\n脚本将在 5 秒后开始，请立即切换到剪映窗口。")

    for s in range(5, 0, -1):
        print(f"  {s}...")
        time.sleep(1)

    print("\n开始执行...\n")
    print("复制原始片段...")
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.5)

    for i in range(1, COPY_COUNT + 1):
        pyautogui.press("end")
        time.sleep(0.3)

        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.3)

        if i % 10 == 0:
            print(f"已完成 {i}/{COPY_COUNT}")

    print(f"\n完成！共复制粘贴 {COPY_COUNT} 次，加上原始片段共 {COPY_COUNT + 1} 个片段。")


if __name__ == "__main__":
    main()
