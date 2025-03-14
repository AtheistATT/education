#!/bin/bash

if [[ -z "$GIT_USERNAME" || -z "$GIT_TOKEN" ]]; then
  echo "Ошибка: переменные окружения GIT_USERNAME и GIT_TOKEN не установлены."
  exit 1
fi

REPO_URL="https://${GIT_USERNAME}:${GIT_TOKEN}@github.com/ваш-username/ваш-репозиторий.git"

git add .

read -p "Введите сообщение для коммита: " commit_message

git commit -m "$commit_message"

git push $REPO_URL master

echo "Коммит выполнен и изменения отправлены в репозиторий."
