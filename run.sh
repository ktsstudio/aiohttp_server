cat config/heroku_config.yaml | envsubst > config/config.yaml
export PYTHONPATH=.
alembic upgrade head
python main.py