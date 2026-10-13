# Aster Package Repository (`MagicDippyEggsRandomStuff/giant-aster-repo`)

This repository contains a comprehensive set of packages for the [Aster](docs.md) package manager, providing both pre-compiled binary (`-bin`) and source (`-src`) versions for popular command-line tools.

## Repository Contents

This repository hosts 217 package definitions covering popular CLI software, including:

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
- **btop** (`btop-bin`, `btop-src`) - Resource monitor for terminal
- **gitui** (`gitui-bin`, `gitui-src`) - Terminal UI for Git
- **atuin** (`atuin-bin`, `atuin-src`) - Shell history sync and search
- **ast-grep** (`ast-grep-bin`, `ast-grep-src`) - AST-based code search and linting
- **biome** (`biome-bin`, `biome-src`) - Web toolchain
- **difftastic** (`difftastic-bin`, `difftastic-src`) - Syntax-aware diff tool
- **silicon** (`silicon-bin`, `silicon-src`) - Code screenshot CLI tool
- **actionlint** (`actionlint-bin`, `actionlint-src`) - GitHub Actions workflow linter
- **superfile** (`superfile-bin`, `superfile-src`) - Modern terminal file manager
- **terraform** (`terraform-bin`), **packer** (`packer-bin`), **vault** (`vault-bin`) - HashiCorp DevOps tools
- **kubectl** (`kubectl-bin`), **k3d** (`k3d-bin`, `k3d-src`), **kind** (`kind-bin`, `kind-src`), **minikube** (`minikube-bin`), **argocd** (`argocd-bin`) - Kubernetes orchestration & GitOps tools
- **cosign** (`cosign-bin`, `cosign-src`), **syft** (`syft-bin`, `syft-src`), **grype** (`grype-bin`, `grype-src`), **trivy** (`trivy-bin`, `trivy-src`) - Security & SBOM utilities
- **bun** (`bun-bin`), **deno** (`deno-bin`, `deno-src`), **fnm** (`fnm-bin`, `fnm-src`), **mise** (`mise-bin`, `mise-src`) - JS runtimes & dev tool managers
- **zola** (`zola-bin`, `zola-src`), **mdbook** (`mdbook-bin`, `mdbook-src`), **wasm-pack** (`wasm-pack-bin`, `wasm-pack-src`), **trunk** (`trunk-bin`, `trunk-src`) - Static site & Rust WASM tools
- ...and many more!

## Usage Instructions

### 1. Add Repository to Aster

To add this repository to Aster, run:

```sh
# Remote HTTP/HTTPS URL
aster repo add main-repo https://raw.githubusercontent.com/MagicDippyEggsRandomStuff/giant-aster-repo/main --priority 100

# Local Directory
aster repo add local-repo file:///path/to/giant-aster-repo --priority 100
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
