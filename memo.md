# init

sudo apt-get install -y make zsh
sudo chsh -s /usr/bin/zsh vagrant
curl -L https://raw.githubusercontent.com/bto/dotfiles/master/bin/installer.sh | bash

# chroot

sudo chroot rootfs /bin/bash
ps
top
pkill top

# unshare

sudo unshare -fp chroot rootfs /bin/bash
ps

# setns

sudo unshare -fp chroot rootfs /bin/bash
sudo ls -l /proc/xxxx/ns
sudo nsenter --pid=/proc/xxxx/ns/pid chroot rootfs /bin/bash

# chroot with mount

sudo mount --bind -o ro $PWD/readonlyfiles $PWD/rootfs/var/readonlyfiles
sudo chroot rootfs /bin/bash
