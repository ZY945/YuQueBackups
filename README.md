# windwos
```bash
# 1.创建虚拟环境
python -m venv test-env
# 2.进入虚拟环境
.\test-env\Scripts\activate
# 3.更新pip
python.exe -m pip install --upgrade pip
# 4.下载所需模块
pip install requests
pip install aiofiles
pip install aiohttp_requests
# 5.启动脚本(可以现根据所需进行修改)
py.exe .\app.py
```
# mac
```bash
# 1.创建虚拟环境
python -m venv test-env
# 2.进入虚拟环境
source ./test-env/bin/activate
# 3.更新pip
python -m pip install --upgrade pip
# 4.下载所需模块
# pip install requests
# pip install aiofiles
# pip install aiohttp_requests
pip install -r requirements.txt
# 5.启动脚本(可以现根据所需进行修改)
python app.py 
```