function carregar_datapoints() {

    setInterval(gerar_datapoints, 3000);

}

function gerar_datapoints() {

    var temperatura = (Math.random() * (60 - 10) + 10).toFixed(1);
    var luminosidade = (Math.random() * 100).toFixed(1);
    var umidade = (Math.random() * 100).toFixed(1);

    var temperaturaTag = document.getElementById('temperatura');    
    var luminosidadeTag = document.getElementById('luminosidade');
    var umidadeTag = document.getElementById('umidade');

    temperaturaTag.innerHTML = temperatura + "ºC";

    luminosidadeTag.innerHTML = luminosidade + "%";

    umidadeTag.innerHTML = umidade + "%";

    var ventiladorTag = document.getElementById('ventilador');
    var statusVentilador = document.getElementById('status_ventilador');

    if( temperatura >= 20 ) {
        ventiladorTag.src = "imagens/ventiladorOn.gif";
        statusVentilador.innerHTML = 'Ligado';
    } else {
        ventiladorTag.src = "imagens/VentiladorOff.png";
        statusVentilador.innerHTML = 'Desligado';
    }

    var lampadaTag = document.getElementById('lampada');
    var lampadaStatusTag = document.getElementById('status_lampadas');

    if( luminosidade > 50 ) {
        lampadaTag.src = "imagens/LampadaOff.gif";
        lampadaStatusTag.innerHTML = 'Desligadas';
    } else {
        lampadaTag.src = "imagens/LampadaOn.gif";
        lampadaStatusTag.innerHTML = 'Ligadas';
    }

    var alarmeTag = document.getElementById('alarme');
    var alarmeStatusTag = document.getElementById('alarme_status');
    
    const apito = new Audio('alarme.mp3');
    
    apito.volume = 0.5;

    if( umidade >= 30 ) {
        alarmeTag.src = "imagens/alarme_off.png";
        alarmeStatusTag.innerHTML = "Desligado";
        apito.pause();
    } else {
        alarmeTag.src = "imagens/alarme_on.gif"
        alarmeStatusTag.innerHTML = "Ligado";    
        apito.play();
    }

}