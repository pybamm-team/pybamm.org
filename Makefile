.PHONY: help themes html serve serve-dev clean teams
.DEFAULT_GOAL := help

help:
	@grep ": ##" Makefile | grep -v grep | tr -d '#'

themes/scientific-python-hugo-theme:
	@if [ ! -d "$<" ]; then \
	  echo "*** ERROR: missing theme" ; \
	  echo ; \
	  echo "It looks as though you are missing the themes directory."; \
	  echo "You need to add the scientific-python-hugo-theme as a submodule."; \
	  echo ; \
	  echo "Please see https://theme.scientific-python.org/getstarted/"; \
	  echo ; \
	  exit 1; \
	fi

themes: themes/scientific-python-hugo-theme

html: ## Build site in `./public`
html: themes
	hugo

serve: ## Serve site, typically on http://localhost:1313
serve: themes
	@hugo --printI18nWarnings server

serve-dev: ## Serve site during development, typically on http://localhost:1313
serve-dev: themes
	@hugo --printI18nWarnings server --disableFastRender

clean: ## Remove built files
clean:
	rm -rf public

teams: ## Generate team pages
teams: themes
	python3 scripts/generate_teams.py
