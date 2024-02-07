# SMTP-Brute-Force

O script ```smtp_brute.py``` foi desenvolvido em Python para realizar um ataque de força bruta contra um servidor SMTP. Ele tenta enumerar usuários válidos enviando comandos VRFY e analisando as respostas do servidor.

<br>

---

<br>

## **Modo de uso**

```bash
python3 smtp_brute.py IP lista
```

## **Exemplo**

```bash
python3 smtp_brute.py 37.59.174.225 /home/arthurcortesr/lista.txt
```

## **Exemplo de saída**

```bash
----------------------------------
| Pk's Academy - SMTP BRUTE FORCE| 
----------------------------------


Usuario encontrado: user1
Usuario encontrado: user2
...
```

<br>

---

<br>

## **Funcionalidades**

1. Estabelece uma conexão TCP com o servidor SMTP na porta 25.
2. Envia comandos VRFY para verificar a existência de usuários no servidor SMTP.
3. Analisa as respostas do servidor para determinar se um usuário foi encontrado.
4. Utiliza expressões regulares para analisar as respostas do servidor.
5. Fornece feedback em tempo real sobre os usuários encontrados durante a enumeração.

<br>

---

<br>

## **Observações**

1. Este script pode ser detectado por sistemas de detecção de intrusão e bloqueado por firewalls ou sistemas de segurança.

<br>

---

<br>

## **Avisos**

1. Certifique-se de ter permissões adequadas para executar o script, especialmente em ambientes controlados e seguros.
2. O uso deste script em sistemas ou redes sem autorização pode violar leis de privacidade e segurança.
3. O ataque de força bruta é uma técnica intrusiva e deve ser realizada apenas em ambientes controlados e autorizados.
4. É altamente recomendável obter permissão explícita antes de realizar testes de penetração em sistemas ou redes.

