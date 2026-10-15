#!/usr/bin/env python3
import json
import os

# Definition of apps with metadata
APPS = [
    {
        "name": "bat",
        "version": "0.24.0",
        "description": "A cat(1) clone with syntax highlighting and Git integration",
        "homepage": "https://github.com/sharkdp/bat",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/sharkdp/bat/releases/download/v0.24.0/bat-v0.24.0-x86_64-unknown-linux-gnu.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/sharkdp/bat/releases/download/v0.24.0/bat-v0.24.0-aarch64-unknown-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/sharkdp/bat.git",
                "ref": "v0.24.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "bat"
            ]
        }
    },
    {
        "name": "eza",
        "version": "0.20.1",
        "description": "A modern, maintained replacement for ls",
        "homepage": "https://eza.rocks",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/eza-community/eza/releases/download/v0.20.1/eza_x86_64-unknown-linux-gnu.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/eza-community/eza/releases/download/v0.20.1/eza_aarch64-unknown-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/eza-community/eza.git",
                "ref": "v0.20.1"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "eza"
            ]
        }
    },
    {
        "name": "fastfetch",
        "version": "2.30.0",
        "description": "An opinionated, fast and lightweight system information tool",
        "homepage": "https://github.com/fastfetch-cli/fastfetch",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/fastfetch-cli/fastfetch/releases/download/2.30.0/fastfetch-linux-amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/fastfetch-cli/fastfetch/releases/download/2.30.0/fastfetch-linux-aarch64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/fastfetch-cli/fastfetch.git",
                "ref": "2.30.0"
            },
            "build": {
                "system": "cmake"
            }
        }
    },
    {
        "name": "glow",
        "version": "2.0.0",
        "description": "Render markdown on the CLI, with pizzazz!",
        "homepage": "https://github.com/charmbracelet/glow",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/charmbracelet/glow/releases/download/v2.0.0/glow_2.0.0_Linux_x86_64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/charmbracelet/glow/releases/download/v2.0.0/glow_2.0.0_Linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/charmbracelet/glow.git",
                "ref": "v2.0.0"
            },
            "build": {
                "steps": [
                    "go build -v -o glow"
                ]
            }
        }
    },
    {
        "name": "neofetch",
        "version": "7.1.0",
        "description": "A command-line system information tool written in bash 3.2+",
        "homepage": "https://github.com/dylanaraps/neofetch",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/dylanaraps/neofetch.git",
                "ref": "7.1.0"
            },
            "build": {
                "system": "make"
            }
        }
    },
    {
        "name": "ripgrep",
        "version": "14.1.0",
        "description": "A line-oriented search tool that recursively searches current directory for a regex pattern",
        "homepage": "https://github.com/BurntSushi/ripgrep",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/BurntSushi/ripgrep/releases/download/14.1.0/ripgrep-14.1.0-x86_64-unknown-linux-musl.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/BurntSushi/ripgrep/releases/download/14.1.0/ripgrep-14.1.0-aarch64-unknown-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/BurntSushi/ripgrep.git",
                "ref": "14.1.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "rg"
            ]
        }
    },
    {
        "name": "fd",
        "version": "10.2.0",
        "description": "A simple, fast and user-friendly alternative to find",
        "homepage": "https://github.com/sharkdp/fd",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/sharkdp/fd/releases/download/v10.2.0/fd-v10.2.0-x86_64-unknown-linux-gnu.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/sharkdp/fd/releases/download/v10.2.0/fd-v10.2.0-aarch64-unknown-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/sharkdp/fd.git",
                "ref": "v10.2.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "fd"
            ]
        }
    },
    {
        "name": "yazi",
        "version": "0.4.0",
        "description": "Blazing fast terminal file manager written in Rust, based on async I/O",
        "homepage": "https://github.com/sxyazi/yazi",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/sxyazi/yazi/releases/download/v0.4.0/yazi-x86_64-unknown-linux-gnu.zip"
                },
                "linux-aarch64": {
                    "url": "https://github.com/sxyazi/yazi/releases/download/v0.4.0/yazi-aarch64-unknown-linux-gnu.zip"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/sxyazi/yazi.git",
                "ref": "v0.4.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "yazi",
                "ya"
            ]
        }
    },
    {
        "name": "starship",
        "version": "1.21.0",
        "description": "The minimal, blazing-fast, and infinitely customizable prompt for any shell!",
        "homepage": "https://starship.rs",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/starship/starship/releases/download/v1.21.0/starship-x86_64-unknown-linux-gnu.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/starship/starship/releases/download/v1.21.0/starship-aarch64-unknown-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/starship/starship.git",
                "ref": "v1.21.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "starship"
            ]
        }
    },
    {
        "name": "zoxide",
        "version": "0.9.6",
        "description": "A smarter cd command, inspired by z and autojump",
        "homepage": "https://github.com/ajeetdsouza/zoxide",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/ajeetdsouza/zoxide/releases/download/v0.9.6/zoxide-0.9.6-x86_64-unknown-linux-musl.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/ajeetdsouza/zoxide/releases/download/v0.9.6/zoxide-0.9.6-aarch64-unknown-linux-musl.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/ajeetdsouza/zoxide.git",
                "ref": "v0.9.6"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "zoxide"
            ]
        }
    },
    {
        "name": "delta",
        "version": "0.18.2",
        "description": "A viewer for git and diff output",
        "homepage": "https://github.com/dandavison/delta",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/dandavison/delta/releases/download/0.18.2/delta-0.18.2-x86_64-unknown-linux-gnu.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/dandavison/delta/releases/download/0.18.2/delta-0.18.2-aarch64-unknown-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/dandavison/delta.git",
                "ref": "0.18.2"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "delta"
            ]
        }
    },
    {
        "name": "dust",
        "version": "1.1.1",
        "description": "A more intuitive version of du in rust",
        "homepage": "https://github.com/bootandy/dust",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/bootandy/dust/releases/download/v1.1.1/dust-v1.1.1-x86_64-unknown-linux-gnu.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/bootandy/dust/releases/download/v1.1.1/dust-v1.1.1-aarch64-unknown-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/bootandy/dust.git",
                "ref": "v1.1.1"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "dust"
            ]
        }
    },
    {
        "name": "bottom",
        "version": "0.10.2",
        "description": "A customizable cross-platform graphical process/system monitor for the terminal",
        "homepage": "https://github.com/ClementTsang/bottom",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/ClementTsang/bottom/releases/download/0.10.2/bottom_x86_64-unknown-linux-gnu.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/ClementTsang/bottom/releases/download/0.10.2/bottom_aarch64-unknown-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/ClementTsang/bottom.git",
                "ref": "0.10.2"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "btm"
            ]
        }
    },
    {
        "name": "procs",
        "version": "0.14.8",
        "description": "A modern replacement for ps written in Rust",
        "homepage": "https://github.com/dalance/procs",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/dalance/procs/releases/download/v0.14.8/procs-v0.14.8-x86_64-linux.zip"
                },
                "linux-aarch64": {
                    "url": "https://github.com/dalance/procs/releases/download/v0.14.8/procs-v0.14.8-aarch64-linux.zip"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/dalance/procs.git",
                "ref": "v0.14.8"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "procs"
            ]
        }
    },
    {
        "name": "tealdeer",
        "version": "1.7.1",
        "description": "A very fast implementation of tldr in Rust",
        "homepage": "https://github.com/dbrgn/tealdeer",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/dbrgn/tealdeer/releases/download/v1.7.1/tldr-x86_64-unknown-linux-musl"
                },
                "linux-aarch64": {
                    "url": "https://github.com/dbrgn/tealdeer/releases/download/v1.7.1/tldr-aarch64-unknown-linux-musl"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/dbrgn/tealdeer.git",
                "ref": "v1.7.1"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "tldr"
            ]
        }
    },
    {
        "name": "hyperfine",
        "version": "1.18.0",
        "description": "A command-line benchmarking tool",
        "homepage": "https://github.com/sharkdp/hyperfine",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/sharkdp/hyperfine/releases/download/v1.18.0/hyperfine-v1.18.0-x86_64-unknown-linux-gnu.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/sharkdp/hyperfine/releases/download/v1.18.0/hyperfine-v1.18.0-aarch64-unknown-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/sharkdp/hyperfine.git",
                "ref": "v1.18.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "hyperfine"
            ]
        }
    },
    {
        "name": "tokei",
        "version": "12.1.2",
        "description": "A program that displays statistics about your code",
        "homepage": "https://github.com/Xaeroxe/tokei",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/Xaeroxe/tokei/releases/download/v12.1.2/tokei-x86_64-unknown-linux-gnu.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/Xaeroxe/tokei/releases/download/v12.1.2/tokei-aarch64-unknown-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/Xaeroxe/tokei.git",
                "ref": "v12.1.2"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "tokei"
            ]
        }
    },
    {
        "name": "zellij",
        "version": "0.41.2",
        "description": "A terminal workspace with batteries included",
        "homepage": "https://zellij.dev",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/zellij-org/zellij/releases/download/v0.41.2/zellij-x86_64-unknown-linux-musl.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/zellij-org/zellij/releases/download/v0.41.2/zellij-aarch64-unknown-linux-musl.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/zellij-org/zellij.git",
                "ref": "v0.41.2"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "zellij"
            ]
        }
    },
    {
        "name": "lazygit",
        "version": "0.44.1",
        "description": "Simple terminal UI for git commands",
        "homepage": "https://github.com/jesseduffield/lazygit",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/jesseduffield/lazygit/releases/download/v0.44.1/lazygit_0.44.1_Linux_x86_64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/jesseduffield/lazygit/releases/download/v0.44.1/lazygit_0.44.1_Linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/jesseduffield/lazygit.git",
                "ref": "v0.44.1"
            },
            "build": {
                "steps": [
                    "go build -v -o lazygit"
                ]
            }
        }
    },
    {
        "name": "lazydocker",
        "version": "0.23.1",
        "description": "A simple terminal UI for docker and docker-compose",
        "homepage": "https://github.com/jesseduffield/lazydocker",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/jesseduffield/lazydocker/releases/download/v0.23.1/lazydocker_0.23.1_Linux_x86_64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/jesseduffield/lazydocker/releases/download/v0.23.1/lazydocker_0.23.1_Linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/jesseduffield/lazydocker.git",
                "ref": "v0.23.1"
            },
            "build": {
                "steps": [
                    "go build -v -o lazydocker"
                ]
            }
        }
    },
    {
        "name": "gh",
        "version": "2.61.0",
        "description": "GitHub\u2019s official command line tool",
        "homepage": "https://cli.github.com",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/cli/cli/releases/download/v2.61.0/gh_2.61.0_linux_amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/cli/cli/releases/download/v2.61.0/gh_2.61.0_linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/cli/cli.git",
                "ref": "v2.61.0"
            },
            "build": {
                "steps": [
                    "make"
                ]
            }
        }
    },
    {
        "name": "fzf",
        "version": "0.56.0",
        "description": "A command-line fuzzy finder",
        "homepage": "https://github.com/junegunn/fzf",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/junegunn/fzf/releases/download/v0.56.0/fzf-0.56.0-linux_amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/junegunn/fzf/releases/download/v0.56.0/fzf-0.56.0-linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/junegunn/fzf.git",
                "ref": "v0.56.0"
            },
            "build": {
                "steps": [
                    "go build -v -o fzf"
                ]
            }
        }
    },
    {
        "name": "yq",
        "version": "4.44.5",
        "description": "a portable command-line YAML, JSON, XML, CSV, TOML and properties processor",
        "homepage": "https://github.com/mikefarah/yq",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/mikefarah/yq/releases/download/v4.44.5/yq_linux_amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/mikefarah/yq/releases/download/v4.44.5/yq_linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/mikefarah/yq.git",
                "ref": "v4.44.5"
            },
            "build": {
                "steps": [
                    "go build -v -o yq"
                ]
            }
        }
    },
    {
        "name": "gum",
        "version": "0.14.5",
        "description": "A tool for glamorous shell scripts",
        "homepage": "https://github.com/charmbracelet/gum",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/charmbracelet/gum/releases/download/v0.14.5/gum_0.14.5_Linux_x86_64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/charmbracelet/gum/releases/download/v0.14.5/gum_0.14.5_Linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/charmbracelet/gum.git",
                "ref": "v0.14.5"
            },
            "build": {
                "steps": [
                    "go build -v -o gum"
                ]
            }
        }
    },
    {
        "name": "vhs",
        "version": "0.8.0",
        "description": "Your CLI home video recorder",
        "homepage": "https://github.com/charmbracelet/vhs",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/charmbracelet/vhs/releases/download/v0.8.0/vhs_0.8.0_Linux_x86_64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/charmbracelet/vhs/releases/download/v0.8.0/vhs_0.8.0_Linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/charmbracelet/vhs.git",
                "ref": "v0.8.0"
            },
            "build": {
                "steps": [
                    "go build -v -o vhs"
                ]
            }
        }
    },
    {
        "name": "lsd",
        "version": "1.1.5",
        "description": "The next generation ls command",
        "homepage": "https://github.com/lsd-rs/lsd",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/lsd-rs/lsd/releases/download/v1.1.5/lsd-v1.1.5-x86_64-unknown-linux-gnu.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/lsd-rs/lsd/releases/download/v1.1.5/lsd-v1.1.5-aarch64-unknown-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/lsd-rs/lsd.git",
                "ref": "v1.1.5"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "lsd"
            ]
        }
    },
    {
        "name": "age",
        "version": "1.2.0",
        "description": "A simple, modern and secure file encryption tool",
        "homepage": "https://github.com/FiloSottile/age",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/FiloSottile/age/releases/download/v1.2.0/age-v1.2.0-linux-amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/FiloSottile/age/releases/download/v1.2.0/age-v1.2.0-linux-arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/FiloSottile/age.git",
                "ref": "v1.2.0"
            },
            "build": {
                "steps": [
                    "go build -v -o age ./cmd/age",
                    "go build -v -o age-keygen ./cmd/age-keygen"
                ]
            }
        }
    },
    {
        "name": "scc",
        "version": "3.3.5",
        "description": "Sloc, Cloc and Code: a fast language counter",
        "homepage": "https://github.com/boyter/scc",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/boyter/scc/releases/download/v3.3.5/scc_Linux_x86_64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/boyter/scc/releases/download/v3.3.5/scc_Linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/boyter/scc.git",
                "ref": "v3.3.5"
            },
            "build": {
                "steps": [
                    "go build -v -o scc"
                ]
            }
        }
    },
    {
        "name": "duf",
        "version": "0.8.1",
        "description": "Disk Usage/Free Utility - a better 'df' alternative",
        "homepage": "https://github.com/muesli/duf",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/muesli/duf/releases/download/v0.8.1/duf_0.8.1_linux_x86_64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/muesli/duf/releases/download/v0.8.1/duf_0.8.1_linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/muesli/duf.git",
                "ref": "v0.8.1"
            },
            "build": {
                "steps": [
                    "go build -v -o duf"
                ]
            }
        }
    },
    {
        "name": "croc",
        "version": "10.0.12",
        "description": "Easily and securely transfer stuff from one computer to another",
        "homepage": "https://github.com/schollz/croc",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/schollz/croc/releases/download/v10.0.12/croc_v10.0.12_Linux-64bit.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/schollz/croc/releases/download/v10.0.12/croc_v10.0.12_Linux-ARM64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/schollz/croc.git",
                "ref": "v10.0.12"
            },
            "build": {
                "steps": [
                    "go build -v -o croc"
                ]
            }
        }
    },
    {
        "name": "navi",
        "version": "2.23.0",
        "description": "An interactive cheatsheet tool for the command-line",
        "homepage": "https://github.com/denisidoro/navi",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/denisidoro/navi/releases/download/v2.23.0/navi-v2.23.0-x86_64-unknown-linux-musl.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/denisidoro/navi/releases/download/v2.23.0/navi-v2.23.0-aarch64-unknown-linux-musl.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/denisidoro/navi.git",
                "ref": "v2.23.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "navi"
            ]
        }
    },
    {
        "name": "watchexec",
        "version": "2.1.2",
        "description": "Executes commands in response to file modifications",
        "homepage": "https://github.com/watchexec/watchexec",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/watchexec/watchexec/releases/download/v2.1.2/watchexec-2.1.2-x86_64-unknown-linux-gnu.tar.xz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/watchexec/watchexec/releases/download/v2.1.2/watchexec-2.1.2-aarch64-unknown-linux-gnu.tar.xz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/watchexec/watchexec.git",
                "ref": "v2.1.2"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "watchexec"
            ]
        }
    },
    {
        "name": "typst",
        "version": "0.12.0",
        "description": "A new markup-based typesetting system that is powerful and easy to learn",
        "homepage": "https://typst.app",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/typst/typst/releases/download/v0.12.0/typst-x86_64-unknown-linux-musl.tar.xz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/typst/typst/releases/download/v0.12.0/typst-aarch64-unknown-linux-musl.tar.xz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/typst/typst.git",
                "ref": "v0.12.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "typst"
            ]
        }
    },
    {
        "name": "ruff",
        "version": "0.7.3",
        "description": "An extremely fast Python linter and code formatter, written in Rust",
        "homepage": "https://github.com/astral-sh/ruff",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/astral-sh/ruff/releases/download/0.7.3/ruff-x86_64-unknown-linux-gnu.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/astral-sh/ruff/releases/download/0.7.3/ruff-aarch64-unknown-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/astral-sh/ruff.git",
                "ref": "0.7.3"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "ruff"
            ]
        }
    },
    {
        "name": "uv",
        "version": "0.4.30",
        "description": "An extremely fast Python package and project manager, written in Rust",
        "homepage": "https://github.com/astral-sh/uv",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/astral-sh/uv/releases/download/0.4.30/uv-x86_64-unknown-linux-gnu.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/astral-sh/uv/releases/download/0.4.30/uv-aarch64-unknown-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/astral-sh/uv.git",
                "ref": "0.4.30"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "uv",
                "uvx"
            ]
        }
    },
    {
        "name": "just",
        "version": "1.36.0",
        "description": "Just a command runner",
        "homepage": "https://github.com/casey/just",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/casey/just/releases/download/1.36.0/just-1.36.0-x86_64-unknown-linux-musl.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/casey/just/releases/download/1.36.0/just-1.36.0-aarch64-unknown-linux-musl.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/casey/just.git",
                "ref": "1.36.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "just"
            ]
        }
    },
    {
        "name": "helix",
        "version": "25.01",
        "description": "A post-modern modal text editor",
        "homepage": "https://helix-editor.com",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/helix-editor/helix/releases/download/25.01/helix-25.01-x86_64-linux.tar.xz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/helix-editor/helix/releases/download/25.01/helix-25.01-aarch64-linux.tar.xz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/helix-editor/helix.git",
                "ref": "25.01"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "hx"
            ]
        }
    },
    {
        "name": "nushell",
        "version": "0.99.1",
        "description": "A new type of shell",
        "homepage": "https://www.nushell.sh",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/nushell/nushell/releases/download/0.99.1/nu-0.99.1-x86_64-unknown-linux-musl.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/nushell/nushell/releases/download/0.99.1/nu-0.99.1-aarch64-unknown-linux-musl.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/nushell/nushell.git",
                "ref": "0.99.1"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "nu"
            ]
        }
    },
    {
        "name": "git-cliff",
        "version": "2.6.1",
        "description": "A highly customizable changelog generator that follows Conventional Commits specifications",
        "homepage": "https://git-cliff.org",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/orhun/git-cliff/releases/download/v2.6.1/git-cliff-2.6.1-x86_64-unknown-linux-gnu.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/orhun/git-cliff/releases/download/v2.6.1/git-cliff-2.6.1-aarch64-unknown-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/orhun/git-cliff.git",
                "ref": "v2.6.1"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "git-cliff"
            ]
        }
    },
    {
        "name": "bandwhich",
        "version": "0.23.0",
        "description": "Terminal bandwidth utilization tool",
        "homepage": "https://github.com/imsnif/bandwhich",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/imsnif/bandwhich/releases/download/v0.23.0/bandwhich-v0.23.0-x86_64-unknown-linux-musl.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/imsnif/bandwhich/releases/download/v0.23.0/bandwhich-v0.23.0-aarch64-unknown-linux-musl.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/imsnif/bandwhich.git",
                "ref": "v0.23.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "bandwhich"
            ]
        }
    },
    {
        "name": "grex",
        "version": "1.4.5",
        "description": "A command-line tool and library for generating regular expressions from user-provided test cases",
        "homepage": "https://github.com/pemistahl/grex",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/pemistahl/grex/releases/download/v1.4.5/grex-v1.4.5-x86_64-unknown-linux-musl.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/pemistahl/grex/releases/download/v1.4.5/grex-v1.4.5-aarch64-unknown-linux-musl.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/pemistahl/grex.git",
                "ref": "v1.4.5"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "grex"
            ]
        }
    },
    {
        "name": "xh",
        "version": "0.23.0",
        "description": "Friendly and fast tool for sending HTTP requests",
        "homepage": "https://github.com/ducaale/xh",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/ducaale/xh/releases/download/v0.23.0/xh-v0.23.0-x86_64-unknown-linux-musl.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/ducaale/xh/releases/download/v0.23.0/xh-v0.23.0-aarch64-unknown-linux-musl.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/ducaale/xh.git",
                "ref": "v0.23.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "xh"
            ]
        }
    },
    {
        "name": "doggo",
        "version": "1.0.5",
        "description": "Command-line DNS client for Humans",
        "homepage": "https://github.com/mr-karan/doggo",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/mr-karan/doggo/releases/download/v1.0.5/doggo_1.0.5_Linux_x86_64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/mr-karan/doggo/releases/download/v1.0.5/doggo_1.0.5_Linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/mr-karan/doggo.git",
                "ref": "v1.0.5"
            },
            "build": {
                "steps": [
                    "go build -v -o doggo ./cmd/doggo"
                ]
            }
        }
    },
    {
        "name": "htop",
        "version": "3.3.0",
        "description": "An interactive process viewer",
        "homepage": "https://htop.dev",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/htop-dev/htop.git",
                "ref": "3.3.0"
            },
            "build": {
                "steps": [
                    "./autogen.sh",
                    "./configure",
                    "make"
                ]
            }
        }
    },
    {
        "name": "tmux",
        "version": "3.5a",
        "description": "A terminal multiplexer",
        "homepage": "https://github.com/tmux/tmux",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/tmux/tmux.git",
                "ref": "3.5a"
            },
            "build": {
                "steps": [
                    "autogen.sh",
                    "./configure",
                    "make"
                ]
            }
        }
    },
    {
        "name": "jq",
        "version": "1.7.1",
        "description": "Command-line JSON processor",
        "homepage": "https://jqlang.github.io/jq/",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/jqlang/jq/releases/download/jq-1.7.1/jq-linux-amd64"
                },
                "linux-aarch64": {
                    "url": "https://github.com/jqlang/jq/releases/download/jq-1.7.1/jq-linux-arm64"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/jqlang/jq.git",
                "ref": "jq-1.7.1"
            },
            "build": {
                "steps": [
                    "./autoreconf -i",
                    "./configure",
                    "make"
                ]
            }
        }
    },
    {
        "name": "tree",
        "version": "2.1.1",
        "description": "Recursive directory listing program",
        "homepage": "https://oldmanhook.github.io/unix-tree/",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/OldManHook/unix-tree.git",
                "ref": "2.1.1"
            },
            "build": {
                "system": "make"
            }
        }
    },
    {
        "name": "btop",
        "version": "1.3.2",
        "description": "A monitor of resources that displays usage and stats for processor, memory, disks, network and processes",
        "homepage": "https://github.com/aristocratos/btop",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/aristocratos/btop/releases/download/v1.3.2/btop-x86_64-linux-musl.tbz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/aristocratos/btop/releases/download/v1.3.2/btop-aarch64-linux-musl.tbz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/aristocratos/btop.git",
                "ref": "v1.3.2"
            },
            "build": {
                "system": "make"
            }
        }
    },
    {
        "name": "gitui",
        "version": "0.26.3",
        "description": "Blazing \ud83d\ude80 fast terminal-ui for git written in rust \ud83e\udd80",
        "homepage": "https://github.com/extrawurst/gitui",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/extrawurst/gitui/releases/download/v0.26.3/gitui-linux-x86_64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/extrawurst/gitui/releases/download/v0.26.3/gitui-linux-aarch64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/extrawurst/gitui.git",
                "ref": "v0.26.3"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "gitui"
            ]
        }
    },
    {
        "name": "atuin",
        "version": "18.3.0",
        "description": "Magical shell history",
        "homepage": "https://github.com/atuinsh/atuin",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/atuinsh/atuin/releases/download/v18.3.0/atuin-x86_64-unknown-linux-gnu.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/atuinsh/atuin/releases/download/v18.3.0/atuin-aarch64-unknown-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/atuinsh/atuin.git",
                "ref": "v18.3.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "atuin"
            ]
        }
    },
    {
        "name": "sd",
        "version": "1.0.0",
        "description": "Intuitive find & replace CLI (sed alternative)",
        "homepage": "https://github.com/chmln/sd",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/chmln/sd/releases/download/v1.0.0/sd-v1.0.0-x86_64-unknown-linux-musl.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/chmln/sd.git",
                "ref": "v1.0.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "sd"
            ]
        }
    },
    {
        "name": "choose",
        "version": "1.3.4",
        "description": "A human-friendly and fast alternative to cut and (sometimes) awk",
        "homepage": "https://github.com/theryangeary/choose",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/theryangeary/choose/releases/download/v1.3.4/choose-x86_64-unknown-linux-gnu"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/theryangeary/choose.git",
                "ref": "v1.3.4"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "choose"
            ]
        }
    },
    {
        "name": "onefetch",
        "version": "2.22.0",
        "description": "Command-line Git information tool",
        "homepage": "https://github.com/o2sh/onefetch",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/o2sh/onefetch/releases/download/2.22.0/onefetch-linux-x86_64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/o2sh/onefetch/releases/download/2.22.0/onefetch-linux-aarch64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/o2sh/onefetch.git",
                "ref": "2.22.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "onefetch"
            ]
        }
    },
    {
        "name": "bacon",
        "version": "3.4.0",
        "description": "Background rust code checker",
        "homepage": "https://github.com/Canop/bacon",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/Canop/bacon/releases/download/v3.4.0/bacon-v3.4.0-x86_64-linux.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/Canop/bacon.git",
                "ref": "v3.4.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "bacon"
            ]
        }
    },
    {
        "name": "trippy",
        "version": "0.12.0",
        "description": "A network diagnostic tool (trip)",
        "homepage": "https://github.com/fujiapple852/trippy",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/fujiapple852/trippy/releases/download/0.12.0/trippy-0.12.0-x86_64-unknown-linux-musl.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/fujiapple852/trippy/releases/download/0.12.0/trippy-0.12.0-aarch64-unknown-linux-musl.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/fujiapple852/trippy.git",
                "ref": "0.12.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "trip"
            ]
        }
    },
    {
        "name": "gping",
        "version": "1.17.3",
        "description": "Ping, but with a graph",
        "homepage": "https://github.com/orf/gping",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/orf/gping/releases/download/gping-v1.17.3/gping-Linux-x86_64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/orf/gping/releases/download/gping-v1.17.3/gping-Linux-arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/orf/gping.git",
                "ref": "gping-v1.17.3"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "gping"
            ]
        }
    },
    {
        "name": "numbat",
        "version": "1.14.0",
        "description": "A statically typed programming language for scientific computations with first-class support for physical dimensions and units",
        "homepage": "https://numbat.dev",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/sharkdp/numbat/releases/download/v1.14.0/numbat-v1.14.0-x86_64-unknown-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/sharkdp/numbat.git",
                "ref": "v1.14.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "numbat"
            ]
        }
    },
    {
        "name": "ast-grep",
        "version": "0.33.0",
        "description": "A CLI tool for code structural search, lint and rewriting",
        "homepage": "https://ast-grep.github.io",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/ast-grep/ast-grep/releases/download/v0.33.0/ast-grep-x86_64-unknown-linux-gnu.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/ast-grep/ast-grep/releases/download/v0.33.0/ast-grep-aarch64-unknown-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/ast-grep/ast-grep.git",
                "ref": "v0.33.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "ast-grep",
                "sg"
            ]
        }
    },
    {
        "name": "biome",
        "version": "1.9.4",
        "description": "A toolchain for web projects (linter, formatter, and more)",
        "homepage": "https://biomejs.dev",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/biomejs/biome/releases/download/cli%2Fv1.9.4/biome-linux-x64"
                },
                "linux-aarch64": {
                    "url": "https://github.com/biomejs/biome/releases/download/cli%2Fv1.9.4/biome-linux-arm64"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/biomejs/biome.git",
                "ref": "cli/v1.9.4"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "biome"
            ]
        }
    },
    {
        "name": "taplo",
        "version": "0.9.3",
        "description": "A versatile TOML toolkit",
        "homepage": "https://taplo.tamasfe.dev",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/tamasfe/taplo/releases/download/0.9.3/taplo-full-linux-x86_64.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/tamasfe/taplo.git",
                "ref": "0.9.3"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "taplo"
            ]
        }
    },
    {
        "name": "shfmt",
        "version": "3.10.0",
        "description": "A shell parser, formatter, and interpreter",
        "homepage": "https://github.com/mvdan/sh",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/mvdan/sh/releases/download/v3.10.0/shfmt_v3.10.0_linux_amd64"
                },
                "linux-aarch64": {
                    "url": "https://github.com/mvdan/sh/releases/download/v3.10.0/shfmt_v3.10.0_linux_arm64"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/mvdan/sh.git",
                "ref": "v3.10.0"
            },
            "build": {
                "steps": [
                    "go build -v -o shfmt ./cmd/shfmt"
                ]
            }
        }
    },
    {
        "name": "shellcheck",
        "version": "0.10.0",
        "description": "ShellCheck, a static analysis tool for shell scripts",
        "homepage": "https://www.shellcheck.net",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/koalaman/shellcheck/releases/download/v0.10.0/shellcheck-v0.10.0.linux.x86_64.tar.xz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/koalaman/shellcheck/releases/download/v0.10.0/shellcheck-v0.10.0.linux.aarch64.tar.xz"
                }
            }
        }
    },
    {
        "name": "difftastic",
        "version": "0.60.0",
        "description": "A structural diff tool that compares files based on their syntax",
        "homepage": "https://github.com/Wilfred/difftastic",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/Wilfred/difftastic/releases/download/0.60.0/difft-x86_64-unknown-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/Wilfred/difftastic.git",
                "ref": "0.60.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "difft"
            ]
        }
    },
    {
        "name": "silicon",
        "version": "0.5.2",
        "description": "Create beautiful images of your source code",
        "homepage": "https://github.com/Aloxaf/silicon",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/Aloxaf/silicon/releases/download/v0.5.2/silicon-v0.5.2-x86_64-unknown-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/Aloxaf/silicon.git",
                "ref": "v0.5.2"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "silicon"
            ]
        }
    },
    {
        "name": "zellij-runner",
        "version": "0.1.0",
        "description": "Runner helper for Zellij workspace terminal",
        "homepage": "https://github.com/zellij-org/zellij",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/zellij-org/zellij.git",
                "ref": "main"
            },
            "build": {
                "system": "cargo",
                "release": True
            },
            "executables": [
                "zellij"
            ]
        }
    },
    {
        "name": "yq-go",
        "version": "4.44.5",
        "description": "Go implementation of yq yaml processor",
        "homepage": "https://github.com/mikefarah/yq",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/mikefarah/yq.git",
                "ref": "v4.44.5"
            },
            "build": {
                "steps": [
                    "go build -v -o yq"
                ]
            }
        }
    },
    {
        "name": "actionlint",
        "version": "1.7.4",
        "description": "Static checker for GitHub Actions workflow files",
        "homepage": "https://github.com/rhysd/actionlint",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/rhysd/actionlint/releases/download/v1.7.4/actionlint_1.7.4_linux_amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/rhysd/actionlint/releases/download/v1.7.4/actionlint_1.7.4_linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/rhysd/actionlint.git",
                "ref": "v1.7.4"
            },
            "build": {
                "steps": [
                    "go build -v -o actionlint ./cmd/actionlint"
                ]
            }
        }
    },
    {
        "name": "superfile",
        "version": "1.6.0",
        "description": "Fancy and modern terminal file manager",
        "homepage": "https://github.com/yorukot/superfile",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/yorukot/superfile/releases/download/v1.6.0/superfile-linux-v1.6.0-amd64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/yorukot/superfile.git",
                "ref": "v1.6.0"
            },
            "build": {
                "steps": [
                    "go build -v -o spf"
                ]
            }
        }
    },
    {
        "name": "existence",
        "version": "latest",
        "description": "We are existing.",
        "homepage": "https://github.com/existence-REAL/existence",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/existence-REAL/existence/releases/download/latest/existence-linux-x86_64"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/existence-REAL/existence.git",
                "ref": "main"
            },
            "build": {
                "steps": [
                    "python3 -m venv .venv",
                    ".venv/bin/pip install pyinstaller",
                    ".venv/bin/pyinstaller --onefile existence.py --name existence"
                ]
            }
        }
    },
    {
        "name": "wine",
        "version": "9.0",
        "description": "Compatibility layer capable of running Windows applications on Unix-like operating systems",
        "homepage": "https://www.winehq.org",
        "src": {
            "source": {
                "type": "git",
                "url": "https://gitlab.winehq.org/wine/wine.git",
                "ref": "wine-9.0"
            },
            "build": {
                "steps": [
                    "./configure",
                    "make"
                ]
            }
        }
    },
    {
        "name": "neovim",
        "version": "0.10.3",
        "description": "Vim-fork focused on extensibility and usability",
        "homepage": "https://neovim.io",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/neovim/neovim/releases/download/v0.10.3/nvim-linux-x86_64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/neovim/neovim/releases/download/v0.10.3/nvim-linux-arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/neovim/neovim.git",
                "ref": "v0.10.3"
            },
            "build": {
                "system": "cmake"
            }
        }
    },
    {
        "name": "ffmpeg",
        "version": "7.1",
        "description": "A complete, cross-platform solution to record, convert and stream audio and video",
        "homepage": "https://ffmpeg.org",
        "src": {
            "source": {
                "type": "git",
                "url": "https://git.ffmpeg.org/ffmpeg.git",
                "ref": "n7.1"
            },
            "build": {
                "steps": [
                    "./configure",
                    "make"
                ]
            }
        }
    },
    {
        "name": "caddy",
        "version": "2.8.4",
        "description": "Fast and extensible multi-platform HTTP/2 web server with automatic HTTPS",
        "homepage": "https://caddyserver.com",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/caddyserver/caddy/releases/download/v2.8.4/caddy_2.8.4_linux_amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/caddyserver/caddy/releases/download/v2.8.4/caddy_2.8.4_linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/caddyserver/caddy.git",
                "ref": "v2.8.4"
            },
            "build": {
                "steps": [
                    "go build -v -o caddy ./cmd/caddy"
                ]
            }
        }
    },
    {
        "name": "k9s",
        "version": "0.32.7",
        "description": "Kubernetes CLI To Manage Your Clusters In Style!",
        "homepage": "https://k9scli.io",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/derailed/k9s/releases/download/v0.32.7/k9s_Linux_amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/derailed/k9s/releases/download/v0.32.7/k9s_Linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/derailed/k9s.git",
                "ref": "v0.32.7"
            },
            "build": {
                "steps": [
                    "go build -v -o k9s"
                ]
            }
        }
    },
    {
        "name": "helm",
        "version": "3.16.3",
        "description": "The Kubernetes Package Manager",
        "homepage": "https://helm.sh",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://get.helm.sh/helm-v3.16.3-linux-amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://get.helm.sh/helm-v3.16.3-linux-arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/helm/helm.git",
                "ref": "v3.16.3"
            },
            "build": {
                "steps": [
                    "go build -v -o helm ./cmd/helm"
                ]
            }
        }
    },
    {
        "name": "hugo",
        "version": "0.139.3",
        "description": "The world's fastest framework for building websites",
        "homepage": "https://gohugo.io",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/gohugoio/hugo/releases/download/v0.139.3/hugo_0.139.3_linux-amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/gohugoio/hugo/releases/download/v0.139.3/hugo_0.139.3_linux-arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/gohugoio/hugo.git",
                "ref": "v0.139.3"
            },
            "build": {
                "steps": [
                    "go build -v -o hugo"
                ]
            }
        }
    },
    {
        "name": "lazysql",
        "version": "0.2.7",
        "description": "A terminal UI for RDBMS written in Go",
        "homepage": "https://github.com/jorgerojas26/lazysql",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/jorgerojas26/lazysql/releases/download/v0.2.7/lazysql_Linux_x86_64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/jorgerojas26/lazysql/releases/download/v0.2.7/lazysql_Linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/jorgerojas26/lazysql.git",
                "ref": "v0.2.7"
            },
            "build": {
                "steps": [
                    "go build -v -o lazysql"
                ]
            }
        }
    },
    {
        "name": "dive",
        "version": "0.12.0",
        "description": "A tool for exploring a docker image, layer contents, and discovering ways to shrink your image size",
        "homepage": "https://github.com/wagoodman/dive",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/wagoodman/dive/releases/download/v0.12.0/dive_0.12.0_linux_amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/wagoodman/dive/releases/download/v0.12.0/dive_0.12.0_linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/wagoodman/dive.git",
                "ref": "v0.12.0"
            },
            "build": {
                "steps": [
                    "go build -v -o dive"
                ]
            }
        }
    },
    {
        "name": "act",
        "version": "0.2.70",
        "description": "Run your GitHub Actions locally!",
        "homepage": "https://github.com/nektos/act",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/nektos/act/releases/download/v0.2.70/act_Linux_x86_64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/nektos/act/releases/download/v0.2.70/act_Linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/nektos/act.git",
                "ref": "v0.2.70"
            },
            "build": {
                "steps": [
                    "go build -v -o act"
                ]
            }
        }
    },
    {
        "name": "czkawka",
        "version": "7.0.0",
        "description": "Multi functional app to find duplicates, empty folders, similar images etc.",
        "homepage": "https://github.com/qarmin/czkawka",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/qarmin/czkawka/releases/download/7.0.0/czkawka_cli"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/qarmin/czkawka.git",
                "ref": "7.0.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "czkawka_cli"
            ]
        }
    },
    {
        "name": "micro",
        "version": "2.0.14",
        "description": "A modern and intuitive terminal-based text editor",
        "homepage": "https://micro-editor.github.io",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/zyedidia/micro/releases/download/v2.0.14/micro-2.0.14-linux64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/zyedidia/micro/releases/download/v2.0.14/micro-2.0.14-linux-arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/zyedidia/micro.git",
                "ref": "v2.0.14"
            },
            "build": {
                "steps": [
                    "go build -v -o micro ./cmd/micro"
                ]
            }
        }
    },
    {
        "name": "presenterm",
        "version": "0.9.0",
        "description": "A terminal-based presentation tool",
        "homepage": "https://github.com/mfontanini/presenterm",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/mfontanini/presenterm/releases/download/v0.9.0/presenterm-v0.9.0-x86_64-unknown-linux-musl.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/mfontanini/presenterm.git",
                "ref": "v0.9.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "presenterm"
            ]
        }
    },
    {
        "name": "hyfetch",
        "version": "1.99.0",
        "description": "neofetch with pride flags",
        "homepage": "https://github.com/hykilpikonna/hyfetch",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/hykilpikonna/hyfetch/releases/download/1.99.0/hyfetch-1.99.0-linux-x86_64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/hykilpikonna/hyfetch.git",
                "ref": "1.99.0"
            },
            "build": {
                "steps": [
                    "python3 -m venv .venv",
                    ".venv/bin/pip install ."
                ]
            }
        }
    },
    {
        "name": "glab",
        "version": "1.49.0",
        "description": "An open-source GitLab command-line tool",
        "homepage": "https://gitlab.com/gitlab-org/cli",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://gitlab.com/gitlab-org/cli/-/releases/v1.49.0/downloads/glab_1.49.0_Linux_x86_64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://gitlab.com/gitlab-org/cli/-/releases/v1.49.0/downloads/glab_1.49.0_Linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://gitlab.com/gitlab-org/cli.git",
                "ref": "v1.49.0"
            },
            "build": {
                "steps": [
                    "go build -v -o glab ./cmd/glab"
                ]
            }
        }
    },
    {
        "name": "curlie",
        "version": "1.7.2",
        "description": "The power of curl, the ease of use of httpie",
        "homepage": "https://curlie.io",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/rs/curlie/releases/download/v1.7.2/curlie_1.7.2_linux_amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/rs/curlie/releases/download/v1.7.2/curlie_1.7.2_linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/rs/curlie.git",
                "ref": "v1.7.2"
            },
            "build": {
                "steps": [
                    "go build -v -o curlie"
                ]
            }
        }
    },
    {
        "name": "miniserve",
        "version": "0.27.1",
        "description": "For when you simply want to serve some files over HTTP",
        "homepage": "https://github.com/svenstaro/miniserve",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/svenstaro/miniserve/releases/download/v0.27.1/miniserve-0.27.1-x86_64-unknown-linux-gnu"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/svenstaro/miniserve.git",
                "ref": "v0.27.1"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "miniserve"
            ]
        }
    },
    {
        "name": "oxipng",
        "version": "9.1.2",
        "description": "Multithreaded PNG optimizer written in Rust",
        "homepage": "https://github.com/shssoichiro/oxipng",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/shssoichiro/oxipng/releases/download/v9.1.2/oxipng-9.1.2-x86_64-unknown-linux-musl.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/shssoichiro/oxipng.git",
                "ref": "v9.1.2"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "oxipng"
            ]
        }
    },
    {
        "name": "ugrep",
        "version": "7.0.0",
        "description": "Ultra fast grep CLI with interactive query UI",
        "homepage": "https://github.com/Genivia/ugrep",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/Genivia/ugrep/releases/download/v7.0.0/ugrep-7.0.0-x86_64-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/Genivia/ugrep.git",
                "ref": "v7.0.0"
            },
            "build": {
                "steps": [
                    "./build.sh"
                ]
            }
        }
    },
    {
        "name": "pnpm",
        "version": "9.14.4",
        "description": "Fast, disk space efficient package manager",
        "homepage": "https://pnpm.io",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/pnpm/pnpm/releases/download/v9.14.4/pnpm-linux-x64"
                },
                "linux-aarch64": {
                    "url": "https://github.com/pnpm/pnpm/releases/download/v9.14.4/pnpm-linux-arm64"
                }
            }
        }
    },
    {
        "name": "sysz",
        "version": "1.0.0",
        "description": "An interactive systemctl terminal UI",
        "homepage": "https://github.com/joehillen/sysz",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/joehillen/sysz.git",
                "ref": "v1.0.0"
            },
            "build": {
                "steps": [
                    "cp sysz /usr/local/bin/sysz"
                ]
            }
        }
    },
    {
        "name": "terraform",
        "version": "1.9.8",
        "description": "Terraform enables you to safely and predictably create, change, and improve infrastructure",
        "homepage": "https://www.terraform.io",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://releases.hashicorp.com/terraform/1.9.8/terraform_1.9.8_linux_amd64.zip"
                },
                "linux-aarch64": {
                    "url": "https://releases.hashicorp.com/terraform/1.9.8/terraform_1.9.8_linux_arm64.zip"
                }
            }
        }
    },
    {
        "name": "packer",
        "version": "1.11.2",
        "description": "Packer is a tool for creating identical machine images for multiple platforms",
        "homepage": "https://www.packer.io",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://releases.hashicorp.com/packer/1.11.2/packer_1.11.2_linux_amd64.zip"
                },
                "linux-aarch64": {
                    "url": "https://releases.hashicorp.com/packer/1.11.2/packer_1.11.2_linux_arm64.zip"
                }
            }
        }
    },
    {
        "name": "vault",
        "version": "1.18.1",
        "description": "A tool for managing secrets, keys, and sensitive data",
        "homepage": "https://www.vaultproject.io",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://releases.hashicorp.com/vault/1.18.1/vault_1.18.1_linux_amd64.zip"
                },
                "linux-aarch64": {
                    "url": "https://releases.hashicorp.com/vault/1.18.1/vault_1.18.1_linux_arm64.zip"
                }
            }
        }
    },
    {
        "name": "kubectl",
        "version": "1.31.2",
        "description": "Production-Grade Container Scheduling and Management CLI",
        "homepage": "https://kubernetes.io/docs/reference/kubectl/",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://dl.k8s.io/release/v1.31.2/bin/linux/amd64/kubectl"
                },
                "linux-aarch64": {
                    "url": "https://dl.k8s.io/release/v1.31.2/bin/linux/arm64/kubectl"
                }
            }
        }
    },
    {
        "name": "k3d",
        "version": "5.7.4",
        "description": "Little helper to run Rancher Lab's k3s in docker",
        "homepage": "https://k3d.io",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/k3d-io/k3d/releases/download/v5.7.4/k3d-linux-amd64"
                },
                "linux-aarch64": {
                    "url": "https://github.com/k3d-io/k3d/releases/download/v5.7.4/k3d-linux-arm64"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/k3d-io/k3d.git",
                "ref": "v5.7.4"
            },
            "build": {
                "steps": [
                    "go build -v -o k3d"
                ]
            }
        }
    },
    {
        "name": "kind",
        "version": "0.25.0",
        "description": "Kubernetes IN Docker - local clusters for testing Kubernetes",
        "homepage": "https://kind.sigs.k8s.io",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/kubernetes-sigs/kind/releases/download/v0.25.0/kind-linux-amd64"
                },
                "linux-aarch64": {
                    "url": "https://github.com/kubernetes-sigs/kind/releases/download/v0.25.0/kind-linux-arm64"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/kubernetes-sigs/kind.git",
                "ref": "v0.25.0"
            },
            "build": {
                "steps": [
                    "go build -v -o kind"
                ]
            }
        }
    },
    {
        "name": "minikube",
        "version": "1.34.0",
        "description": "Run Kubernetes locally",
        "homepage": "https://minikube.sigs.k8s.io",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/kubernetes/minikube/releases/download/v1.34.0/minikube-linux-amd64"
                },
                "linux-aarch64": {
                    "url": "https://github.com/kubernetes/minikube/releases/download/v1.34.0/minikube-linux-arm64"
                }
            }
        }
    },
    {
        "name": "argocd",
        "version": "2.13.0",
        "description": "Declarative GitOps CD tool for Kubernetes",
        "homepage": "https://argo-cd.readthedocs.io",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/argoproj/argo-cd/releases/download/v2.13.0/argocd-linux-amd64"
                },
                "linux-aarch64": {
                    "url": "https://github.com/argoproj/argo-cd/releases/download/v2.13.0/argocd-linux-arm64"
                }
            }
        }
    },
    {
        "name": "cosign",
        "version": "2.4.1",
        "description": "Container Signing, Verification and Storage in an OCI registry",
        "homepage": "https://github.com/sigstore/cosign",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/sigstore/cosign/releases/download/v2.4.1/cosign-linux-amd64"
                },
                "linux-aarch64": {
                    "url": "https://github.com/sigstore/cosign/releases/download/v2.4.1/cosign-linux-arm64"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/sigstore/cosign.git",
                "ref": "v2.4.1"
            },
            "build": {
                "steps": [
                    "go build -v -o cosign ./cmd/cosign"
                ]
            }
        }
    },
    {
        "name": "syft",
        "version": "1.16.0",
        "description": "CLI tool for generating a Software Bill of Materials (SBOM)",
        "homepage": "https://github.com/anchore/syft",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/anchore/syft/releases/download/v1.16.0/syft_1.16.0_linux_amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/anchore/syft/releases/download/v1.16.0/syft_1.16.0_linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/anchore/syft.git",
                "ref": "v1.16.0"
            },
            "build": {
                "steps": [
                    "go build -v -o syft ./cmd/syft"
                ]
            }
        }
    },
    {
        "name": "grype",
        "version": "0.84.0",
        "description": "A vulnerability scanner for container images and filesystems",
        "homepage": "https://github.com/anchore/grype",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/anchore/grype/releases/download/v0.84.0/grype_0.84.0_linux_amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/anchore/grype/releases/download/v0.84.0/grype_0.84.0_linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/anchore/grype.git",
                "ref": "v0.84.0"
            },
            "build": {
                "steps": [
                    "go build -v -o grype ./cmd/grype"
                ]
            }
        }
    },
    {
        "name": "trivy",
        "version": "0.57.1",
        "description": "Comprehensive security scanner for vulnerabilities and misconfigurations",
        "homepage": "https://trivy.dev",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/aquasecurity/trivy/releases/download/v0.57.1/trivy_0.57.1_Linux-64bit.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/aquasecurity/trivy/releases/download/v0.57.1/trivy_0.57.1_Linux-ARM64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/aquasecurity/trivy.git",
                "ref": "v0.57.1"
            },
            "build": {
                "steps": [
                    "go build -v -o trivy ./cmd/trivy"
                ]
            }
        }
    },
    {
        "name": "zola",
        "version": "0.19.2",
        "description": "A fast static site generator in a single binary",
        "homepage": "https://www.getzola.org",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/getzola/zola/releases/download/v0.19.2/zola-v0.19.2-x86_64-unknown-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/getzola/zola.git",
                "ref": "v0.19.2"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "zola"
            ]
        }
    },
    {
        "name": "mdbook",
        "version": "0.4.40",
        "description": "Create book from markdown files",
        "homepage": "https://rust-lang.github.io/mdBook/",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/rust-lang/mdBook/releases/download/v0.4.40/mdbook-v0.4.40-x86_64-unknown-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/rust-lang/mdBook.git",
                "ref": "v0.4.40"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "mdbook"
            ]
        }
    },
    {
        "name": "wasm-pack",
        "version": "0.13.1",
        "description": "Your favorite rust -> wasm workflow tool",
        "homepage": "https://rustwasm.github.io/wasm-pack/",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/rustwasm/wasm-pack/releases/download/v0.13.1/wasm-pack-v0.13.1-x86_64-unknown-linux-musl.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/rustwasm/wasm-pack.git",
                "ref": "v0.13.1"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "wasm-pack"
            ]
        }
    },
    {
        "name": "trunk",
        "version": "0.21.4",
        "description": "Build, bundle & ship your Rust WASM application to the web",
        "homepage": "https://trunkrs.dev",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/trunk-rs/trunk/releases/download/v0.21.4/trunk-x86_64-unknown-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/trunk-rs/trunk.git",
                "ref": "v0.21.4"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "trunk"
            ]
        }
    },
    {
        "name": "cargo-deny",
        "version": "0.16.1",
        "description": "Cargo plugin for linting your dependencies",
        "homepage": "https://github.com/EmbarkStudios/cargo-deny",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/EmbarkStudios/cargo-deny/releases/download/0.16.1/cargo-deny-0.16.1-x86_64-unknown-linux-musl.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/EmbarkStudios/cargo-deny.git",
                "ref": "0.16.1"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "cargo-deny"
            ]
        }
    },
    {
        "name": "cargo-audit",
        "version": "0.21.0",
        "description": "Audit Cargo.lock files for crates with security vulnerabilities",
        "homepage": "https://github.com/rustsec/rustsec",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/rustsec/rustsec/releases/download/cargo-audit%2Fv0.21.0/cargo-audit-x86_64-unknown-linux-musl-v0.21.0.tgz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/rustsec/rustsec.git",
                "ref": "cargo-audit/v0.21.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "cargo-audit"
            ]
        }
    },
    {
        "name": "bob",
        "version": "3.0.1",
        "description": "A simple Neovim version manager",
        "homepage": "https://github.com/MordechaiHadad/bob",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/MordechaiHadad/bob/releases/download/v3.0.1/bob-linux-x86_64.zip"
                },
                "linux-aarch64": {
                    "url": "https://github.com/MordechaiHadad/bob/releases/download/v3.0.1/bob-linux-arm64.zip"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/MordechaiHadad/bob.git",
                "ref": "v3.0.1"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "bob"
            ]
        }
    },
    {
        "name": "fnm",
        "version": "1.38.1",
        "description": "Fast and simple Node.js version manager, built in Rust",
        "homepage": "https://github.com/Schniz/fnm",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/Schniz/fnm/releases/download/v1.38.1/fnm-linux.zip"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/Schniz/fnm.git",
                "ref": "v1.38.1"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "fnm"
            ]
        }
    },
    {
        "name": "bun",
        "version": "1.1.38",
        "description": "Incredibly fast JavaScript frontend toolchain and runtime",
        "homepage": "https://bun.sh",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/oven-sh/bun/releases/download/bun-v1.1.38/bun-linux-x64.zip"
                },
                "linux-aarch64": {
                    "url": "https://github.com/oven-sh/bun/releases/download/bun-v1.1.38/bun-linux-aarch64.zip"
                }
            }
        }
    },
    {
        "name": "deno",
        "version": "2.1.2",
        "description": "A modern runtime for JavaScript and TypeScript",
        "homepage": "https://deno.com",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/denoland/deno/releases/download/v2.1.2/deno-x86_64-unknown-linux-gnu.zip"
                },
                "linux-aarch64": {
                    "url": "https://github.com/denoland/deno/releases/download/v2.1.2/deno-aarch64-unknown-linux-gnu.zip"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/denoland/deno.git",
                "ref": "v2.1.2"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "deno"
            ]
        }
    },
    {
        "name": "oxlint",
        "version": "0.11.0",
        "description": "Designed to catch erroneous or useless code without requiring any configuration",
        "homepage": "https://oxc.rs",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/oxc-project/oxc/releases/download/oxlint_v0.11.0/oxlint-linux-x64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/oxc-project/oxc/releases/download/oxlint_v0.11.0/oxlint-linux-arm64.tar.gz"
                }
            }
        }
    },
    {
        "name": "mise",
        "version": "2024.11.23",
        "description": "dev tools, env vars, task runner",
        "homepage": "https://mise.jdx.dev",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/jdx/mise/releases/download/v2024.11.23/mise-v2024.11.23-linux-x64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/jdx/mise/releases/download/v2024.11.23/mise-v2024.11.23-linux-arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/jdx/mise.git",
                "ref": "v2024.11.23"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "mise"
            ]
        }
    },
    {
        "name": "direnv",
        "version": "2.35.0",
        "description": "Unclutter your .profile - environment switcher for the shell",
        "homepage": "https://direnv.net",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/direnv/direnv/releases/download/v2.35.0/direnv.linux-amd64"
                },
                "linux-aarch64": {
                    "url": "https://github.com/direnv/direnv/releases/download/v2.35.0/direnv.linux-arm64"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/direnv/direnv.git",
                "ref": "v2.35.0"
            },
            "build": {
                "steps": [
                    "go build -v -o direnv"
                ]
            }
        }
    },
    {
        "name": "television",
        "version": "0.8.2",
        "description": "A fast, customizable, and versatile fuzzy finder TUI",
        "homepage": "https://github.com/alexpasmantier/television",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/alexpasmantier/television/releases/download/0.8.2/tv-0.8.2-x86_64-unknown-linux-musl.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/alexpasmantier/television.git",
                "ref": "0.8.2"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "tv"
            ]
        }
    },
    {
        "name": "jless",
        "version": "0.9.0",
        "description": "An interactive command-line JSON viewer",
        "homepage": "https://jless.io",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/PaulJuliusMartinez/jless/releases/download/v0.9.0/jless-v0.9.0-x86_64-unknown-linux-gnu.zip"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/PaulJuliusMartinez/jless.git",
                "ref": "v0.9.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "jless"
            ]
        }
    },
    {
        "name": "fq",
        "version": "0.13.0",
        "description": "jq for binary formats",
        "homepage": "https://github.com/wader/fq",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/wader/fq/releases/download/v0.13.0/fq_0.13.0_linux_amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/wader/fq/releases/download/v0.13.0/fq_0.13.0_linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/wader/fq.git",
                "ref": "v0.13.0"
            },
            "build": {
                "steps": [
                    "go build -v -o fq"
                ]
            }
        }
    },
    {
        "name": "restic",
        "version": "0.17.3",
        "description": "Fast, secure, efficient backup program",
        "homepage": "https://restic.net",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/restic/restic/releases/download/v0.17.3/restic_0.17.3_linux_amd64.bz2"
                },
                "linux-aarch64": {
                    "url": "https://github.com/restic/restic/releases/download/v0.17.3/restic_0.17.3_linux_arm64.bz2"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/restic/restic.git",
                "ref": "v0.17.3"
            },
            "build": {
                "steps": [
                    "go run build.go"
                ]
            }
        }
    },
    {
        "name": "rclone",
        "version": "1.68.2",
        "description": "rsync for cloud storage",
        "homepage": "https://rclone.org",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/rclone/rclone/releases/download/v1.68.2/rclone-v1.68.2-linux-amd64.zip"
                },
                "linux-aarch64": {
                    "url": "https://github.com/rclone/rclone/releases/download/v1.68.2/rclone-v1.68.2-linux-arm64.zip"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/rclone/rclone.git",
                "ref": "v1.68.2"
            },
            "build": {
                "steps": [
                    "go build -v -o rclone"
                ]
            }
        }
    },
    {
        "name": "yt-dlp",
        "version": "2024.11.18",
        "description": "A feature-rich command-line audio/video downloader",
        "homepage": "https://github.com/yt-dlp/yt-dlp",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/yt-dlp/yt-dlp/releases/download/2024.11.18/yt-dlp"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/yt-dlp/yt-dlp.git",
                "ref": "2024.11.18"
            },
            "build": {
                "steps": [
                    "make"
                ]
            }
        }
    },
    {
        "name": "lf",
        "version": "r33",
        "description": "Terminal file manager written in Go",
        "homepage": "https://github.com/gokcehan/lf",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/gokcehan/lf/releases/download/r33/lf-linux-amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/gokcehan/lf/releases/download/r33/lf-linux-arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/gokcehan/lf.git",
                "ref": "r33"
            },
            "build": {
                "steps": [
                    "go build -v -o lf"
                ]
            }
        }
    },
    {
        "name": "nnn",
        "version": "5.0",
        "description": "Tiny, lightning fast, feature-packed terminal file manager",
        "homepage": "https://github.com/jarun/nnn",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/jarun/nnn/releases/download/v5.0/nnn-static-5.0.x86_64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/jarun/nnn.git",
                "ref": "v5.0"
            },
            "build": {
                "system": "make"
            }
        }
    },
    {
        "name": "gdu",
        "version": "5.29.0",
        "description": "Fast disk usage analyzer written in Go",
        "homepage": "https://github.com/dundee/gdu",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/dundee/gdu/releases/download/v5.29.0/gdu_linux_amd64.tgz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/dundee/gdu/releases/download/v5.29.0/gdu_linux_arm64.tgz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/dundee/gdu.git",
                "ref": "v5.29.0"
            },
            "build": {
                "steps": [
                    "go build -v -o gdu ./cmd/gdu"
                ]
            }
        }
    },
    {
        "name": "ncdu",
        "version": "2.6",
        "description": "NCurses Disk Usage",
        "homepage": "https://dev.yorhel.nl/ncdu",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://dev.yorhel.nl/download/ncdu-2.6-linux-x86_64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://dev.yorhel.nl/download/ncdu-2.6-linux-aarch64.tar.gz"
                }
            }
        }
    },
    {
        "name": "kakoune",
        "version": "2024.05.18",
        "description": "Maw-driven text editor, modal edit on steroids",
        "homepage": "https://kakoune.org",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/mawww/kakoune.git",
                "ref": "v2024.05.18"
            },
            "build": {
                "system": "make"
            }
        }
    },
    {
        "name": "aria2",
        "version": "1.37.0",
        "description": "Ultra fast download utility with multi-protocol & multi-source support",
        "homepage": "https://aria2.github.io",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/aria2/aria2.git",
                "ref": "release-1.37.0"
            },
            "build": {
                "steps": [
                    "autoreconf -i",
                    "./configure",
                    "make"
                ]
            }
        }
    },
    {
        "name": "httpie",
        "version": "3.2.4",
        "description": "User-friendly CLI HTTP client for the API era",
        "homepage": "https://httpie.io",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/httpie/cli.git",
                "ref": "3.2.4"
            },
            "build": {
                "steps": [
                    "python3 -m venv .venv",
                    ".venv/bin/pip install ."
                ]
            }
        }
    },
    {
        "name": "opentofu",
        "version": "1.8.6",
        "description": "OpenTofu lets you declaratively manage your cloud infrastructure",
        "homepage": "https://opentofu.org",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/opentofu/opentofu/releases/download/v1.8.6/tofu_1.8.6_linux_amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/opentofu/opentofu/releases/download/v1.8.6/tofu_1.8.6_linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/opentofu/opentofu.git",
                "ref": "v1.8.6"
            },
            "build": {
                "steps": [
                    "go build -v -o tofu ./cmd/tofu"
                ]
            }
        }
    },
    {
        "name": "terragrunt",
        "version": "0.69.1",
        "description": "Thin wrapper for Terraform / OpenTofu that provides extra tools",
        "homepage": "https://terragrunt.gruntwork.io",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/gruntwork-io/terragrunt/releases/download/v0.69.1/terragrunt_linux_amd64"
                },
                "linux-aarch64": {
                    "url": "https://github.com/gruntwork-io/terragrunt/releases/download/v0.69.1/terragrunt_linux_arm64"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/gruntwork-io/terragrunt.git",
                "ref": "v0.69.1"
            },
            "build": {
                "steps": [
                    "go build -v -o terragrunt"
                ]
            }
        }
    },
    {
        "name": "flux",
        "version": "2.4.0",
        "description": "Open and extensible continuous delivery solution for Kubernetes",
        "homepage": "https://fluxcd.io",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/fluxcd/flux2/releases/download/v2.4.0/flux_2.4.0_linux_amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/fluxcd/flux2/releases/download/v2.4.0/flux_2.4.0_linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/fluxcd/flux2.git",
                "ref": "v2.4.0"
            },
            "build": {
                "steps": [
                    "go build -v -o flux ./cmd/flux"
                ]
            }
        }
    },
    {
        "name": "kubectx",
        "version": "0.9.5",
        "description": "Faster way to switch between clusters and namespaces in kubectl",
        "homepage": "https://github.com/ahmetb/kubectx",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/ahmetb/kubectx/releases/download/v0.9.5/kubectx_v0.9.5_linux_x86_64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/ahmetb/kubectx/releases/download/v0.9.5/kubectx_v0.9.5_linux_arm64.tar.gz"
                }
            }
        }
    },
    {
        "name": "stern",
        "version": "1.30.0",
        "description": "Multi pod and container log tailing for Kubernetes",
        "homepage": "https://github.com/stern/stern",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/stern/stern/releases/download/v1.30.0/stern_1.30.0_linux_amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/stern/stern/releases/download/v1.30.0/stern_1.30.0_linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/stern/stern.git",
                "ref": "v1.30.0"
            },
            "build": {
                "steps": [
                    "go build -v -o stern"
                ]
            }
        }
    },
    {
        "name": "skaffold",
        "version": "2.13.2",
        "description": "Easy and Repeatable Kubernetes Development",
        "homepage": "https://skaffold.dev",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/GoogleContainerTools/skaffold/releases/download/v2.13.2/skaffold-linux-amd64"
                },
                "linux-aarch64": {
                    "url": "https://github.com/GoogleContainerTools/skaffold/releases/download/v2.13.2/skaffold-linux-arm64"
                }
            }
        }
    },
    {
        "name": "podman",
        "version": "5.3.1",
        "description": "A daemonless container engine for developing, managing, and running OCI Containers",
        "homepage": "https://podman.io",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/containers/podman.git",
                "ref": "v5.3.1"
            },
            "build": {
                "steps": [
                    "make podman"
                ]
            }
        }
    },
    {
        "name": "buildah",
        "version": "1.38.0",
        "description": "A tool that facilitates building OCI container images",
        "homepage": "https://buildah.io",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/containers/buildah.git",
                "ref": "v1.38.0"
            },
            "build": {
                "steps": [
                    "make buildah"
                ]
            }
        }
    },
    {
        "name": "skopeo",
        "version": "1.17.0",
        "description": "Work with remote images registries - retrieving information, images, signing content",
        "homepage": "https://github.com/containers/skopeo",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/containers/skopeo.git",
                "ref": "v1.17.0"
            },
            "build": {
                "steps": [
                    "make bin/skopeo"
                ]
            }
        }
    },
    {
        "name": "pandoc",
        "version": "3.5",
        "description": "Universal markup converter",
        "homepage": "https://pandoc.org",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/jgm/pandoc/releases/download/3.5/pandoc-3.5-linux-amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/jgm/pandoc/releases/download/3.5/pandoc-3.5-linux-arm64.tar.gz"
                }
            }
        }
    },
    {
        "name": "exiftool",
        "version": "13.00",
        "description": "Read, Write and Edit Meta Information in a Wide Variety of Files",
        "homepage": "https://exiftool.org",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/exiftool/exiftool.git",
                "ref": "13.00"
            },
            "build": {
                "steps": [
                    "perl Makefile.PL",
                    "make"
                ]
            }
        }
    },
    {
        "name": "go-task",
        "version": "3.40.0",
        "description": "A task runner / simpler Makefile alternative written in Go",
        "homepage": "https://taskfile.dev",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/go-task/task/releases/download/v3.40.0/task_linux_amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/go-task/task/releases/download/v3.40.0/task_linux_arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/go-task/task.git",
                "ref": "v3.40.0"
            },
            "build": {
                "steps": [
                    "go build -v -o task ./cmd/task"
                ]
            }
        }
    },
    {
        "name": "cargo-nextest",
        "version": "0.9.85",
        "description": "Next-generation test runner for Rust projects",
        "homepage": "https://nexte.st",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/nextest-rs/nextest/releases/download/cargo-nextest-0.9.85/cargo-nextest-0.9.85-x86_64-unknown-linux-gnu.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/nextest-rs/nextest.git",
                "ref": "cargo-nextest-0.9.85"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "cargo-nextest"
            ]
        }
    },
    {
        "name": "cargo-watch",
        "version": "8.5.2",
        "description": "Watches over your Cargo project's source",
        "homepage": "https://github.com/watchexec/cargo-watch",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/watchexec/cargo-watch/releases/download/v8.5.2/cargo-watch-v8.5.2-x86_64-unknown-linux-gnu.tar.xz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/watchexec/cargo-watch.git",
                "ref": "v8.5.2"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "cargo-watch"
            ]
        }
    },
    {
        "name": "cargo-expand",
        "version": "1.0.95",
        "description": "Subcommand to show result of macro expansion",
        "homepage": "https://github.com/dtolnay/cargo-expand",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/dtolnay/cargo-expand.git",
                "ref": "1.0.95"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "cargo-expand"
            ]
        }
    },
    {
        "name": "cargo-edit",
        "version": "0.13.0",
        "description": "A cargo subcommand for managing dependencies",
        "homepage": "https://github.com/killercup/cargo-edit",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/killercup/cargo-edit.git",
                "ref": "v0.13.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "cargo-add",
                "cargo-rm",
                "cargo-upgrade"
            ]
        }
    },
    {
        "name": "atlas",
        "version": "0.29.0",
        "description": "A modern tool for managing database schemas",
        "homepage": "https://atlasgo.io",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://release.ariga.io/atlas/atlas-linux-amd64-v0.29.0"
                },
                "linux-aarch64": {
                    "url": "https://release.ariga.io/atlas/atlas-linux-arm64-v0.29.0"
                }
            }
        }
    },
    {
        "name": "dbmate",
        "version": "2.22.0",
        "description": "A lightweight, framework-agnostic database migration tool",
        "homepage": "https://github.com/amacneil/dbmate",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/amacneil/dbmate/releases/download/v2.22.0/dbmate-linux-amd64"
                },
                "linux-aarch64": {
                    "url": "https://github.com/amacneil/dbmate/releases/download/v2.22.0/dbmate-linux-arm64"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/amacneil/dbmate.git",
                "ref": "v2.22.0"
            },
            "build": {
                "steps": [
                    "go build -v -o dbmate"
                ]
            }
        }
    },
    {
        "name": "usql",
        "version": "0.19.3",
        "description": "Universal command-line interface for SQL databases",
        "homepage": "https://github.com/xo/usql",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/xo/usql/releases/download/v0.19.3/usql-0.19.3-linux-amd64.tar.bz2"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/xo/usql.git",
                "ref": "v0.19.3"
            },
            "build": {
                "steps": [
                    "go build -v -o usql"
                ]
            }
        }
    },
    {
        "name": "mycli",
        "version": "1.27.2",
        "description": "A Terminal Client for MySQL with AutoCompletion and Syntax Highlighting",
        "homepage": "https://www.mycli.net",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/dbcli/mycli.git",
                "ref": "v1.27.2"
            },
            "build": {
                "steps": [
                    "python3 -m venv .venv",
                    ".venv/bin/pip install ."
                ]
            }
        }
    },
    {
        "name": "pgcli",
        "version": "4.1.0",
        "description": "Postgres CLI with autocompletion and syntax highlighting",
        "homepage": "https://www.pgcli.com",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/dbcli/pgcli.git",
                "ref": "v4.1.0"
            },
            "build": {
                "steps": [
                    "python3 -m venv .venv",
                    ".venv/bin/pip install ."
                ]
            }
        }
    },
    {
        "name": "sops",
        "version": "3.9.1",
        "description": "Simple and Flexible Tool for Managing Secrets",
        "homepage": "https://github.com/getsops/sops",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/getsops/sops/releases/download/v3.9.1/sops-v3.9.1.linux.amd64"
                },
                "linux-aarch64": {
                    "url": "https://github.com/getsops/sops/releases/download/v3.9.1/sops-v3.9.1.linux.arm64"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/getsops/sops.git",
                "ref": "v3.9.1"
            },
            "build": {
                "steps": [
                    "go build -v -o sops ./cmd/sops"
                ]
            }
        }
    },
    {
        "name": "gopass",
        "version": "1.15.15",
        "description": "The slightly more awesome standard unix password manager for teams",
        "homepage": "https://www.gopass.pw",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/gopasspw/gopass/releases/download/v1.15.15/gopass-1.15.15-linux-amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/gopasspw/gopass/releases/download/v1.15.15/gopass-1.15.15-linux-arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/gopasspw/gopass.git",
                "ref": "v1.15.15"
            },
            "build": {
                "steps": [
                    "go build -v -o gopass"
                ]
            }
        }
    },
    {
        "name": "pass",
        "version": "1.7.4",
        "description": "The standard unix password manager",
        "homepage": "https://www.passwordstore.org",
        "src": {
            "source": {
                "type": "git",
                "url": "https://git.zx2c4.com/password-store",
                "ref": "1.7.4"
            },
            "build": {
                "system": "make"
            }
        }
    },
    {
        "name": "bitwarden-cli",
        "version": "2024.11.0",
        "description": "The Bitwarden command-line interface (CLI)",
        "homepage": "https://bitwarden.com",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/bitwarden/clients/releases/download/cli-v2024.11.0/bw-linux-2024.11.0.zip"
                }
            }
        }
    },
    {
        "name": "doppler",
        "version": "3.69.0",
        "description": "Official CLI for Doppler, the developer secret store",
        "homepage": "https://doppler.com",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/DopplerHQ/cli/releases/download/v3.69.0/doppler_3.69.0_linux_amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/DopplerHQ/cli/releases/download/v3.69.0/doppler_3.69.0_linux_arm64.tar.gz"
                }
            }
        }
    },
    {
        "name": "pulumi",
        "version": "3.141.0",
        "description": "Pulumi - Infrastructure as Code in any programming language",
        "homepage": "https://www.pulumi.com",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://get.pulumi.com/releases/sdk/pulumi-v3.141.0-linux-x64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://get.pulumi.com/releases/sdk/pulumi-v3.141.0-linux-arm64.tar.gz"
                }
            }
        }
    },
    {
        "name": "crossplane",
        "version": "1.18.2",
        "description": "The Cloud Native Control Plane Framework",
        "homepage": "https://crossplane.io",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://releases.crossplane.io/stable/v1.18.2/bin/linux_amd64/crank"
                },
                "linux-aarch64": {
                    "url": "https://releases.crossplane.io/stable/v1.18.2/bin/linux_arm64/crank"
                }
            }
        }
    },
    {
        "name": "fish",
        "version": "3.7.1",
        "description": "The user-friendly command line shell",
        "homepage": "https://fishshell.com",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/fish-shell/fish-shell.git",
                "ref": "3.7.1"
            },
            "build": {
                "system": "cmake"
            }
        }
    },
    {
        "name": "zsh",
        "version": "5.9",
        "description": "Zsh is a shell designed for interactive use and scripting",
        "homepage": "https://www.zsh.org",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/zsh-users/zsh.git",
                "ref": "zsh-5.9"
            },
            "build": {
                "steps": [
                    "Util/preconfig",
                    "./configure",
                    "make"
                ]
            }
        }
    },
    {
        "name": "mosh",
        "version": "1.4.0",
        "description": "Mobile Shell: remote terminal application that allows roaming",
        "homepage": "https://mosh.org",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/mobile-shell/mosh.git",
                "ref": "mosh-1.4.0"
            },
            "build": {
                "steps": [
                    "./autogen.sh",
                    "./configure",
                    "make"
                ]
            }
        }
    },
    {
        "name": "asciinema",
        "version": "2.4.0",
        "description": "Terminal session recorder",
        "homepage": "https://asciinema.org",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/asciinema/asciinema.git",
                "ref": "v2.4.0"
            },
            "build": {
                "steps": [
                    "python3 -m venv .venv",
                    ".venv/bin/pip install ."
                ]
            }
        }
    },
    {
        "name": "dua-cli",
        "version": "2.29.0",
        "description": "View disk space usage and delete unneeded data fast",
        "homepage": "https://github.com/Byron/dua-cli",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/Byron/dua-cli/releases/download/v2.29.0/dua-v2.29.0-x86_64-unknown-linux-musl.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/Byron/dua-cli.git",
                "ref": "v2.29.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "dua"
            ]
        }
    },
    {
        "name": "macchina",
        "version": "6.1.0",
        "description": "A fast, minimal and customizable system information fetcher",
        "homepage": "https://github.com/Macchina-CLI/macchina",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/Macchina-CLI/macchina/releases/download/v6.1.0/macchina-linux-x86_64"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/Macchina-CLI/macchina.git",
                "ref": "v6.1.0"
            },
            "build": {
                "system": "cargo",
                "release": True,
                "locked": True
            },
            "executables": [
                "macchina"
            ]
        }
    },
    {
        "name": "pfetch",
        "version": "0.7.0",
        "description": "A pretty empty system information script written in POSIX sh",
        "homepage": "https://github.com/dylanaraps/pfetch",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/dylanaraps/pfetch.git",
                "ref": "0.7.0"
            },
            "build": {
                "steps": [
                    "echo 'pfetch script ready'"
                ]
            }
        }
    },
    {
        "name": "inxi",
        "version": "3.3.36-1",
        "description": "Full featured CLI system information tool",
        "homepage": "https://smxi.org/docs/inxi.htm",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/smxi/inxi.git",
                "ref": "3.3.36-1"
            },
            "build": {
                "steps": [
                    "echo 'inxi perl script ready'"
                ]
            }
        }
    },
    {
        "name": "hcloud",
        "version": "1.48.0",
        "description": "A command-line interface for Hetzner Cloud",
        "homepage": "https://github.com/hetznercloud/cli",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/hetznercloud/cli/releases/download/v1.48.0/hcloud-linux-amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/hetznercloud/cli/releases/download/v1.48.0/hcloud-linux-arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/hetznercloud/cli.git",
                "ref": "v1.48.0"
            },
            "build": {
                "steps": [
                    "go build -v -o hcloud ./cmd/hcloud"
                ]
            }
        }
    },
    {
        "name": "doctl",
        "version": "1.120.0",
        "description": "Official command line interface for the DigitalOcean API",
        "homepage": "https://github.com/digitalocean/doctl",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/digitalocean/doctl/releases/download/v1.120.0/doctl-1.120.0-linux-amd64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/digitalocean/doctl/releases/download/v1.120.0/doctl-1.120.0-linux-arm64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/digitalocean/doctl.git",
                "ref": "v1.120.0"
            },
            "build": {
                "steps": [
                    "go build -v -o doctl ./cmd/doctl"
                ]
            }
        }
    },
    {
        "name": "glances",
        "version": "4.2.1",
        "description": "Glances an Eye on your system. A top/htop alternative for GNU/Linux",
        "homepage": "https://nicolargo.github.io/glances/",
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/nicolargo/glances.git",
                "ref": "v4.2.1"
            },
            "build": {
                "steps": [
                    "python3 -m venv .venv",
                    ".venv/bin/pip install ."
                ]
            }
        }
    },
    {
        "name": "subfinder",
        "version": "2.6.6",
        "description": "Subdomain discovery tool that discovers valid subdomains for websites",
        "homepage": "https://github.com/projectdiscovery/subfinder",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/projectdiscovery/subfinder/releases/download/v2.6.6/subfinder_2.6.6_linux_amd64.zip"
                },
                "linux-aarch64": {
                    "url": "https://github.com/projectdiscovery/subfinder/releases/download/v2.6.6/subfinder_2.6.6_linux_arm64.zip"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/projectdiscovery/subfinder.git",
                "ref": "v2.6.6"
            },
            "build": {
                "steps": [
                    "go build -v -o subfinder ./cmd/subfinder"
                ]
            }
        }
    },
    {
        "name": "zsign",
        "version": "1.1.2",
        "description": "Fast Cross-Platform iOS Code Signing Tool",
        "homepage": "https://github.com/zhlynn/zsign",
        "bin": {
            "downloads": {
                "linux-x86_64": {
                    "url": "https://github.com/zhlynn/zsign/releases/download/v1.1.2/zsign-linux-x86_64.tar.gz"
                },
                "linux-aarch64": {
                    "url": "https://github.com/zhlynn/zsign/releases/download/v1.1.2/zsign-linux-aarch64.tar.gz"
                }
            }
        },
        "src": {
            "source": {
                "type": "git",
                "url": "https://github.com/zhlynn/zsign.git",
                "ref": "v1.1.2"
            },
            "build": {
                "steps": [
                    "cd build/linux",
                    "make"
                ]
            }
        }
    }
]

def main():
    packages_dir = "packages"
    os.makedirs(packages_dir, exist_ok=True)

    index_packages = {}

    for app in APPS:
        name = app["name"]
        version = app["version"]
        desc = app["description"]
        homepage = app.get("homepage", "")

        # Binary package if present
        if "bin" in app:
            pkg_id = f"{name}-bin"
            def_path = f"packages/{pkg_id}.json"

            supported_platforms = list(app["bin"]["downloads"].keys())

            bin_pkg = {
                "schema_version": 1,
                "id": pkg_id,
                "name": name,
                "version": version,
                "type": "binary",
                "description": desc,
                "homepage": homepage,
                "downloads": app["bin"]["downloads"],
                "supported_platforms": supported_platforms
            }

            with open(def_path, "w") as f:
                json.dump(bin_pkg, f, indent=4)
                f.write("\n")

            index_packages[pkg_id] = {
                "definition": def_path,
                "type": "binary",
                "description": desc
            }

        # Source package if present
        if "src" in app:
            pkg_id = f"{name}-src"
            def_path = f"packages/{pkg_id}.json"

            src_pkg = {
                "schema_version": 1,
                "id": pkg_id,
                "name": name,
                "version": version,
                "type": "source",
                "description": f"{desc} (source build)",
                "homepage": homepage,
                "source": app["src"]["source"],
                "build": app["src"]["build"]
            }
            if "executables" in app["src"]:
                src_pkg["executables"] = app["src"]["executables"]

            with open(def_path, "w") as f:
                json.dump(src_pkg, f, indent=4)
                f.write("\n")

            index_packages[pkg_id] = {
                "definition": def_path,
                "type": "source",
                "description": f"{desc} (source build)"
            }

    index_data = {
        "schema_version": 2,
        "description": "A giant Aster repo full of mostly untested packages, some work though.",
        "homepage": "https://github.com/MagicDippyEggsRandomStuff/giant-aster-repo",
        "packages": index_packages
    }

    with open("index.json", "w") as f:
        json.dump(index_data, f, indent=4)
        f.write("\n")

    print(f"Generated {len(index_packages)} packages in index.json and {packages_dir}/")

if __name__ == "__main__":
    main()
