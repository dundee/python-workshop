# Python workshop - P2P chatovací aplikace

Ukázkový projekt demonstrující možnosti jazyka python při realizaci P2P chatovací aplikace.
Projekt je používán v rámci python workshopu pořádaného v rámci Seznam IT akademie.

## Příprava prostředí pro workshop (debian)

### Aktualizace systému
    sudo apt-get update
    sudo apt-get upgrade

### Instalace vimu a gitu
    sudo apt-get install vim
    sudo apt-get install git git-man liberror-perl

#### Instalace Atomu a pluginů
    wget https://atom.io/download/deb -O atom-amd64.deb
    sudo dpkg -i atom-amd64.deb
    apm install autocomplete-python \
        goto-definition \
        highlight-selected \
        linter \
        linter-pep8 \
        linter-flake8 \
        linter-pylint \
        minimap \
        project-manager \
        tree-ignore

### Instalace SublimeText 3
    wget https://download.sublimetext.com/sublime-text_build-3126_amd64.deb
    sudo dpkg -i sublime-text_build-3126_amd64.deb

### Instalace deb a pip balicků
    sudo apt-get install dialog
    sudo apt-get install python3
    sudo apt-get install python3-pip
    sudo pip3 install flake8 pep8 pylint
    sudo pip3 install werkzeug pytest requests pythondialog sqlpuzzle blessed
    sudo pip3 install mypy-lang
