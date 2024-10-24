print("Високосний" if (lambda y: not y % 4 and (y % 100 != 0 or y % 400 == 0))(int(input("Введіть рік: "))) else "Не високосний")
