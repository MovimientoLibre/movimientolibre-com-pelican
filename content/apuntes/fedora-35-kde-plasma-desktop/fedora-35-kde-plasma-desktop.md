Title: Post-instalación de Fedora 35 KDE Plasma Desktop
Summary: Después de instalar Fedora 35 KDE Plasma Desktop siga estas recomendaciones para mejorar su nuevo sistema operativo.
Slug: fedora-35-kde-plasma-desktop
Date: 2021-10-31 13:36:00
Modified: 2021-10-31 13:36:00
Category: apuntes
Tags: fedora
Preview: fedora-logo-icon.png


## Instale de Fedora 35

**Nota:** Al momento de escribir este apunte aun estaba la versión 35 como _beta_. Muy pronto estará marcada como _final_.

El propósito de este apunte es compartir las instrucciones _post_ instalación de Fedora 35 con KDE Plasma.

Luego de instalar [Fedora 35 KDE Plasma Desktop](https://spins.fedoraproject.org/kde/download/index.html) con una memoria USB hacemos una actualización...

    $ sudo dnf --refresh check-update
    $ sudo dnf update

Y reiniciamos...

    # systemctl reboot

A continuación vamos a convertir la instalación de un KDE _puro_ a una _herramienta poderosa_ para desarrollo de software.

## A a partir de aquí use root

Abra una terminal y cambie a _root_

    sudo su -

## ¡Vamos a instalar!

Instalar LibreOffice

    dnf groupinstall LibreOffice
    dnf install libreoffice-help-es libreoffice-langpack-es

Instalar soporte para contenedores

    dnf groupinstall 'Container Management' --with-optional

Instalar Libvirt

    dnf groupinstall 'Virtualization' --with-optional

Instalar Kate

    dnf install kate
    dnf install falkon

Instalar Google Chrome

    dnf install fedora-workstation-repositories
    dnf repolist --all
    dnf config-manager --set-enabled google-chrome
    dnf --refresh update
    dnf install google-chrome-stable

Instalar tipografías

    dnf install google-roboto-condensed-fonts google-roboto-fonts google-roboto-mono-fonts
    dnf install google-droid-fonts-all
    dnf install mozilla-fira-mono-fonts mozilla-fira-sans-fonts
    dnf install terminus-fonts

Instalar VSCode

    rpm --import https://packages.microsoft.com/keys/microsoft.asc
    sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
    dnf --refresh update
    dnf install code

Instalar Sublime Text

    rpm -v --import https://download.sublimetext.com/sublimehq-rpm-pub.gpg
    dnf config-manager --add-repo https://download.sublimetext.com/rpm/stable/x86_64/sublime-text.repo
    dnf --refresh update
    dnf install sublime-text

Instalar Calibre

    dnf install calibre

Instalar GIMP

    dnf install gimp

Instalar Inkscape

    dnf install inkscape

Instalar soporte de impresoras HP

    dnf install hplip

Instalar aplicaciones de terminal

    dnf install figlet pwgen youtube-dl hwinfo htop system-storage-manager

Instalar RClone

    dnf install rclone

## Eliminar KDE PIM

Bueno, siendo _fan_ de KDE no uso la suite de información personal (PIM), así que la retiro con...

    dnf remove kdepim-runtime kdepim-addons
    dnf remove akregator
    dnf autoremove \*akonadi\*

## RMP Fusion

RPM Fusion nos brinda el software que necesitamos pero que no cumple con las directrices del Software Libre. Ejecutar

    dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

Actualizar

    dnf --refresh update
    dnf groupupdate core
    dnf groupupdate multimedia --setop="install_weak_deps=False" --exclude=PackageKit-gstreamer-plugin
    dnf groupupdate sound-and-video

Instalar aplicaciones multimedia

    dnf install audacious audacious-plugins-freeworld audacious-plugins-freeworld-aac audacious-plugins-freeworld-ffaudio audacious-plugins-freeworld-mms
    dnf install mplayer mencoder
    dnf install ffmpeg ffmpegthumbs
    dnf install moc

Instalar el editor de video KDEnlive

    dnf install kdenlive frei0r-plugins

## Más software para desarrollo

Instalar todas las herramientas para Python

    dnf groupinstall 'Python Classroom'

Instalar la base de datos PostgreSQL

    dnf install postgresql postgresql-server

Instalar la base de datos MariaDB

    dnf install mariadb qt5-qtbase-mysql

Instalar Redis y wkhtmltopdf para crear PDFs con Python

    dnf install redis
    dnf install wkhtmltopdf

Instalar seahorse para administrar las contrasenas de Gnome, porque VSCode lo utiliza

    dnf install seahorse

## Limpieza

Ejecutar la orden de eliminar las dependencias que no se usen...

    dnf autoremove
