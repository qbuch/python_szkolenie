#Mario pyramid

while True:
    height = int(input("How high should the pyramid be?: "))
    if height >= 1 and height <=8:
        break

for num in range(height):
    print(" " * (height - num) + "#")

#nie wiem jak sie pozbyc pierwszej linii ktora wyswietal tylko spacje

# floor = int(input("Podaj liczbe pieter: "))
# for i in range(0, floor):
#     for i in range(0, i + 1):
#         print(end="#")
#     print()