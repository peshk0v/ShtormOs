import os

username = input("WRITE YOUR USERNAME")
print("TO START INSTALL CLICK ENTER")
input()

print("INSTALLING PACKAGES")
os.system("sudo pacman -S neofetch python-pip zsh flatpak firefox cups sane xsane code htop neovim mpv okular curl skanlite")
print("PACKAGES INSTALL SUCCICES!")
print("CONFIGURATE NEOFETCH")
os.system("sudo mv date/neo/neofetch /usr/bin/")
os.system(f"sudo mv date/neo/config.conf /home/{username}/.config/neofetch/")
print("NEOFETCH CONFIGURATED!")
print("INSTALLING YAY")
os.system("sudo pacman -S --needed base-devel")
os.system("cd")
os.system("git clone https://aur.archlinux.org/yay.git")
os.system("cd yay")
os.system("makepkg -si")
os.system("yay --version")
print("YAY SUCCSICEFULL INSTALLED!")
print("INSTALLING PYTHON PACKAGES")
os.system("pip install art tabulate --break-system-packages")
print("PACKAGES INSTALL SUCSSICES!")
print("MOVING BACKGROUND IMAGES")
os.system(f"mv shtorm /home/{username}/Изображения/shtorm")
print("BACKGROUND IMAGES MOVED!")
print("ZSH CONFIGURATE")
os.system("curl -L https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh | sh")
os.system(f"mv /date/zsh/.zshrc /home/{username}/")
os.system(f"mv /date/zsh/.p10k.zsh /home/{username}/")
print("ZSH CONFIGURATED")
print("INSTALLING FLATPAK PACKAGES")
os.system("flatpak install flathub org.libreoffice.LibreOffice")
os.system("flatpak install flathub org.telegram.desktop")
os.system("flatpak install flathub org.ksnip.ksnip")
print("FLATPAK PACKAGES INSTALLED!")