Vagrant.configure("2") do |config|
  config.vm.box = "debian/bullseye64" # Utilise la box Debian 12 (Bullseye) officielle

  config.vm.provision "shell", inline: <<-SHELL
    # Autoriser les commandes apt sans mot de passe pour l'utilisateur root
    echo 'Defaults rootpw' > /etc/sudoers.d/apt
    echo 'root ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers.d/apt
    chmod 440 /etc/sudoers.d/apt

    # Mise à jour du système via apt
    apt update -y
  SHELL
end