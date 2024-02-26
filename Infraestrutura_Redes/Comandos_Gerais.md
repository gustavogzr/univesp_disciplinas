# Comandos Gerais

## Instalação do Apache

~~~bash
sudo apt-get update
sudo apt-get install apache2

sudo systemctl status apache2 # Verificar o status do Apache
sudo systemctl start apache2 # Iniciar o Apache
sudo systemctl stop apache2 # Parar o Apache
sudo systemctl restart apache2 # Reiniciar o Apache
sudo systemctl reload apache2 # Recarregar o Apache sem perder as conexões

hostname -I # Verificar o IP do servidor

sudo mkdir /var/www/meudominio/ # Criar um diretório para o site

sudo chown -R $USER:$USER /var/www/meudominio/ # Alterar o proprietário do diretório

sudo chmod -R 755 /var/www/meudominio/ # Alterar as permissões do diretório

sudo pico /var/www/meudominio/index.html # Criar um arquivo index.html

sudo pico /etc/apache2/sites-available/meudominio.conf # Criar um arquivo de configuração do site

sudo a2ensite meudominio.conf # Habilitar o site

sudo a2dissite 000-default.conf # Desabilitar o site padrão

sudo apache2ctl configtest # Verificar a configuração do Apache

sudo systemctl restart apache2 # Reiniciar o Apache

sudo pico /var/log/apache2/access.log # Verificar os acessos ao site

sudo pico /var/log/apache2/error.log # Verificar os erros do site
~~~

## Instalação do MySQL

~~~bash
sudo apt-get update
sudo apt-get install mysql-server
sudo mysql_secure_installation

sudo mysql # Acessar o MySQL
SHOW DATABASES; # Mostrar os bancos de dados
USE mysql; # Acessar o banco de dados mysql
SHOW TABLES; # Mostrar as tabelas do banco de dados mysql
SELECT * FROM plugin; # Mostrar os registros da tabela plugin
QUIT; # Sair do MySQL
~~~

## Instalação do PHP

~~~bash
sudo apt-get update # Atualizar a lista de pacotes
sudo apt-get install php libapache2-mod-php php-mysql # Instalar o PHP, o módulo do Apache e o driver do MySQL
php -v # Verificar a versão do PHP

sudo pico /etc/apache2/mods-enabled/dir.conf # Alterar a prioridade dos arquivos index.php - colocar o index.php em primeiro lugar

sudo systemctl reload apache2 # Recarregar o Apache com novas configurações

sudo pico /var/www/meudominio/info.php # Criar um arquivo info.php
~~~

Acessar via browser a URL <http://IP/info.php>

## Observação sobre Linux e superusuário

~~~bash
sudo su # Acessar o superusuário
exit # Sair do superusuário
~~~

Evitar o uso do superusuário para não comprometer o sistema.

## Criar aplicação

~~~bash
sudo mysql # Acessar o MySQL
~~~

~~~sql
CREATE DATABASE exemploinfra; -- Criar um banco de dados
CREATE USER 'alunoinfra'@'%' IDENTIFIED WITH mysql_native_password BY 'Aluno123#@'; -- Criar um usuário