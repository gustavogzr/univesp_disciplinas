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
GRANT ALL ON exemploinfra.* TO 'alunoinfra'@'%'; -- Conceder privilégios ao usuário
exit
~~~

~~~bash
mysql -u alunoinfra -p # Acessar o MySQL com o usuário criado
~~~

~~~sql
SHOW DATABASES; -- Mostrar os bancos de dados

CREATE TABLE exemploinfra.computador (
    item_id INT AUTO_INCREMENT,
    conteudo VARCHAR(255),
    PRIMARY KEY(item_id)
); -- Criar uma tabela

USE exemploinfra; -- Acessar o banco de dados exemploinfra
SELECT * FROM computador; -- Mostrar os registros da tabela computador
SHOW TABLES; -- Mostrar as tabelas do banco de dados exemploinfra

INSERT INTO computador (conteudo) VALUES ("Placa Mãe"); -- Inserir um registro na tabela computador

SELECT * FROM computador; -- Mostrar os registros da tabela computador

INSERT INTO computador (conteudo) VALUES 
    ("Memória"),
    ("Processador"),
    ("Placa de Vídeo"),
    ("Fonte"),
    ("Monitor"),
    ("Teclado"),
    ("Mouse")
;-- Inserir vários registros na tabela computador

SELECT * FROM computador; -- Mostrar os registros da tabela computador

exit -- Sair do MySQL
~~~

~~~bash
sudo pico /var/www/meudominio/listacomponentes.php # Criar um arquivo listacomponentes.php

hostname -I # Verificar o IP do servidor
~~~

Acessar via browser a URL: <http://IP/listacomponentes.php>

## Alterando forma de obtenção de IP da máquina virtual

- Desligar a máquina virtual
- Clicar com o botão direito na máquina virtual
- Clicar em Configurações
- Clicar em Rede
- Alterar a opção de Adaptador de Rede para "Placa em Modo Bridge"
- Clicar em OK
- Iniciar a máquina virtual
- Verificar o novo IP da máquina virtual

~~~bash
sudo apt-get install net-tools # Instalar o pacote net-tools
ifconfig # Verificar o IP da máquina virtual
ping 192.168.15.15 # Verificar a conectividade com a máquina virtual

sudo install openssh-server # Instalar o servidor SSH
~~~

No computador local, acessar via terminal a máquina virtual:

~~~bash
ssh aluno@192.168.15.15 # Acessar a máquina virtual
# inserir a senha do usuário aluno
sudo shutdown -h now # Desligar a máquina virtual
~~~

## Alterar compartilhamento de pasta

- Desligar a máquina virtual
- Clicar com o botão direito na máquina virtual
- Clicar em Configurações
- Clicar em Pastas Compartilhadas
- Clicar em "Acrescentar uma nova pasta compartilhada"
- Selecionar a pasta a ser compartilhada
- Preencher o campo "Ponto de montagem" com o caminho onde a pasta será montada
- Marcar a opção "Montar automaticamente"
- Clicar em OK
- Iniciar a máquina virtual
- Clicar em "Dispositivos" no menu da máquina virtual
- Clicar em "Inserir imagem de CD dos Adicionais para Convidado"
- Clicar em "Download"

## Criar uma aplicação API REST

~~~bash
sudo apt-get update # Atualizar a lista de pacotes
sudo mysql -u root -p # Acessar o MySQL
~~~

~~~sql
SHOW DATABASES; -- Mostrar os bancos de dados
USE exemploinfra; -- Acessar o banco de dados exemploinfra
SELECT * FROM computador; -- Mostrar os registros da tabela computador
QUIT; -- Sair do MySQL
~~~

~~~bash
cd /var/www/meudominio/ # Acessar o diretório do site
mkdir exemploinfra-rest # Criar um diretório para a aplicação
ls -la # Listar os arquivos e diretórios
cd exemploinfra-rest/ # Acessar o diretório da aplicação
mkdir api # Criar um diretório para a API
mkdir classe # Criar um diretório para as classes
mkdir config # Criar um diretório para as configurações
cd config/ # Acessar o diretório das configurações
sudo pico database.php # Criar um arquivo database.php
cd .. # Voltar um diretório
cd classe/ # Acessar o diretório das classes
sudo pico pecas.php # Criar um arquivo pecas.php
cd .. # Voltar um diretório
cd api/ # Acessar o diretório da API
sudo pico cria.php # Criar um arquivo cria.php
sudo pico atualiza.php # Criar um arquivo atualiza.php
sudo pico apaga.php # Criar um arquivo apaga.php
sudo pico lertudo.php # Criar um arquivo lertudo.php
sudo pico leiaitem.php # Criar um arquivo leiaitem.php

sudo snap install postman # Instalar o postman
postman # Abrir o postman
~~~

## Instalação e Uso do Docker

~~~bash
sudo apt-get update # Atualizar a lista de pacotes

sudo apt install apt-transport-https ca-certificates curl software-properties-common # Instalar pacotes necessários

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - # Adicionar a chave GPG do repositório oficial do Docker

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable" # Adicionar o repositório do Docker

sudo apt update # Atualizar a lista de pacotes

apt-cache policy docker-ce # Verificar a disponibilidade do Docker

sudo apt install docker-ce # Instalar o Docker

sudo systemctl status docker # Verificar o status do Docker

sudo systemctl start docker # Iniciar o Docker

sudo usermod -aG docker ${USER} # Adicionar o usuário ao grupo docker

su - ${USER} # Sair e entrar novamente no sistema

id -nG # Verificar os grupos do usuário. O grupo docker deve aparecer

docker # listar os comandos do Docker

docker --version # Verificar a versão do Docker

docker run hello-world # Executar o container hello-world. Normalmente usado para verificar se a instalação do Docker está correta

docker pull ubuntu # Baixar a imagem do Ubuntu

docker images # Listar as imagens baixadas

docker run -it ubuntu # Executar o container do Ubuntu. O parâmetro -it é para executar o container em modo interativo

docker stop container_id # Parar o container. O container_id é o ID do container

apt update # Atualizar a lista de pacotes do Ubuntu. Não é necessário o uso do sudo pois o usuário já está no modo root

apt install nano net-tools systemctl # Instalar os pacotes nano, net-tools e systemctl

apt-get install apache2 # Instalar o Apache

systemctl status apache2 # Verificar o status do Apache

systemctl start apache2 # Iniciar o Apache

hostname -I # Verificar o IP do container
~~~

No navegador do computador local, acessar a URL: <http://IP_do_container>

~~~bash
mkdir /var/www/meudominio # Criar um diretório para o site

chown -R $USER:$USER /var/www/meudominio # Alterar o proprietário do diretório

chmod -R 755 /var/www/meudominio # Alterar as permissões do diretório

pico /var/www/meudominio/index.html # Criar um arquivo index.html

pico /etc/apache2/sites-available/meudominio.conf # Criar um arquivo de configuração do site

a2ensite meudominio.conf # Habilitar o site

a2dissite 000-default.conf # Desabilitar o site padrão

apache2ctl configtest # Verificar a configuração do Apache. A saída deve ser "Syntax OK"

systemctl restart apache2 # Reiniciar o Apache
~~~

No navegador do computador local, acessar a URL: <http://IP_do_container>

~~~bash
apt-get install mysql-server # Instalar o MySQL

service mysql start # Iniciar o MySQL

mysql_secure_installation # Configurar o MySQL

mysql # Acessar o MySQL

apt-get install php libapache2-mod-php php-mysql # Instalar o PHP, o módulo do Apache e o driver do MySQL

php -v # Verificar a versão do PHP

pico /etc/apache2/mods-enabled/dir.conf # Alterar a prioridade dos arquivos index.php - colocar o index.php em primeiro lugar

systemctl restart apache2 # Reiniciar o Apache

pico /var/www/meudominio/info.php # Criar um arquivo info.php para testar o PHP
~~~

Acessar via browser a URL <http://IP_do_container/info.php>

~~~bash
docker commit -m "Tools, Apache, PHP e MySQL" -a "Gustavo Zarpelon Radaelli" ad80b1bd6f54 aluno/ubuntu-infra # Criar uma nova imagem com as ferramentas instaladas

docker images # Listar as imagens

docker ps -a # Listar os containers.

docker ps -l # Listar o último container criado

docker stop container_id # Parar o container. O container_id é o ID do container

docker start container_id # Iniciar o container. O container_id é o ID do container

docker exec -it container_id bash # Acessar o container. O container_id é o ID do container

docker rm container_id # Remover o container. O container_id é o ID do container

docker login -u docker_registry_username # Fazer login no Docker Hub. O docker_registry_username é o nome de usuário do Docker Hub

docker tag aluno/ubuntu-infra docker_registry_username/ubuntu-infra # Adicionar uma tag à imagem. O docker_registry_username é o nome de usuário do Docker Hub

docker push docker_registry_username/ubuntu-infra # Enviar a imagem para o Docker Hub. O docker_registry_username é o nome de usuário do Docker Hub
~~~

## Instalação do Google Cloud SDK (Software Development Kit)

Seguir as instruções do site <https://cloud.google.com/sdk/docs/install>

Para verificar a instalação, executar o comando:

~~~bash
gcloud # a saída irá mostrar os comandos do gcloud

gcloud --version # verificar a versão do gcloud

gcloud init # inicializar o gcloud

gcloud auth login # autenticar no gcloud
~~~


~~~bash
# Mostrar todas as imagens criadas localmente pelo docker:
docker images
## Instalação de AWS CLI

~~~bash
sudo apt-get install unzip # Instalar o unzip

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" # Baixar o arquivo zip da AWS CLI

unzip awscliv2.zip # Descompactar o arquivo zip

sudo ./aws/install # Instalar a AWS CLI
~~~
