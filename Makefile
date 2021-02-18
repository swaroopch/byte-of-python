# https://github.com/honkit/honkit
setup:
	npm install honkit --save-dev

serve:
	npx honkit serve

prettier_glob="**/*.{json,md,yml,yaml}"

lint:
	npx prettier --check "${prettier_glob}"

format:
	npx prettier --write "${prettier_glob}"
