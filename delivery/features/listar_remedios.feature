Funcionalidade: Listar remédios
    Para poder comprar um remédio
    Como um usuário do sistema
    Eu gostaria de ver uma lista contendo os remédios para eu escolher

    Cenário: Listando todos os remédios
        Dado que existem 10 remédios cadastrados no banco de dados
        Quando eu vou para a página de listagem de remédios
        Então eu deveria ver a listagem com o nome dos 10 remédios
