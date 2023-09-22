.PHONY: \
	__run-build \
	clean \
	languages \
	run \
	run_local

SHELL = /bin/bash -euo pipefail

CLJ = clj
CPP =cpp
C = c
RS = rs
ZIG = zig
PY = py

SUPPORTED_LANGUAGES = \
	$(CLJ) \
	$(CPP) \
	$(C) \
	$(RS) \
	$(ZIG) \
	$(PY)

ifdef LANGUAGES
SUPPORTED_LANGUAGES := $(LANGUAGES)
endif

FOLDER_EXISTS = 0
ifneq ("$(wildcard $(FOLDER))","")
    FOLDER_EXISTS = 1
endif

ifdef FOLDER
	ifeq ("$(FOLDER_EXISTS)","1")
		FOLDERS := $(shell find $(FOLDER) -name 'problem.md' | sed 's/problem.md//g' | sort)
	endif
else
	FOLDERS := $(shell find . -name 'problem.md' | sed 's/problem.md//g' | sort)
endif

DOCKER_RUN := docker run -v $$(pwd):/code -u "$$(id -u):$$(id -g)"
DOCKER_BUILD := docker build -q -f

__run-build:
ifdef LANGUAGE
	$(error On run task, you should use LANGUAGES not LANGUAGE)
endif
	@for language in $(SUPPORTED_LANGUAGES); do \
		echo "Building $$language"; \
		$(DOCKER_BUILD) .docker/$$language.Dockerfile -t $$language .; \
	done

clean:
	@find . -name '*.class' -delete
	@find . -name '*.cml' -delete
	@find . -name '*.cmo' -delete
	@find . -name '*.exe' -delete
	@find . -name '*.hi' -delete
	@find . -name '*.o' -delete
	@find . -name '*.out' -delete
	@find . -name 'Main.java' -delete
	@find . -name 'result-*.txt' -delete
	@find . -type d -name "META-INF" -exec rm -rf {} +
	@find . -type d -name "\?" -exec rm -rf {} +

languages:
	@./scripts/languages.sh


run: clean __run-build
ifdef LANGUAGE
	$(error On run task, you should use LANGUAGES not LANGUAGE)
endif
	@scripts/run-problems.sh "$(FOLDERS)" "$(SUPPORTED_LANGUAGES)" "$(DOCKER_RUN)"

run_local: clean
ifdef LANGUAGE
	$(error On run task, you should use LANGUAGES not LANGUAGE)
endif
	@scripts/run-problems-local.sh "$(FOLDERS)" "$(SUPPORTED_LANGUAGES)" "$(DOCKER_RUN)"

wrong:
	@find . -name 'WRONG' | sort
