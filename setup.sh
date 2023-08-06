#/bin/bash

DOTFILES_PATH=$(realpath $(dirname $0))

add_source_if_rc(){
    RC="$1"

    if [ -f $RC ]; then
        string="source $DOTFILES_PATH/.shellrc"
        echo $string >> $RC
    fi
}

# .shellrc
add_source_if_rc "$HOME/.bashrc"
add_source_if_rc "$HOME/.zshrc"

# .gitconfig
test -f $HOME/.gitconfig || ln -s $DOTFILES_PATH/.gitconfig $HOME/.gitconfig

echo dotfiles installation completed!

