import os, subprocess
import time, sys

class AutoCustomTerminal:

  def __init__(self) -> None:

    self.check_root()
    if len(sys.argv) == 2:
      self.revert()
      sys.exit(0)

    self.users = self.users_custom()
    self.install_packages()
    self.install_font()
    self.configPowerLevel()
    pass

  def check_root(self):
    if (os.getuid() != 0):
      print("\n[-] Necesitas ser root")
      exit(1)

    print("\n[+] Root verificado")

  def users_custom(self):

    current_user = os.popen("pwd").read().split('/')[2]

    print("\nUSARIOS A APLICAR LA TERMINAL")
    print(f"\n 1 - Todos\n 2 - Usuario actual {current_user}")

    option = int(input("\n-> "))

    if option == 2:
      return [current_user]
    
    else:
      result_terminal = os.popen("ls /home").readlines()

      users = [user.replace("\n","") for user in result_terminal]
      return users

  def install_packages(self):
    print("\nInstalling Packages")
    time.sleep(2)
    os.system("sudo apt install zsh zsh-syntax-highlighting -y")
    os.system("sudo dpkg -i ./packages/lsd.deb")
    os.system("sudo dpkg -i ./packages/bat.deb")
    print("\n[+] Packages installed")
    time.sleep(2)

  def install_font(self):

    print("\n[?] Installing Font")
    time.sleep(3)
    os.system("sudo mkdir /usr/share/fonts/HackFont")
    os.system("sudo cp ./packages/Hack.zip /usr/share/fonts/HackFont")
    os.system("sudo unzip /usr/share/fonts/HackFont/Hack.zip")
    os.system("sudo mv HackNerd* /usr/share/fonts/HackFont/")
    os.system("sudo fc-cache -f")

    print("\n[+] Font Installed")
    time.sleep(2)

    os.system("clear")

    print("\n\nNow open a new terminal and select the new font, then press enter here...\n")
    input()

  def configPowerLevel(self):

    print("\nConfig Powerlevel10k")

    time.sleep(2)

    for user in self.users:
      os.system(f"sudo chsh -s /usr/bin/zsh {user}")
      os.system(f"sudo chmod 707 /home/{user}")
      os.system(f"git clone --depth=1 https://github.com/romkatv/powerlevel10k.git /home/{user}/.powerlevel10k")
      os.system(f"mv /home/{user}/.zshrc /home/{user}/.zshrc_copy")
      os.system(f"cp ./packages/zshrc /home/{user}/.zshrc")
      os.system(f"sudo chmod 766 /home/{user}/.zshrc")

    print("\nAll configured\n")
    print("Logging out the user in 15s")
    for x in range(15):
      print(f"Logging out: {x} seconds")
      time.sleep(1)

    os.system("sudo kill -9 -1")

  def revert(self):
    print("\nUninstalling...")
    time.sleep(2)

    result_terminal = os.popen("ls /home").readlines()

    users = [user.replace("\n","") for user in result_terminal]

    for user in users:
      os.system(f"sudo rm -rf /home/{user}/.powerlevel10k")
      os.system(f"sudo rm -f /home/{user}/.p10k")
      os.system(f"sudo rm -f /home/{user}/.zshrc")
      os.system(f"sudo mv /home/{user}/.zshrc_copy /home/{user}/.zshrc")

    os.system("sudo rm -f LICENSE.md")
    os.system("sudo rm -f README.md")
    os.system("sudo apt remove lsd bat -y")
    os.system("sudo rm -rf /usr/share/fonts/HackFont")
    print("\n[+] Uninstalled successfully")

if __name__ == '__main__':

  AutoCustomTerminal()