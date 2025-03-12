## TPC4 - Analisador léxico

**Data:** 2025-02-28

## Resumo: 
Este TPC consiste em criar um analisador léxico para uma linguagem de query. Por exemplo:

        #DBPedia: obras de Chuck Berry

        SELECT ?nome ?desc WHERE {
            ?s a dbo:MusicalArtist.
            ?s foaf:name "Chuck Berry"@en.
            ?w dbo:artist ?s.
            ?w foaf:name ?nome.
            ?w dbo:abstract ?desc.
        } LIMIT 1000

O resultado esperado seria:

        COMMENT #DBPedia: obras de Chuck Berry
        SELECT SELECT
        VAR nome
        VAR desc
        WHERE WHERE
        LBRAC {
        VAR s
        A a
        PREF dbo:MusicalArtist
        DOT .
        VAR s
        PREF foaf:name
        STRING Chuck Berry
        LANG @en
        DOT .
        VAR w
        PREF dbo:artist
        VAR s
        DOT .
        VAR w
        PREF foaf:name
        VAR nome
        DOT .
        VAR w
        PREF dbo:abstract
        VAR desc
        DOT .
        RBRAC }
        LIMIT LIMIT
        INT 1000

## Resultados
- [Código fonte (`analex.py`)](analex.py)

## Autor

**Nome:** Duarte Alexandre Oliveira Faria

**Número:** a95609

**Fotografia:**

![Fotografia do Autor](TPC1\20200928.jpg) 