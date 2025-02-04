# Simulação e Controle de uma Coqueria usando Modbus e IHMs

## Descrição do Projeto
Este projeto simula o controle de uma coqueria siderúrgica, garantindo que o forno mantenha a temperatura adequada para não comprometer a qualidade do coque. A aplicação realiza leituras e controle de variáveis essenciais por meio do protocolo Modbus, armazenando os dados em um banco SQLite e apresentando interfaces gráficas via ScadaBR e Streamlit.

## Objetivos
- Monitorar e controlar temperatura, tonelagem, posição de tremonhas e trens, nível de gases inertes.
- Aplicar 5 regras de automação para ações como acionamento de ventiladores conforme temperatura.
- Simular os valores das variáveis via servidor Modbus.
- Criar um web service com API para integração e consumo de dados históricos.
- Desenvolver duas IHMs:
- ScadaBR para visualização estática e controle.
- Streamlit para visualização dinâmica e análises gráficas.


## Arquitetura
- Servidor Modbus: Simula sensores e dispositivos industriais.
- Web Service: API REST para comunicação entre o Modbus e os IHMs.
- Banco de Dados SQLite: Armazena valores das variáveis, timestamps e históricos.
- IHMs:
1. ScadaBR: Interface estática para supervisão.
2. Streamlit: Dashboard dinâmico com gráficos.

## Regras de Automação
1. Se temperatura > 900°C, ativar ventilador.
2. Se temperatura < 700°C, aumentar alimentação de coque.
3. Se tonelagem de carga for excessiva, reduzir alimentação.
4. Se nível de gases inertes estiver baixo, acionar válvulas de reposição.
5. Se posição de tremonhas/trens estiver desalinhada, alertar operador.

## Entrega
Os seguintes artefatos serão entregues:

- Pasta compactada com arquivos do ScadaBR.
- Códigos-fonte do web service, IHMs, servidor Modbus e banco de dados.
- Repositório GitHub documentado.