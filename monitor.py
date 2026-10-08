import psutil
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# ========== 替换为你的邮箱信息 ==========
MAIL_USER = "2124978873@qq.com"
MAIL_PASS = "nowbxibpggzijgjj"
TO_MAIL = "2124978873@qq.com"
# ===================================

def send_email(content):
    """发送QQ邮件告警"""
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header('【监控告警】电脑内存异常', 'utf-8')
    msg['From'] = MAIL_USER
    msg['To'] = TO_MAIL

    try:
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(MAIL_USER, MAIL_PASS)
        server.sendmail(MAIL_USER, [TO_MAIL], msg.as_string())
        server.quit()
        print("✅ 告警邮件已发送")
    except Exception as e:
        print(f"❌ 邮件发送失败: {e}")

def check_memory():
    """检查内存使用率"""
    mem = psutil.virtual_memory()
    mem_percent = mem.percent
    print(f"当前内存使用率: {mem_percent}%")

    # 阈值设为80%，触发告警
    if mem_percent > 80:
        send_email(f"【告警】电脑内存使用率过高！当前使用率: {mem_percent}%\n请尽快检查电脑状态。")

if __name__ == "__main__":
    print("监控已启动，每10秒检查一次...")
    while True:
        check_memory()
        time.sleep(10)