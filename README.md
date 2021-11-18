# docker-flask-todos

練習用

## フォルダ構成

```
.
├── .env
├── Dockerfile
├── README.md
├── docker-compose.yml
├── requirements.txt
└── src
    ├── apis
    │   ├── __init__.py
    │   └── todos.py
    ├── app.py
    ├── dao
    │   ├── __init__.py
    │   └── todo.py
    ├── schema
    │   └── todo.py
    ├── templates
    │   ├── layout.html
    │   └── view.html
    ├── utils
    │   └── format.py
    └── view.py
```

## アプリケーション起動

イメージ作成
```
docker-compose build --no-cache
```

コンテナを起動
```
docker-compose up -d
```

コンテナの停止
```
docker-compose down
```

## アクセス方法

```
# View
http://localhost/view/

# swagger ui
http://localhost/doc/

# タスク一覧(raw data)
http://localhost/api/todos/

# IDでタスクを指定（例）
http://localhost/api/todos/12d6aaeb-4d4f-4b6a-9ee5-c8a0d9b68cba
```

## Operations

### POST

```
curl -X 'POST' \
  'http://localhost:5000/api/todos/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "task": "task01"
}'
```

Response Body

```
{
  "id": "12d6aaeb-4d4f-4b6a-9ee5-c8a0d9b68cba",
  "task": "task01",
  "created_at": "2021-11-18 19:00:38"
}
```

### GET /api/todos/

```
curl -X 'GET' \
  'http://localhost:5000/api/todos/' \
  -H 'accept: application/json'
```

Response Body

```
[
  {
    "id": "afe16e65-049a-4543-8d2b-550c8e59063c",
    "task": "PUT test",
    "created_at": "2021-11-18 18:58:30"
  },
  {
    "id": "476e052c-4b16-496d-b746-721adf040b8b",
    "task": "??????",
    "created_at": "2021-11-18 18:58:30"
  },
  {
    "id": "5419ace8-6a89-424c-918e-fc052aaafbcd",
    "task": "profit!",
    "created_at": "2021-11-18 18:58:30"
  }
]
```

### GET /api/todos/{id}

```
curl -X 'GET' \
  'http://localhost:5000/api/todos/12d6aaeb-4d4f-4b6a-9ee5-c8a0d9b68cba' \
  -H 'accept: application/json'
```

Response Body

```
{
  "id": "12d6aaeb-4d4f-4b6a-9ee5-c8a0d9b68cba",
  "task": "task01",
  "created_at": "2021-11-18 19:00:38"
}
```

### PUT /api/todos/{id}

```
curl -X 'PUT' \
  'http://localhost:5000/api/todos/afe16e65-049a-4543-8d2b-550c8e59063c' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "task": "PUT test"
}'
```

Response Body

```
{
  "id": "afe16e65-049a-4543-8d2b-550c8e59063c",
  "task": "PUT test",
  "created_at": "2021-11-18 18:58:30"
}
```

### DELETE /api/todos/{id}

```
curl -X 'DELETE' \
  'http://localhost:5000/api/todos/12d6aaeb-4d4f-4b6a-9ee5-c8a0d9b68cba' \
  -H 'accept: application/json'
```

## TODO

* View から GET/POST/PUT/DELETE を実行可能にする。

## 参考URL

* [DockerとDocker ComposeでPythonの実行環境を作成する](https://zuma-lab.com/posts/docker-python-settings)
* [Dockerfile + docker-compose.ymlでFlask環境構築](https://qiita.com/ayaka105/items/7f8428fa352bcd6e75e9)
* [Flask-RESTX でサンプルアプリケーションを作ってみた](https://qiita.com/kiyo27/items/d928f65b215d914f1979)
* [【Flask】JQueryでAjax通信をする手順。〜 JavaScript初心者向け 〜](https://sunnyday-travel-aso-6487.ssl-lolipop.jp/programing/python/flask/ajax/)