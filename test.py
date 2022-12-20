from main import

player = make_hero(
    name="Вася Питонов",
    inventory=["зелье"],
    hp_now=1000,
    money=10000
)

game = True
while game:
    visit_hub(player)
