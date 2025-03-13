## TPC4 - Vending Machine

**Data:** 2025-03-08

## Resumo: 
Este TPC consiste em contruir um programa que simule uma máquina de vending.
A máquina tem um stock de produtos: uma lista de triplos, nome do produto, quantidade e preço.


            stock = [
                {"cod": "A23", "nome": "água 0.5L", "quant": 8, "preco"0.7}
                ...
            ]

Onde estará persistido num ficheiro JSON.

Para a simulação, será possível efetuar as seguintes ações:

- LISTAR 
- MOEDA
- SELECIONAR
- SAIR

Como por exemplo:

        maq: 2024-03-08, Stock carregado, Estado atualizado.
        maq: Bom dia. Estou disponível para atender o seu pedido.
        >> LISTAR
        maq:
        cod | nome | quantidade | preço
        ---------------------------------
        A23 água 0.5L 8 0.7
        ...
        >> MOEDA 1e, 20c, 5c, 5c .
        maq: Saldo = 1e30c
        >> SELECIONAR A23
        maq: Pode retirar o produto dispensado "água 0.5L"
        maq: Saldo = 60c
        >> SELECIONAR A23
        maq: Saldo insufuciente para satisfazer o seu pedido
        maq: Saldo = 60c; Pedido = 70c
        >> ...
        ...
        maq: Saldo = 74c
        >> SAIR
        maq: Pode retirar o troco: 1x 50c, 1x 20c e 2x 2c.
        maq: Até à próxima

## Resultados
- [Código fonte (`vending.py`)](vending.py)
- [Ficheiro JSON(`stock.json`)](stock.json)

## Autor

**Nome:** Duarte Alexandre Oliveira Faria

**Número:** a95609

**Fotografia:**

![Fotografia do Autor](TPC1\20200928.jpg)