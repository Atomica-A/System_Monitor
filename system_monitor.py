import psutil
import subprocess
import os
from dotenv import load_dotenv

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")
 
def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

cpu = get_cpu_usage()
memory = get_memory_usage()
disk = get_disk_usage()

if cpu >= 80:
    cpu_message = f"Your CPU usage is: {cpu}. Which is very high!!"
    curl_command = f'curl -s -X POST "https://api.telegram.org/bot{bot_token}/sendMessage" ' \
               f' -d "chat_id={chat_id}" ' \
               f' -d "text={cpu_message}"'
    response = subprocess.run(curl_command, shell=True, text=True, capture_output=True)


if memory >= 80:
    memory_message = f"Your Memory usage is: {memory}. Which is very high!!"
    curl_command = f'curl -s -X POST "https://api.telegram.org/bot{bot_token}/sendMessage" ' \
               f' -d "chat_id={chat_id}" ' \
               f' -d "text={memory_message}"'
    response = subprocess.run(curl_command, shell=True, text=True, capture_output=True)


if disk >= 85:
    disk_message = f"Your disk usage is: {disk}. Which is very high!!"
    curl_command = f'curl -s -X POST "https://api.telegram.org/bot{bot_token}/sendMessage" ' \
               f' -d "chat_id={chat_id}" ' \
               f' -d "text={disk_message}"'
    response = subprocess.run(curl_command, shell=True, text=True, capture_output=True)




