function alterarCor(id) {
  let element = document.getElementById(id);
  if (element) {
    let ligado = "rgb(30, 136, 229)"; // Azul Ligado
    let desligado = "rgb(100, 181, 246)"; // Azul Desligado

    let corAtual = element.style.fill;
    element.style.fill = corAtual === ligado ? desligado : ligado;
  }
}
