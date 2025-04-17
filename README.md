# checkout-transparent-mp

Um exemplo bem simples de como fazer um checkout transparente (sem sair de sua pagina) no Mercago Pago. Feito em Python + JS + HTML.
Antes de qualquer coisa, crie sua conta no mercado pago como vendedor e obtenha suas credenciais.
O Mercado Pago, vai fornecer suas chaves publicas e keys tanto para produção quanto para sandbox (testes).

Para quem tiver dificuldade de criar uma conta de vendedor e configurar a aplicação, este vídeo ajuda:
https://www.youtube.com/watch?v=gwqPNEW0xVY

No sandbox, utilize cartões virtuais gerados pelo MP. Caso precise pesquise no Claude ou ChatGPT sobre cartões fictícios para sandbox do Mercado Pago.
De qualquer forma, vou deixar no template um modelo que funciona bem.

Esses cartões não geram cobrança e nem aparecem no seu painel do MP como transações realizadas.

1) PRIMEIRO PASSO:
   Baixar repositório para seu local de dev

2) SEGUNDO PASSO:
   Instalar dependência: pip install mercadopago (como é só uma, não gerei requirements.txt)

3) TERCEIRO PASSO:
   Substituir na view, suas chaves públicas e suas access keys (teste ou produção)

4) QUARTO PASSO:
   Se estiver tudo ok, rode o servidor e acesse: http://127.0.0.1:8000/checkout/

5) QUINTO PASSO:
   Informe os dodos de teste e clique em Pagar. Pronto, o pagamento foi realizado (você receberá mensagem) e será redirecionado para a página que desejar.

OBSERVAÇÕES:

Os dados trabalhados aqui estão em uma constante. Eles devem ser adaptados para buscar de sua loja, os valores corretos, assim como dados do comprador, que devem ser resgatados do usuáriologado etc...

Dentro de Template/ deixei 4 arquivos: o de checkout, de sucesso, de pagamento pendente e de erro. Adapte conforme sua necessidade.

Caso queira, adapte a view para gravar em banco as informações de pagamento etc.... neste exemplo não faço isso. Outo ponto é que pode ser interessante deixar suas access_key em variáveis de ambiente.

É importante redigitar todas as informações do formulário para simular aprovação do mercado pago.

TELAS DO SISTEMA:

![image](https://github.com/user-attachments/assets/291dcb91-1245-44ba-a132-4d0a2d34d2ee)

![image](https://github.com/user-attachments/assets/6e45d214-b4cd-49f3-9e51-3fe1db9fa83f)

![image](https://github.com/user-attachments/assets/a1afecb9-adee-4fc3-9b8f-cd537deaeafd)

