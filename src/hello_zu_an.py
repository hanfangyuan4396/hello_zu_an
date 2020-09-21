import time
import pyautogui as ag

print('祖安人v1.0，建议使用win10自带输入法')
print('遇到意外情况CTRL + alt + del 停止')
num = int(input('输入攻击次数:(推荐1-9)无上限'))
pause = int(input('输入攻击间歇秒数:(防止电脑卡顿，建议1以上)'))
print('5秒后开始攻击，请尽快切回聊天框！')
time.sleep(5)

for i in range(num):
    with open('zu_an_ci_hui.txt') as f:
        for line in f:
            time.sleep(pause/2)
            # 先不输入最后回车，停顿一会儿再发送
            ag.typewrite(line[:-1])
            time.sleep(pause/2)
            ag.typewrite('\n')
        time.sleep(pause)
input('攻击完成！enter键退出....')