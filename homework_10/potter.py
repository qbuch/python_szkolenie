# Utwórz hierarchię klas (min 5 klas) bazując na informacji dot. zaklęć z sagi Harry Potter https://harrypotter.fandom.com/wiki/List_of_spells.
# Każde zaklęcie powinno mieć możliwość jego rzucenia i wyświetlenia opisu.

class Spell:
    def __init__(self, name, effect, description):
        self.name = name
        self.effect = effect
        self.description = description

    def cast_spell(self):
        print(f'I put a {self.name} spell on You!')

    def descritpion(self):
        print(f'{self.description}')

    def __str__(self):
        return f'{self.name} {self.effect} {self.description}'


class Crucio(Spell):
    def __init__(self, name, effect, description):
        super().__init__(name, effect, description)


if __name__ == '__main__':
    crucio = Crucio("crucio", 'Inflicts intense pain ', 'This curse does not physically harm the victim, but may in extreme cases drive them insane')
    crucio.cast_spell()
    crucio.description()
    crucio.effect()
