import requests,json

#剧集信息
# rss订阅地址
subscribe_ssr = 'ssr_url'
# 剧名
title_of_series = 'series_name'
# 季数(比如第一季，则输入1)
season_of_series = 1

#qbittorrent信息
# qbittorrent 用户账号密码
qbit_username = 'username'
qbit_password = 'password'
# qbittorrent地址:端口
url_qbt = 'http://localhost:port'
# qbittorrent 剧集储存根目录(你希望你的剧集存放在哪里)
series_directory = 'your/eries/directory'

##############################################################

# qbittorrent api 参数
api_param = '/api/v2/'
# 登录接口
auth_login_api = 'auth/login'
# 登出接口
auth_logout_api = 'auth/logout'
# 创建分类接口
create_category_api =  'torrents/createCategory'
# 添加rss订阅接口
add_feed_api = 'rss/addFeed'
# rss下载规则接口
set_rule_api = 'rss/setRule'


# 1. 登录并接受cookie
login_param = {'username' : qbit_username,
             'password' : qbit_password}
headers = {'Referer': url_qbt}

login_request =requests.post(url_qbt + api_param + auth_login_api , headers=headers, data=login_param)
print(login_request.status_code)
login_request_response_headers = login_request.headers
cookie_with_SID = login_request_response_headers['set-cookie'].split(';')[0]

headers['Cookie'] = cookie_with_SID


# 2. 创建新目录
createCategory_param = {'category': title_of_series, 'savePath' : series_directory + title_of_series + '/Season ' + str(season_of_series)}
createCategory_request = requests.post(url_qbt + api_param + create_category_api , headers=headers, data=createCategory_param)


# 3. RSS添加新订阅并改名
addFeed_param = {'url' : subscribe_ssr,
                 'path': title_of_series}
addFeed_request = requests.post(url_qbt + api_param + add_feed_api , headers=headers, data=addFeed_param)
print(addFeed_request.status_code)

# 4. 创建RSS下载器
ruleDef_param = {"addPaused":None,
                 "affectedFeeds":[subscribe_ssr],
                 "assignedCategory":"",
                 "enabled":True,
                 "episodeFilter":"",
                 "ignoreDays":0,
                 "lastMatch":"",
                 "mustContain":"",
                 "mustNotContain":"",
                 "previouslyMatchedEpisodes":[],
                 "priority":0,
                 "savePath":"",
                 "smartFilter":False,
                 "torrentContentLayout":None,
                 "torrentParams":{"category": title_of_series,
                                  "download_limit":-1,
                                  "download_path":"",
                                  "inactive_seeding_time_limit":-2,
                                  "operating_mode":"AutoManaged",
                                  "ratio_limit":-2,"save_path":"",
                                  "seeding_time_limit":-2,
                                  "skip_checking":False,
                                  "tags":[""],"upload_limit":-1,
                                  "stopped":False},
                "useRegex":False}

setRule_param = {'ruleName': title_of_series,
                 'ruleDef': json.dumps(ruleDef_param)}

setRule_request = requests.post(url_qbt + api_param + set_rule_api , headers=headers, data=setRule_param)
print(setRule_request.status_code)


# 5. 登出
logout_request = requests.post(url_qbt + api_param + auth_logout_api , headers=headers, data={})
print(logout_request.status_code)