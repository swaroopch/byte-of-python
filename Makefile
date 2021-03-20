# https://github.com/honkit/honkit
setup:
	npm install honkit --save-dev

build:
	npx honkit build . public --log=debug

pdf:
	npx honkit pdf . byte-of-python.pdf

epub:
	npx honkit epub . byte-of-python.epub

serve:
	npx honkit serve
