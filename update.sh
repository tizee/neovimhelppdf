#!/bin/bash
# Download updated vim documentation and faq
set -e

echo Getting vim
if [[ -d neovim ]]; then
    ( cd neovim; git pull )
else
    git clone https://github.com/neovim/neovim.git --depth 1
fi

if ! [[ -d doc ]]; then
    echo making doc directory
    mkdir doc
fi

echo Copying files into doc directory
cp neovim/runtime/doc/*.txt doc

