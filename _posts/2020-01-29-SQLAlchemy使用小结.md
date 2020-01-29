---
layout: post
title: SQLAlchemy使用小结
subtitle: Flask+SQLAlchemy
author: Kingtous
date: 2020-01-29 17:49:49
header-img: img/post-bg-alitrip.jpg
catalog: True
tags:
- Flask
- Python
---

以下一个自己正在写的Flask项目。

Github链接：[接受API上传代码并返回结果的代码执行服务器](https://github.com/Kingtous/Flask-CodeRunningServer)

### SQLAlchemy

#### 初始化

SQLAlchemy通常与Flask框架进行绑定，以下用`app`表示框架

初始化分为以下几步

- 定义SQL数据库连接
- 修改SQLAlchemy配置
- 创建SQLAlchemy实例
- 创建SQL基类
- 创建SQL引擎
- 创建SQL Session Maker
    - 与`app`绑定
- 创建Session类
    - 使用Session()方法创建一个可与数据库通讯的session，注意要记得`close`

示例：

```python
app.config['SQLALCHEMY_DATABASE_URI'] = Cf.base_mysql_connection_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
db = SQLAlchemy(app)
Cf.database = db
Cf.SQLBase = declarative_base()
Cf.SQLEngine = create_engine(Cf.base_mysql_connection_url)
Cf.SQLSessionMaker = sessionmaker(bind=Cf.SQLEngine)
Cf.SQLSession = scoped_session(Cf.SQLSessionMaker)  # scoped_session保证线程安全
```

#### 增

- `data`为**继承上方示例中db.Model**的**类**的一个**实体**

```python
@staticmethod
def add_to_sql(data):
  session = Cf.SQLSession()
  session.add(data)
  session.commit()
  return session
```

#### 删

```python
@staticmethod
def delete_to_sql(data):
  session = Cf.SQLSession()
  session.delete(data)
  session.commit()
  return session
```

#### 改

- 通过`session.query()`查询得到要改的元素A，得到元素A的实体，直接修改A的属性后进行`session.commit()`即可

#### 查

以`get`方法分页，每页`10`篇帖子为例

示例：

```python
def get(self):
  args = self.parser.parse_args()
  page_num = int(args.get('page', None))
  if page_num is None or type(page_num) != int or page_num <= 0:
    return ResponseClass.warn(ResponseCode.FORMAT_ERROR)
  # 将page_num-1，适应计算
  page_num = page_num - 1
  session = AppUtils.get_session()
  from app.database_models import Threads
  threads = session.query(Threads).filter_by(user_id=g.user.id).offset(
    page_num * self.page_num_per_request).limit(
    self.page_num_per_request).all()
  threads = [tr.get_public_dict() for tr in threads]
  return ResponseClass.ok_with_data(threads)
```

注意：

- `filter_by`要在`offset`和`limit`前用
- `session`要`close`**！！！**保持良好习惯（比如上方的示例就忘了close(打脸)）
    - `close`要在对`query`获取的元素做完操作后进行，否则`close`掉后，`query`出来的类就不存在了
- `all()`返回所有，`first()`返回第一个