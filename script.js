async function enviarMensagem() {
    const input = document.getElementById("mensagem")
    const chat = document.getElementById("chat")
    const mensagem = input.value
    chat.innerHTML += `<div><strong>Você:</strong> ${mensagem}</div>`
    input.value = ""

    const resposta = await fetch("http://localhost:8000/perguntar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mensagem })
    }).then(res => res.json())

    chat.innerHTML += `<div><strong>Fortebott:</strong> ${resposta.resposta}</div>`
    chat.scrollTop = chat.scrollHeight
}
