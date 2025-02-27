## TPC2 - Dataset de obras musicais

**Data:** 2025-02-21

## Resumo: 
Este TPC, tem como objetivo criar um conversor de MarkDown para HTML.
Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"
- In: `# Exemplo`
- Out: `<h1>Exemplo</h1>`
- Bold: pedaços de texto entre "**":
- In: `Este é um **exemplo** ...`
- Out: `Este é um <b>exemplo</b> ...`
- Itálico: pedaços de texto entre "*":
- In: `Este é um *exemplo* ...`
- Out: `Este é um <i>exemplo</i> ...`
Lista numerada:
In: <md>
    1. Primeiro item
    2. Segundo item
    3. Terceiro item
Out:
<html>
    <ol>
    <li>Primeiro item</li>
    <li>Segundo item</li>
    <li>Terceiro item</li>
    </ol>
Link: [texto](endereço URL)
In: ` Como pode ser consultado em [página da UC](http://www.uc.pt)`
Out: `Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>`

## Resultados
- [Código fonte (`md2 html.py`)](md2html.py)
- [Ficheiro Markdown)](example.md)
- [Ficheiro HTML](example.html)

## Autor

**Nome:** Duarte Alexandre Oliveira Faria

**Número:** a95609

**Fotografia:**

![Fotografia do Autor](TPC1/20200928.jpg) 