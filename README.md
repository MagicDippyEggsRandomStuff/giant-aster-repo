# Aster Package Repository

This repository contains a comprehensive set of packages for the [Aster](docs.md) package manager, providing both pre-compiled binary (`-bin`) and source (`-src`) versions for popular command-line tools.

## Repository Contents

This repository hosts 90 package definitions covering popular CLI software, including:

- **bat** (`bat-bin`, `bat-src`) - A cat clone with syntax highlighting and Git integration
- **eza** (`eza-bin`, `eza-src`) - Modern replacement for `ls`
- **fastfetch** (`fastfetch-bin`, `fastfetch-src`) - Fast and lightweight system information tool
- **glow** (`glow-bin`, `glow-src`) - Markdown rendering on the CLI
- **ripgrep** (`ripgrep-bin`, `ripgrep-src`) - Fast line-oriented search tool
- **fd** (`fd-bin`, `fd-src`) - Simple, fast alternative to `find`
- **yazi** (`yazi-bin`, `yazi-src`) - Terminal file manager
- **starship** (`starship-bin`, `starship-src`) - Cross-shell prompt
- **zoxide** (`zoxide-bin`, `zoxide-src`) - Smarter `cd` command
- **lazygit** (`lazygit-bin`, `lazygit-src`) - Simple terminal UI for git
- **zellij** (`zellij-bin`, `zellij-src`) - Terminal workspace and multiplexer
- **uv** (`uv-bin`, `uv-src`) & **ruff** (`ruff-bin`, `ruff-src`) - Fast Python tooling
- **helix** (`helix-bin`, `helix-src`) - Post-modern modal text editor
- ...and many more!

## Usage Instructions

### 1. Add Repository to Aster

To add this repository to Aster, run:

```sh
# Remote HTTP/HTTPS URL
aster repo add main-repo https://raw.githubusercontent.com/user/aster-repo/main --priority 100

# Local Directory
aster repo add local-repo file:///path/to/repo --priority 100
```

### 2. Update Repository Catalog

Refresh Aster's repository catalog cache:

```sh
aster repo update
```

### 3. Install Packages

Search and install packages using Aster:

```sh
# Install binary version
aster install bat-bin

# Install source version
aster install bat-src
```

## Structure

- `index.json`: Repository index file cataloging all available packages.
- `packages/`: Directory containing JSON package definitions.
- `generate_repo.py`: Script used to build/maintain package definitions.
- `validate_repo.py`: Script used to validate schema and index references.
