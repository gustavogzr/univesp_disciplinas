# Instalando e Utilizado o OpenShift

Realizar download do OpenShift no seguinte link:
<https://github.com/openshift/origin/releases/download/v3.11.0/openshift-origin-client-tools-v3.11.0-0cbc58b-linux-64bit.tar.gz>

Tratando o arquivo baixado:

~~~bash
tar -xvzf openshift-origin-client-tools-v3.11.0-0cbc58b-linux-64bit.tar.gz # Descompactar

cd openshift-origin-client-tools-v3.11.0-0cbc58b-linux-64bit/ # Acessar o diretório

sudo cp oc kubectl /usr/local/bin/ # Copiar os binários oc e kubectl para o diretório /usr/local/bin/

oc version # Verificar a versão do OpenShift
~~~

Criação de um arquivo "daemon.json" e permitir o uso do registro do docker:

~~~bash
sudo pico /etc/docker/daemon.json # Criar o arquivo

~~~

Adicionar o seguinte conteúdo ao arquivo. Este arquivo permite que o docker utilize o registro do OpenShift:

~~~json
{
"insecure-registries" : [ "172.30.0.0/16" ]
}
~~~

Reiniciar o serviço do docker:

~~~bash
sudo systemctl restart docker

sudo systemctl enable docker

sudo systemctl status docker
~~~

Para iniciar o cluster OpenShift usar o seguinte comando:

~~~bash
oc cluster up --public-hostname=192.168.15.22
~~~

Para logar como administrador no OpenShift:

~~~bash
oc login -u system:admin
~~~