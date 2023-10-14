# Calcula o placar atual
def set_scoreboard(victories, losses):
  return victories - losses

# Verifica o placar e fornece o ranqueamento adequada
def check_scoreboard(victories, losses):
  score = set_scoreboard(victories, losses)

  if score <= 10:
    rank = ["Ferro", 1]
  elif score > 10 and score <= 20:
    rank = ["Bronze", 2]
  elif score > 20 and score <= 50:
    rank = ["Prata", 3]
  elif score > 50 and score <= 80:
    rank = ["Ouro", 4]
  elif score > 80 and score <= 90:
    rank = ["Diamante", 5]
  elif score > 90 and score <= 100:
    rank = ["Lendário", 6]
  elif score > 100:
    rank = ["Imortal", 7]
  return rank

# Mostra o resultado no console
def print_result():
  print(f"O Herói tem o saldo de {score} e está no nível de {rank[0]}", "⭐️" * rank[1])

# Verifica se há problemas com os valores fornecidos
def verify_score(msg):
  score = -1
  while score < 0 or type(score) is not int:
    try:
      score = int(input(msg))
    except:
      print("Valor fornecido inválido, digite um número inteiro.")
  return score

victories = verify_score("Informe o número de vitórias: ")
losses = verify_score("Informe o número de derrotas: ")
score = set_scoreboard(victories, losses)
rank = check_scoreboard(victories, losses)

print_result()