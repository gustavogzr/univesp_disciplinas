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
sudo mysql # Acessar o MySQL
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
cd.. # Voltar um diretório
cd classe/ # Acessar o diretório das classes
sudo pico pecas.php # Criar um arquivo pecas.php
cd.. # Voltar um diretório
cd api/ # Acessar o diretório da API
sudo pico cria.php # Criar um arquivo cria.php
sudo pico atualiza.php # Criar um arquivo atualiza.php
sudo pico apaga.php # Criar um arquivo apaga.php
sudo pico lertudo.php # Criar um arquivo lertudo.php
sudo pico leiaitem.php # Criar um arquivo leiaitem.php

sudo snap install postman # Instalar o postman
postman # Abrir o postman
~~~
