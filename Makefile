HONKIT := ./scripts/honkit

setup:
	$(HONKIT) --version

build:
	$(HONKIT) build . public --log=debug

pdf:
	$(HONKIT) pdf . byte-of-python.pdf

epub:
	$(HONKIT) epub . byte-of-python.epub

serve:
	$(HONKIT) serve
