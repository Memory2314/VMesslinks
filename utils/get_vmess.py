import requests
from Crypto.Cipher import AES
import base64

# 接口URL
url = "https://www.m4twf.xyz:20000/api/evmess?&proto=v2&platform=android&googleplay=1&ver=3.0.5&deviceid=1bcec3395995cf19unknown&unicode=1bcec3395995cf19unknown&t=1717462751804&code=9GFZ2R&recomm_code=&f=2024-06-04&install=2024-06-04&token=amSTaWVnkZWOk2xscWlsb5mZbmRolGuRZ2mQl5Jrkmhnaw==&package=com.honeybee.network&area=5"

# 解密密钥和IV（文本）
key = b'ks9KUrbWJj46AftX'
iv = b'ks9KUrbWJj46AftX'

# 存储解密后的节点信息
decrypted_nodes = set()

# 获取并解密节点信息
def fetch_and_decrypt():
    response = requests.get(url)
    if response.status_code == 200:
        encrypted_data = response.text.strip()  # 获取返回的加密字符串
        try:
            # 将Base64编码的加密数据解码
            encrypted_data_bytes = base64.b64decode(encrypted_data)
            # 创建AES解密器
            cipher = AES.new(key, AES.MODE_CBC, iv)
            # 解密数据
            decrypted_data = cipher.decrypt(encrypted_data_bytes)
            # 返回解密后的数据
            return decrypted_data.decode('utf-8', errors='ignore').rstrip('\x00')
        except Exception as e:
            print(f"解密失败：{e}")
            return None
    else:
        print(f"请求失败，状态码: {response.status_code}")
        return None

# 重复获取并解密节点信息10次
for _ in range(10):
    node_info = fetch_and_decrypt()
    if node_info:
        decrypted_nodes.add(node_info)

# 保存去重后的节点信息
vmess = ""
for node in decrypted_nodes:
    print(node)
    vmess += f"{node}\n"
with open("./links/vmess", "w") as f:
    f.write(vmess)