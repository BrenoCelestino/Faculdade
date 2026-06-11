# ==========================================
# 1. FUNÇÕES (MÓDULOS)
# ==========================================

def formatar_palavra(palavra_secreta, letras_acertadas):
    """Apenas formata a string para a tela. Não toma decisões de jogo."""
    return " ".join([letra if letra in letras_acertadas else "_" for letra in palavra_secreta])

def verificar_vitoria(palavra_secreta, letras_acertadas):
    """
    Verifica a condição de vitória usando lógica de dados.
    Retorna True se TODAS as letras da palavra estiverem nos acertos.
    """
    # Lê-se: "É verdade que toda 'letra' na 'palavra_secreta' está nas 'letras_acertadas'?"
    return all(letra in letras_acertadas for letra in palavra_secreta)

# ==========================================
# 2. LOOP PRINCIPAL DO JOGO
# ==========================================

palavra_secreta = "GATO"
letras_acertadas = []
tentativas = 6

# O loop roda enquanto o jogador tiver vidas
while tentativas > 0:
    
    # 1. EXIBIR O ESTADO ATUAL (Interface)
    print("\n" + "="*20)
    print(f"Tentativas restantes: {tentativas}")
    print(f"Palavra: {formatar_palavra(palavra_secreta, letras_acertadas)}")
    
    # 2. RECEBER INPUT (Interação)
    chute = input("Digite uma letra: ").upper().strip()

    # 3. ATUALIZAR O ESTADO (Regras de Negócio)
    if chute in letras_acertadas:
        print("-> Você já tentou essa letra!")
        continue # Pula para o próximo ciclo sem descontar vida

    if chute in palavra_secreta:
        print("-> Boa! Você acertou uma letra.")
        letras_acertadas.append(chute)
    else:
        print("-> Errou!")
        tentativas -= 1

    # 4. CHECAR CONDIÇÕES DE FIM DE JOGO (Vitória/Derrota)
    # Aqui a checagem acontece de forma independente da tela
    if verificar_vitoria(palavra_secreta, letras_acertadas):
        print("\n" + "="*20)
        print(f"Palavra final: {formatar_palavra(palavra_secreta, letras_acertadas)}")
        print("🏆 PARABÉNS! VOCÊ VENCEU! 🏆")
        break # Encerra o loop e o jogo

# Se o loop terminar e as tentativas chegarem a 0, é Game Over.
if tentativas == 0:
    print("\n" + "="*20)
    print("💀 GAME OVER! 💀")
    print(f"A palavra correta era: {palavra_secreta}")