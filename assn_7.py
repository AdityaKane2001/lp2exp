egrep -c '(vmx|svm)' /proc/cpuinfo
sudo kvm-ok
sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils
sudo adduser ‘username’ libvirt
sudo adduser ‘[username]’ kvm
virsh list --all
sudo systemctl status libvirtd
sudo systemctl enable --now libvirtd
sudo apt install virt-manager
sudo virt-manager

https://phoenixnap.com/kb/ubuntu-install-kvm