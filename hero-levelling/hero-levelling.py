# Função que retorna o nível do herói dependendo de quanto EXP possui
def check_hero_level():
  if hero_exp <= 1000:
    hero_level = ["Ferro", 1]
  elif hero_exp > 1000 and hero_exp <= 2000:
    hero_level = ["Bronze", 2]
  elif hero_exp > 2000 and hero_exp <= 5000:
    hero_level = ["Prata", 3]
  elif hero_exp > 6000 and hero_exp <= 7000:
    hero_level = ["Ouro", 4]
  elif hero_exp > 7000 and hero_exp <= 8000:
    hero_level = ["Platina", 5]
  elif hero_exp > 8000 and hero_exp <= 9000:
    hero_level = ["Ascendente", 6]
  elif hero_exp > 9000 and hero_exp <= 10000:
    hero_level = ["Imortal", 7]
  elif hero_exp > 10000:
    hero_level = ["Radiante", 8]
  return hero_level

# Função que printa as informações do herói no console
def print_hero_stats():
  print(f"O herói de nome {hero_name} está no nível de {hero_level[0]}", "⭐️" * hero_level[1])

# Função que pede e verifica o EXP
def verify_exp():
  hero_exp = -1
  while hero_exp < 0 or type(hero_exp) is not int:
    try:
      hero_exp = int(input("Digite o XP acumulado (valor inteiro positivo): "))
    except:
      print("Valor fornecido inválido, digite um número inteiro.")
  return hero_exp

hero_name = input("Digite o nome do herói: ")
hero_exp = verify_exp()
hero_level = check_hero_level()

print_hero_stats()