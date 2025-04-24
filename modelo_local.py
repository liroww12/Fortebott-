def responder_pergunta(pergunta):
    if "temperatura" in pergunta.lower():
        return "A temperatura ideal para câmaras frias de congelados fica entre -18°C e -25°C."
    elif "compressor" in pergunta.lower():
        return "O compressor é o coração do sistema de refrigeração, responsável pela compressão do gás refrigerante."
    else:
        return "Ainda estou aprendendo sobre isso. Pode reformular ou perguntar de outra forma?"
