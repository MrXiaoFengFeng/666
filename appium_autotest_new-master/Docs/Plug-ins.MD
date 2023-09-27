# 拓展工具存放目录

## ElementsConf.py
- 此脚本为自动维护元素字典的拓展脚本
- 使用此脚本可以将指定界面的元素信息与配置文件中的字典信息进行校验和更新
    1. 对于新元素: 向字典中添加元素的id及text信息
    2. 对于已有元素: 优先更新id,若只有text发生变化不予理会(见下文)
- 需要人力维护的项:
    1. 因为此脚本原理是获取所有的文字项目,所以必然存在很多有text但text并不符合要求的项目,所以需要人力进行一次描述修改,修改后的元素信息在后期同步时不会被再次修改
    2. 在每次进行数据维护时,需要将手机连接至电脑并且将待操作app打开至待同步的界面,在脚本中选择已有页面进行维护或输入新页面名称进行添加

## PluginsConf.py
- 此脚本为自动维护.plugin.PluginRootActivity活动中pluginId的插件
- 我们可用通过am start -n com.xiaomi.shop/com.xiaomi.shop2.plugin.PluginRootActivity --es pluginId {id} 命令来调起小米商城中的部分活动(应该与push的推送有关,个人感觉只要有推送过的页面就可以通过此方法跳转)
- 可查阅 Config\PluginsId.yml 文件中的id对应信息
- 此脚本会自动按id递加的形式从给定id开始向后寻找,如遇到非异常页面,则提示用户手动输入页面标题,所有信息都将被保存在 Config\PluginsId.yml 中

## Element_selector
- 文件夹包含两部分,各个页面的离线版布局元素和uiaotomatorviewer离线版
- 用户可用java打开 Plug-ins\Element_selector\uiautomatorviewer\uiautomatorviewer-standalone-1.1-all.jar (设置好Java变量)
  ``` 
  java -jar Plug-ins\Element_selector\uiautomatorviewer\uiautomatorviewer-standalone-1.1-all.jar
  ```
- 使用方法:
  1. 打开jar独立包
  2. 在ui左上角选择从文件打开
  3. 打开待查询页面对应的Page文件夹中的对应文件
  4. 使用鼠标选定元素,可在右边得到元素的信息