# Simulação e Controle de uma Coqueria usando Modbus e IHMs

## Descrição do Projeto
Este projeto tem por objetivo implementar uma IHM básica, aos padrões ISA-101, para uma planta industrial de CDQ (Coke Dry Quenching).
Nele podemos encontrar os seguintes artefatos:

## Objetivos
- Monitorar e controlar temperatura, tonelagem, posição de tremonhas e trens, nível de gases inertes.
- Aplicar 5 regras de automação para ações como acionamento de ventiladores conforme temperatura.
- Simular os valores das variáveis via servidor Modbus.
- Criar um web service com API para integração e consumo de dados históricos.
- Desenvolver duas IHMs:
- ScadaBR para visualização estática e controle.
- Streamlit para visualização dinâmica e análises gráficas.

## Arquitetura

Cada um dos artefatos abaixo está dentro deste repositório e constituem compoenentes diferentes desse projeto.
Todos contam com um `Dockerfile` que permite empacota-los dentro de um container. 

### → [ihm_front](https://github.com/Batchuka/ifes-integracao-industrial/tree/main/ihm_front)
Projeto JavaScript, HTML e CSS que constituem o Front-End dessa aplicação. Para execução no vscode, é possível usar o LiveService.

### → [modbus_service](https://github.com/Batchuka/ifes-integracao-industrial/tree/main/modbus_service)
Projeto Python gerenciado pelo Poetry, que implementa um server modbus simulando o que seria a planta industrial do CDQ.
Basicamente com uma lógica que produz as variáveis definidas em aqui abaixo em `Variáveis`.

Para executa-lo no VSCODE, você pode usar o debugger `debugpy`.

### → [web_service](https://github.com/Batchuka/ifes-integracao-industrial/tree/main/web_service)
Projeto Python gerenciado pelo Poetry, que implementa um web service que integra ao server modbus.
Além disso, ele fornece uma API. Ao executar o projeto, você pode acessar `/docs` para o swagger da API.

Para executa-lo no VSCODE, você pode usar o debugger `debugpy`.
## Variáveis

1. Temperatura da Câmara de Resfriamento (°C) – Indica a temperatura interna onde o coque é resfriado.
2. Pressão do Vapor Gerado (bar) – Mede a pressão do vapor na caldeira.
3. Fluxo de Gases Inertes (m³/h) – Controla a circulação de gases 3 gases (A, B e C) para evitar oxidação do Coque.
4. Velocidade do Blower (RPM) – Regula a circulação dos gases na câmara de resfriamento.
5. Nível de Coque (Nível) – Mede a quantidade de coque carregado na Câmara de Resfriamento. Uma abstração para a tonelagem, havendo três níveis: 1, 2 e 3.

## Regras de Automação
1. Se a temperatura da câmara de resfriamento exceder 1100°C, aumentar o fluxo de gases inertes para evitar superaquecimento.
2. Se a pressão do vapor ultrapassar 20 bar, aumentar o nível de água de recirculação na caldeira para dissipar mais calor e evitar sobrepressão.
3. Se o fluxo de gases inertes cair abaixo de 1800 m³/h, aumentar a injeção de gás para evitar combustão indesejada.
4. Se a velocidade do blower cair abaixo de 1000 RPM, abrir um sinal para indicar obstrução dos filtros.
5. Medir 3 níveis: (1) baixo, não ligar blower; (2) médio, ligar um blower; (3) alto, ligar dois blowers.
