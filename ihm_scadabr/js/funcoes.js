function carregar_datapoints() {

    setInterval(gerar_datapoints, 3000);


}

function gerar_datapoints() {

    var temperatura = Math.floor(Math.random() * 50) + 10;
    var luminosidade = Math.floor(Math.random() * 100);
    var umidade = Math.floor(Math.random() * 100);

    var temperaturaTag = document.getElementById('temperatura');    
    var luminosidadeTag = document.getElementById('luminosidade');
    var umidadeTag = document.getElementById('umidade');

    temperaturaTag.innerHTML = temperatura + "ºC";

    luminosidadeTag.innerHTML = luminosidade + "%";

    umidadeTag.innerHTML = umidade + "%";

    var ventiladorTag = document.getElementById('ventilador');

    if( temperatura >= 20 ) {
        ventiladorTag.src = "imagens/ventilador_on.gif"
    } else {
        ventiladorTag.src = "imagens/ventilador_off.png"
    }

    var lampadaTag = document.getElementById('lampada');

    if( luminosidade < 50 ) {
        lampadaTag.src = "imagens/lampada_on.jpeg"
    } else {
        lampadaTag.src = "imagens/lampada_off.jpeg"
    }

    var alarmeTag = document.getElementById('alarme');

    if( umidade >= 30 ) {
        alarmeTag.src = "imagens/alarme_off.png"
    } else {
        alarmeTag.src = "imagens/alarme_on.gif"
    }

}