# Пререквизитс
* docker
* docker compose
* остальное должно само запулится при запуске компоуза

# Как запустить
```
./setup.sh
./launch.sh
```

Или 

```
docker compose -f compose.yaml -f compose.redash.yaml build
docker compose -f compose.redash.yaml run --rm server create_db

docker compose -f compose.yaml -f compose.redash.yaml up
```

Оба варианта делают одно и то же

# Дашборд

<img width="937" height="921" alt="image" src="https://github.com/user-attachments/assets/aa5ff4cb-46ff-4f48-8c5f-b92e7b1457cf" />
