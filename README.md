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

## Variáveis

1. Temperatura da Câmara de Resfriamento (°C) – Indica a temperatura interna onde o coque é resfriado.
2. Pressão do Vapor Gerado (bar) – Mede a pressão do vapor na caldeira.
3. Fluxo de Gases Inertes (m³/h) – Controla a circulação de gases para evitar oxidação.
4. Velocidade do Blower (RPM) – Regula a circulação dos gases na câmara de resfriamento.
5. Temperatura do Coque Resfriado (°C) – Mede a temperatura do coque ao sair do processo.

## Regras de Automação
1. Se a temperatura da câmara de resfriamento exceder 1100°C, aumentar o fluxo de gases inertes para evitar superaquecimento;
2. Se a pressão do vapor ultrapassar 20 bar, aumentar o nível de água de recirculação na caldeira para dissipar mais calor e evitar sobrepressão;
3. Se a temperatura do coque resfriado estiver acima de 250°C, aumentar a velocidade do blower para garantir resfriamento adequado;
4. Se o fluxo de gases inertes cair abaixo de 1800 m³/h, ativar um alarme e aumentar a injeção de gás para evitar combustão indesejada;
5. Se a velocidade do blower cair abaixo de 1000 RPM, abrir um sinal para indicar obstrução dos filtros;

## Entrega
Os seguintes artefatos serão entregues:

- Pasta compactada com arquivos do ScadaBR.
- Códigos-fonte do web service, IHMs, servidor Modbus e banco de dados.
- Repositório GitHub documentado.
