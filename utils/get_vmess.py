import requests
from datetime import datetime

# 获取今天的日期
year = datetime.now().year
month = datetime.now().strftime("%m")
day = datetime.now().strftime("%d")

# 构建 URL，日期部分会自动替换为当前日期
url = f"https://clashnode.cc/uploads/{year}/{month}/0-{year}{month}{day}.txt"

# 发送 HTTP 请求获取链接内容
try:
    v2ray_response = requests.get(url+'.txt')
    clash_response = requests.get(url+'.yaml')
    v2ray_response.raise_for_status()  # 检查请求是否成功
    clash_response.raise_for_status()

    print(f"成功获取到内容 (日期: {current_date}):")
    v2ray_node = v2ray_response.text
    print(v2ray_node)

except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")

# 将去重后的节点信息保存到文件
with open("./links/v2ray", "w") as f:
    f.write(v2ray_node)
with open("./links/clash", "w") as f:
    f.write(clash_response)

print("节点信息已保存")
