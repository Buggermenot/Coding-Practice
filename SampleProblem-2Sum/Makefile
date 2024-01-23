TARGET := $(firstword $@,$(MAKECMDGOALS))
ARGS := $(wordlist 2,3,$(MAKECMDGOALS))


ECHO := @echo Running $(TARGET) file with arguments: $(ARGS)

py:
	$(ECHO)
	python Run_Files/Boiler.py $(ARGS)
sample:
	@:

%:
	@echo Incorrect input parameters. Do make py/cpp/c/java [sample]