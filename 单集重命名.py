import requests,re


# 程序参数
# 筛选最近x个torrent
torrent_num = '15'
#qbittorrent信息
# qbittorrent 用户账号密码
qbit_username = 'username'
qbit_password = 'password'
# qbittorrent地址:端口
url_qbt = 'http://localhost:port'
# qbittorrent 剧集储存根目录(你的剧集存放在哪里)
series_directory = 'your/eries/directory'
# qbittorrent 下载中文件存放目录(选项——下载——保存管理——勾选“保存未完成的torrent到”，并将后面框中的目录复制到下面)
incomplete_directory = 'your/incomplete/directory'

##############################################################

# qbittorrent api 参数
api_param = '/api/v2/'
# 登录接口
auth_login_api = 'auth/login'
# 登出接口
auth_logout_api = 'auth/logout'
# 获取torrent接口
create_category_api =  'torrents/info'
# torrent文件改名接口
rename_file_api =  'torrents/renameFile'


# 1. 登录并接受cookie
login_param = {'username' : qbit_username,
             'password' : qbit_password}
headers = {'Referer': url_qbt}

login_request =requests.post(url_qbt + api_param + auth_login_api , headers=headers, data=login_param)
print(login_request.status_code)
login_request_response_headers = login_request.headers
cookie_with_SID = login_request_response_headers['set-cookie'].split(';')[0]

headers['Cookie'] = cookie_with_SID


# 2. 获取torrent 列表, 输出改名列表
def is_match(str):
    #集数提取规则
    patterns = ['\\x20[0-9][0-9]\\x20', '-[0-9][0-9]-', '\[[0-9][0-9]\]']

    for item in patterns:
        if re.search(item,str):
            return [True, re.search(item, str).group()[1:-1]]
        else:
            continue
    return [False,str]

# 调用torrent信息提取接口
get_torrent_info_param = {'filter': 'all',
                          'sort': 'added_on',
                          'reverse': 'true',
                          'limit': torrent_num}###
get_torrent_info_request = requests.post(url_qbt + api_param + create_category_api, headers=headers, data=get_torrent_info_param)
print(get_torrent_info_request.status_code)


# 输出torrent文件路径、储存路径、hash值
get_torrent_info_request_json = get_torrent_info_request.json()
# 文件路径
torrent_content_path = []
# 储存路径
torrent_save_path = []
#hash值
torrent_hash = []
for i in range(len(get_torrent_info_request_json)):
    if incomplete_directory in get_torrent_info_request_json[i]['save_path']:
        continue
    elif series_directory in get_torrent_info_request_json[i]['content_path']:
        torrent_content_path.append(get_torrent_info_request_json[i]['content_path'])
        torrent_save_path.append(get_torrent_info_request_json[i]['save_path'])
        torrent_hash.append(get_torrent_info_request_json[i]['hash'])
    else:
        continue

# torrent 文件名
torrent_file_name = []
for i in range(len(torrent_content_path)):
    torrent_file_name.append(torrent_content_path[i].replace(torrent_save_path[i]+'/', ''))

# 根据 'E+集数' 的格式输出重命名后的剧名
torrent_file_rename = []
for item in torrent_file_name:
    if is_match(item)[0]:
        torrent_file_rename.append('E' + is_match(item)[1] + item[-4:])
    else:
        torrent_file_rename.append(item)


# 改名
for i in range(len(torrent_hash)):
    rename_file_request =requests.post(url_qbt + api_param + rename_file_api , headers=headers, \
                                    data={'hash': torrent_hash[i], 'oldPath': torrent_file_name[i], 'newPath': torrent_file_rename[i]})
    print(rename_file_request.status_code)


# 5. 登出
logout_request = requests.post(url_qbt + api_param + auth_logout_api , headers=headers, data={})
print(logout_request.status_code)
