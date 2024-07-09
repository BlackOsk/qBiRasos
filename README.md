# qBiRasos
## 一、什么是qBiRasos
qBiRasos 是为应对qBittorrent订阅RSS下载时的遭遇的繁琐操作而开发的一套程序。
### qBiRasos的运行流程
1. 输入RSS订阅地址，剧集名称，剧集季数
2. 输入qbittorrent的登录用户账号密码，地址+端口，保存剧集的地址（使用媒体管理工具，如jellyfin时，建议把所有剧集保存在一个地址下的不同文件夹中，文件夹的名称以剧集标题命名。这也是本程序采用的方式）
3. 登录qbittorrent
4. 根据剧集名称自动创建分类和分类的保存目录
5. 添加RSS订阅，并根据剧集名修改RSS订阅源名称
6. 创建RSS自动下载器，下载器绑定4，5中创建的分类和RSS订阅源
*****
完成以上步骤后，qBittorrent会自动开始下载RSS订阅源中包含的项目
## 二、qBiRasos的应用条件
1. 程序基于python，建议安装anaconda后使用VS Code运行
2. 目前实测可应用于qBittorrent最新版的webAPI（2.9.3）
3. qBittorrent 的选项-下载-保存管理中：
   1. 默认Torrent管理模式 设为 自动
   2. 当Torrent分类修改时 设为 重新定位Torrent
   3. 当默认保存路径修改时 设为 重新定位受影响的Torrent
   4. 当分类保存路径修改时 设为 重新定位受影响的Torrent
4.  qBittorrent 的选项-RSS-中：
     1. RSS阅读器-启用获取RSS订阅 需勾选打开
     2. RSS Torrent自动下载器 需勾选打开
## 三、开发参考内容
1. [qBittorrent Web API documentation](https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1))
