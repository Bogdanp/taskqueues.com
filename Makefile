.PHONY: all
all: build


.PHONY: build
build: build/index.html


.PHONY: deploy
deploy: build
	gcloud app deploy --project taskqueues-192117 app.yaml


.PHONY: watch
watch:
	watchmedo shell-command -Rwc "python build.py --config taskqueues.yml build/index.html"


build/index.html: taskqueues.yml template.html
	./build.py --config taskqueues.yml build/index.html
