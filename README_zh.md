# Dotfiles

个人 Linux 配置文件仓库，由 [chezmoi](https://www.chezmoi.io/) 管理，包含 Shell、编辑器、终端、桌面环境和应用程序配置。

[English](README.md)

## 配置内容

- **Shell：** Zsh 配置、别名、插件、命令补全、历史记录、按键绑定和提示符，以及用户配置文件与 X 会话启动配置。
- **编辑器：** Vim 配置、One Dark 配色方案，以及语法和缩进配置。
- **终端：** Kitty 配置、自定义标签栏和 X resources。
- **桌面环境（X11）：** bspwm、sxhkd、Polybar、Rofi、Dunst 和 Picom 配置，以及会话自动启动项。
- **应用程序：** Git、GTK、fontconfig、CopyQ、Fcitx 5、Go、容器镜像仓库、浏览器和 VS Code 启动参数，以及 smart-go-dl。
- **私有配置：** GPG、SSH 和部分应用程序配置以加密文件保存。

## 使用方法

使用该仓库初始化 chezmoi 并应用配置：

```sh
chezmoi init https://github.com/antonchen/dotfiles.git
chezmoi apply
```

应用更新前可先查看差异：

```sh
chezmoi diff
chezmoi apply
```

部分配置针对本机和桌面环境定制。应用或使用前，请先安装相应应用程序。

## 开源授权

本项目采用 [MIT License](LICENSE) 授权。
