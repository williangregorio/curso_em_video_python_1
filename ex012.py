preco_produto = float(input('Digite o valor do produto: R$ '))
desconto = float(input('Digite o valor do desconto: '))
preco_novo = preco_produto - (preco_produto * desconto/100)
print('O valor do produto com o desconto de {}% passa a ser R${:.2f}'.format(desconto,preco_novo))

