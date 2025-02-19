.PHONY: all install config clean

INSTALL_PATH=/usr/local/bin
CONFIG_DIR=$(HOME)/.config/kowalski
CONFIG_FILE=$(CONFIG_DIR)/core.yaml

all: install config

install:
	@echo "Building and installing kowalski..."
	@mkdir -p release
	@go build -o release/ko
	@sudo mv release/ko $(INSTALL_PATH)/
	@echo "Installed ko to $(INSTALL_PATH)"

config:
	@if [ ! -f "$(CONFIG_FILE)" ]; then \
		echo "Creating config directory..."; \
		mkdir -p "$(CONFIG_DIR)"; \
		echo "Creating config template..."; \
		echo "notesPath: \"\"" > "$(CONFIG_FILE)"; \
		echo "editor: \"\"" >> "$(CONFIG_FILE)"; \
		echo "model: \"\"" >> "$(CONFIG_FILE)"; \
		echo "apiKey: \"\"" >> "$(CONFIG_FILE)"; \
		echo "Created $(CONFIG_FILE)"; \
		echo "Please edit $(CONFIG_FILE) to set your configuration"; \
	else \
		echo "Config file already exists at $(CONFIG_FILE)"; \
	fi

clean:
	@rm -rf release
