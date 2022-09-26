# 项目介绍
python写的一些工具

# excel工具
可以将数据库的数据，按照指定查询sql，导出至excel。

- db.properties

配置数据库的连接参数

- excel.properties

配置excel相关参数，并提供执行sql

- bean-map.properties

提供数据库字段与中文名的映射关系。

以如下sql为例

select `userName` from user

可以选择在bean-map中配置映射关系 userName=姓名

也可以不配置bean-map，但需要把sql改为 select `userName` as 姓名 from user 