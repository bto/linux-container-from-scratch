# init

sudo apt-get install -y make zsh
sudo chsh -s /usr/bin/zsh vagrant
curl -L https://raw.githubusercontent.com/bto/dotfiles/master/bin/installer.sh | bash

# chroot

sudo chroot rootfs /bin/bash
ps
top
pkill top

# chroot with mount

sudo mount --bind -o ro $PWD/readonlyfiles $PWD/rootfs/var/readonlyfiles
sudo chroot rootfs /bin/bash
cat /var/readonlyfiles/hello.txt
echo hello >> /var/readonlyfiles/hello.txt

# unshare

sudo unshare -fp chroot rootfs /bin/bash
ps

# setns

sudo unshare -fp chroot rootfs /bin/bash
sudo ls -l /proc/xxxx/ns
sudo nsenter --pid=/proc/xxxx/ns/pid chroot rootfs /bin/bash

# cgroups

sudo mkdir /sys/fs/cgroup/memory/demo
ls /sys/fs/cgroup/memory/demo
echo $((1024 * 1024 * 100)) | sudo tee /sys/fs/cgroup/memory/demo/memory.limit_in_bytes
cat /sys/fs/cgroup/memory/demo/memory.limit_in_bytes

cat /sys/fs/cgroup/memory/user.slice/tasks
echo $$ | sudo tee -a /sys/fs/cgroup/memory/demo/tasks
cat /sys/fs/cgroup/memory/demo/tasks
cat /sys/fs/cgroup/memory/user.slice/tasks

# Capabilities

cp /bin/ping .
sudo setcap cap_net_raw+ep ./ping
getcap ./ping
./ping 127.0.0.1

capsh --print
sudo /bin/bash
capsh --print
sudo capsh --drop=cap_chown,cap_setpcap,cap_setfcap,cap_sys_admin --chroot=$PWD/rootfs --
