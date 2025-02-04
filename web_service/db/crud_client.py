from client_utils import cadastrar_produto, buscar_produto_by_id, buscar_produto_by_nome, \
    listar_produtos, atualizar_produto, remover_produto


if __name__ == '__main__':
    
    while True:

        print('\n\n1 - Cadastrar Produto')
        print('2 - Buscar Produto pelo ID')
        print('3 - Buscar Produto pelo Nome')
        print('4 - Listar Produtos')
        print('5 - Atualizar Produto')
        print('6 - Remover Produto')
        print('7 - Sair')

        opcao = input('\nDigite sua opção: ')

        match opcao:

            case '1':
                
                id_produto = int(input('\n\nID: '))
                nome = input('Nome: ')
                preco = float(input('Preço: '))

                cadastro_ok = cadastrar_produto(id_produto, nome, preco)

                if cadastro_ok is None:
                    print('\n\nErro durante o Cadastro!')
                elif cadastro_ok:
                    print('\n\nProduto Cadastrado com Sucesso!')
                else:
                    print('\n\nErro. Já existe um produto com o mesmo ID cadastrado!')

            case '2':    

                id_produto = int(input('\n\nID: '))
                produto = buscar_produto_by_id(id_produto)
                if produto is None:
                    print('\nNenhum produto encontrado!')
                else:
                    print(f'\nID: {produto["id"]}')
                    print(f'  Nome: {produto["nome"]}')
                    print(f'  Preço: {produto["preco"]}')                    
            
            case '3':                
                
                nome = input('\n\nNome: ')
                produtos = buscar_produto_by_nome(nome)
                if produtos is None:
                    print(f'\n\nNenhum produto foi Encontrado!')
                else:
                    for produto in produtos:
                        print(f'\n\nID: {produto["id"]}')
                        print(f'Nome: {produto["nome"]}')
                        print(f'Preço: {produto["preco"]}')

            case '4':  

                produtos = listar_produtos()
                if produtos is None:
                    print('\n\nErro na requisição!')
                else:
                    print(f'\nTotal Produtos: {len(produtos)}')
                    for produto in produtos:
                        print(f'\nID: {produto["id"]}')
                        print(f'  Nome: {produto["nome"]}')
                        print(f'  Preço: {produto["preco"]}')
            
            case '5':
                
                id_produto = int(input('\n\nID: '))
                
                produto = buscar_produto_by_id(id_produto)
                
                if produto is None:
                
                    print('\nNenhum produto encontrado!')
                
                else:

                    novo_nome = input('\n\nNome: ')
                    novo_preco = input('Preço: ')

                    produto['nome'] = novo_nome if len(novo_nome) > 0 else produto['nome']
                    
                    produto['preco'] = float(novo_preco) if len(novo_preco) > 0 else \
                        produto['preco']

                    atualizacao_ok = atualizar_produto(id_produto, produto)

                    if atualizacao_ok is None:
                        print('\n\nErro durante a Atualização!')
                    elif atualizacao_ok:
                        print('\n\nProduto Atualizado com Sucesso!')

            case '6':
                
                id_produto = int(input('\nID: '))

                remocao_ok = remover_produto(id_produto)

                if remocao_ok is None:
                    print('\n\nErro durante a Remoção!')
                elif remocao_ok:
                    print('\n\nProduto Removido com Sucesso!')
                else:
                    print('\n\nNenhum produto encontrado com o ID informado!')

            case '7':
                print('\nSistema Finalizado!')
                break

            case _:
                print('\n\nOpção Inválida!')
