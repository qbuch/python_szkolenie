#Mario pyramid

while True:
    height = int(input("How high should the pyramid be?: "))
    if height >= 1 and height <=8:
        break

for num in range(height):
    print(" " * (height - num) + "#" * (num - 1)

#nie wiem jak sie pozbyc pierwszej linii ktora wyswietal tylko spacje