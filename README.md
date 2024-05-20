# Projeto_Arquitetura_de_Software
Caso de Uso: Sistema de Vendas de Produtos Naturais

Caso de Uso: Sistema de Vendas de Produtos Naturais

• Ator Principal: Funcionário (acesso apenas no lançamento de vendas)

• Ator Secundário: Administrador do Sistema (acesso total)

Casos de Uso:

• UC01 - Autenticação:

o O funcionário acessa o sistema e é solicitado a autenticar-se inserindo seu nome
de usuário e senha.

o Se as credenciais estiverem corretas, o cliente é autenticado e pode acessar as
funcionalidades do sistema.

o Estrutura de dados: login, nome, email.

• UC02 - Cadastro de Produto:

o O administrador do sistema pode adicionar novos produtos ao catálogo.

o Após o cadastro, os produtos são exibidos no site para os clientes.

o Estrutura de dados: nome, descrição, preço custo, preço vendas, peso,

quantidade comprado, quantidade vendida, Fabricante, Grupo e Subgrupo

• UC03 - Cadastro do Fabricante:

o O administrador pode cadastrar informações sobre os fabricantes dos produtos
naturais.

o Esses dados são associados aos produtos para fornecer informações adicionais
aos clientes.

o Estrutura de dados: nome fantasia, razão social, cnpj, endereço, telefone, email,
vendedor

• UC04 - Cadastro de Grupo e UC05 - Subgrupo:

o Os produtos naturais podem ser agrupados em categorias e subcategorias para
facilitar a navegação.

o O administrador pode criar novos grupos e subgrupos, por exemplo, "Alimentos
Orgânicos" pode ser um grupo, com "Frutas", "Verduras" e "Grãos" como
subgrupos.

o Estrutura de dados: nome e descrição

• UC06 - Lançamento de Vendas:

o O funcionário pode adicionar itens que foram escolhidos para compra.

o O sistema calcula valor de venda e quantidade do produto.

o Ao finalizar todos os itens escolhidos, o sistema registra a venda, atualiza o
estoque.

2
o Estrutura de dados: Produto, Fabricante, Grupo, SubGrupo, preço venda,
quantidade, data e hora venda

• UC07 - Visualizar Vendas:

o O funcionário pode visualizar através de gráficos a situação atual do comércio.

o Visualiza na mesma tela 3x3 gráficos* com as seguintes temáticas

▪ Gráfico de Linha: apresentar o valor do custo Total e o valor venda Total
mensal do ano corrente. (Vendas)

▪ Gráfico de Barras: apresentar o valor da quantidade comprado total e a
quantidade vendida total mensal do ano corrente. (Produto)

▪ Gráfico de Dispersão: apresentar o percentual de lucro dos produtos
vendidos mensal do ano corrente. (Produto)

▪ Gráfico de Pizza: apresentar os 3 produtos mais vendidos em
quantidade mensal do ano corrente. (Vendas)

▪ Gráfico de Barras e Linha: apresentar os 4 grupos de produtos mais
vendidos mensal do ano corrente com a meta de quantidade >= 1000
unidades. (Vendas)

▪ Tabela Analítica: listar os produtos que estão com estoque baixo e
ordem decrescente.

*Use as libs plotly.express e plotly.graph_objs

![Captura de tela 2024-05-11 215736](https://github.com/EricIkeda1/Projeto_Arquitetura_de_Software/assets/93358246/0fcb5de5-0f92-42e4-90ea-6181ddb70123)

Fluxo de Eventos Típico:

O funcionário acessa o sistema da loja online de produtos naturais.
Ele faz login usando seu nome de usuário e senha.
O funcionário navega pelos produtos, filtrando por fabricante, grupo ou subgrupo, se desejar.
Ele adiciona os produtos desejados aos itens de compras e o sistema calcula valor de venda e quantidade do produto.
Ao finalizar os itens escolhidos, o sistema registra a venda, atualiza o estoque
Arquitetura do sistema Linguagem: Python Framework: Django ServidorWeb: Apache usar módulo mod_wsgi Estilo de arquitetural: estilo em camadas (3) com estilo MVC, conforme ilustração abaixo:

![Captura de tela 2024-05-11 215842](https://github.com/EricIkeda1/Projeto_Arquitetura_de_Software/assets/93358246/4148c0e1-de91-41a5-bdf9-f5e93278afdf)

Design Patterns:

• Padrões de criação:

o Factory Method: Fornece uma interface para criação de famílias de objetos relacionados ou dependentes sem especificar suas classes concretas. o Singleton: Garante que uma classe tenha somente uma instância e fornece um ponto global de acesso para ela.

• Padrões comportamentais: o Observer: Define uma dependência um-para-muitos entre objetos, de modo que, quando um objeto muda de estado, todos os seus dependentes são automaticamente notificados e atualizados
