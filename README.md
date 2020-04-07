# Firebase Cloud Messaging Server

O Firebase Cloud Messaging (FCM) é uma solução de mensagens entre plataformas que permite o envio confiável de notificações sem custo.


Usando o FCM, você pode notificar um app cliente de que novos e-mails ou outros dados estão disponíveis para sincronização. Você pode enviar mensagens de notificação para promover novas interações e a retenção de usuários. Para casos de uso como mensagens instantâneas, uma mensagem pode transferir um payload de até 4 KB para um app cliente.

## Como executar esse exemplo?
Baixe o arquivo de configuração e coloque dentro de uma pasta chamada `config`. 

Após isso adicione a referencia para este arquivo em `admin.py`.

## Aplicação no Gooex

Para utilização no Gooex será preciso adicionar mais dois campos ao cadastro de usuários. Sendo um campo para `token_web` e outro para `token_mobile`.

Para que assim, um usuário possa receber as notificações em ambos os devices.

É preciso também um endpoint para que essas informações possam ser atualizadas. Pois as vezes acontece de a SDK do Firebase mudar o token (sobretudo na Web).