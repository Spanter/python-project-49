install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

#Сборка пакета
build:
	poetry build

#Отладка публикации
publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

#Проверка проекта на качество кода
lint:
	poetry run flake8 brain_games
