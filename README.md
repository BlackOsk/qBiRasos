# qBiRasos

## 一、什么是qBiRasos

qBiRasos 是为应对qBittorrent订阅RSS下载时的遭遇的繁琐操作，通过python开发的一系列程序。

## 二、qBiRasos适用于什么场景

推荐在NAS上部署qBittorrent服务以及媒体管理系统（如jellyfin、Plex、Emby等），使用qBittorrent的RSS订阅下载功能下载剧集，并需要修改下载文件的保存地址和文件名，以适用于媒体管理系统的刮削功能，或具有类似需求的用户使用。

## 三、目前包含的内容以及使用方式

### 2.1 根据rss订阅链接和剧名，自动建立分类并下载

**此功能对应的程序为：*rss自动建立分类并下载.py***

#### 程序功能

输入rss订阅链接、剧名、季数、以及相关qBittorrent的参数，程序将根据输入内容建立分类及分类保存地址，添加RSS订阅，建立自动下载规则并开始下载。

#### 操作方式

1. 将`subscribe_ssr`的定义内容（`=`后面的` ''`中间）改为对应资源的RSS订阅链接
2. 将`title_of_series`的定义内容（`=`后面的` ''`中间）改为对应资源的标题（标题名最好能在媒体管理系统刮削信息的媒体信息网站中能被正确搜寻——简单的说，最好填入这个资源的官方标题、正式标题）
3. 将`title_of_series`的定义内容（`=`后面的` ''`中间）改为对应剧集季数的**数字**
4. 将`qbit_username`的定义内容（`=`后面的` ''`中间）改为你登录qBittorrent所使用的账号
5. 将`qbit_password`的定义内容（`=`后面的` ''`中间）改为上一步中登录qBittorrent的账号所使用的密码
6. 将`url_qbt`的定义内容（`=`后面的` ''`中间）改为qBittorrent服务的地址和端口
7. 将`series_directory`的定义内容（`=`后面的` ''`中间）改为在qBittorrent中储存剧集的根目录（*若剧集保存在`download/series`下，则输入`downbload/series`）
   *使用媒体管理系统，如jellyfin时，建议把所有剧集保存在一个地址下的不同文件夹中，文件夹的名称以剧集标题命名。这也是本程序采用的方式*
8. 运行程序

#### 运行流程

1. 输入相关参数
2. 登录qbittorrent
3. 根据剧集名称自动创建分类和分类的保存目录
4. 添加RSS订阅，并根据剧集名修改RSS订阅源名称
5. 创建RSS自动下载器，下载器绑定4，5中创建的分类和RSS订阅源

*****

完成以上步骤后，qBittorrent会自动开始下载RSS订阅源中包含的项目，并将下载的torrent保存到对应的分类地址中。

### 2.2 修改下载剧集单集的文件名

**此功能对应的程序为：*单集重命名.py***

#### 程序功能

获取qBittorrent最新的x个torrent文件，判断出其中属于剧集的文件，在剧集原文件名中提取集数信息，最后批量将剧集文件重命名为“E+集数”的形式（例如原文件名为`[xxxx] xxxxxx- 04 [xxxxxxxxx][xxxxxx].mkv`，程序运行后改名为`E4.mkv`）

#### 操作方式

1. 将`torrent_num`的定义内容（`=`后面的` ''`中间）改为希望选取的最近的torrent数量（如希望选取最新的15个torrent文件，则输入15）
2. 将`qbit_username`的定义内容（`=`后面的` ''`中间）改为你登录qBittorrent所使用的账号
3. 将`qbit_password`的定义内容（`=`后面的` ''`中间）改为上一步中登录qBittorrent的账号所使用的密码
4. 将`url_qbt`的定义内容（`=`后面的` ''`中间）改为qBittorrent服务的地址和端口
5. 将`series_directory`的定义内容（`=`后面的` ''`中间）改为在qBittorrent中储存剧集的根目录（*若剧集保存在`download/series`下，则输入`downbload/series`
6. 将`incomplete_directory`的定义内容（`=`后面的` ''`中间）改为qBittorrent储存下载中文件的位置（qBittorrent的选项——下载——保存管理——勾选“保存未完成的torrent到”，并将后面框中的目录复制到`''`中间）。
7. 运行程序

#### 运行流程

1. 输入相关参数
2. 登录qbittorrent
3. 获取torrent信息列表，根据是否为剧集储存的根目录判断是否为剧集
4. 提取信息列表中的torrent hash值、torrent保存路径、torrent文件名
5. 根据正则表达式提取剧集文件的集数
6. 形成改名后的torrent文件名列表
7. 调用改名接口，完成文件改名

******

完成以上步骤后，最新的n个（根据`torrent_num`中的数量确定）torrent文件中，储存在`series_directory`对应参数下的文件将会根据原文件名中的集数信息，改名为`E+集数+后缀`的形式。

## 二、qBiRasos的应用条件

1. 程序基于python，运行需要具有python的运行环境
2. 目前实测可应用于qBittorrent最新版的webAPI（2.9.3）
3. qBittorrent 的选项-下载-保存管理中：
   1. 默认Torrent管理模式 设为 自动
   2. 当Torrent分类修改时 设为 重新定位Torrent
   3. 当默认保存路径修改时 设为 重新定位受影响的Torrent
   4. 当分类保存路径修改时 设为 重新定位受影响的Torrent
4. qBittorrent 的选项-RSS-中：
     1. RSS阅读器-启用获取RSS订阅 需勾选打开
     2. RSS Torrent自动下载器 需勾选打开

## 三、开发参考内容

1. [qBittorrent Web API documentation](https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1))
