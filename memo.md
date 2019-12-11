# init

sudo apt-get install -y make zsh
sudo chsh -s /usr/bin/zsh vagrant
curl -L https://raw.githubusercontent.com/bto/dotfiles/master/bin/installer.sh | bash

# chroot

- sudo chroot rootfs /bin/bash
- ps -> error
  - mount -t proc proc /proc
- top
- pkill top

# unshare

- sudo unshare -fpm --mount-proc=/proc chroot rootfs /bin/bash
- ps

# setns

- sudo unshare -fpm --mount-proc=/proc chroot rootfs /bin/bash
- sudo ls -l /proc/xxxx/ns
- sudo nsenter --pid=/proc/xxxx/ns/pid unshare -fpm --mount-proc=/proc chroot rootfs /bin/bash
