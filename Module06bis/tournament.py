from ex3.factories import CreatureFactory, FlameFactory, TransformCreatureFactory
from ex4.strategies import BattleStrategy, NormalStrategy, AggressiveStrategy, InvalidStrategyError


def run_tournament(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            print("* Battle *")
            fac1, strat1 = opponents[i]
            fac2, strat2 = opponents[j]

            c1 = fac1.create_base()
            c2 = fac2.create_base()

            print(c1.describe())
            print("VS.")
            print(c2.describe())
            print("now fight!")

            try:
                strat1.act(c1)
                strat2.act(c2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    flame_fac = FlameFactory()
    trans_fac = TransformCreatureFactory()
    
    norm_strat = NormalStrategy()
    agg_strat = AggressiveStrategy()

    print("Tournament 0 (basic)")
    print("[(Flameling+Normal), (Shiftling+Aggressive)]")
    run_tournament([(flame_fac, norm_strat), (trans_fac, agg_strat)])

    print("\nTournament 1 (error)")
    print("[(Shiftling+Aggressive), (Flameling+Aggressive)]")
    run_tournament([(trans_fac, agg_strat), (flame_fac, agg_strat)])


if __name__ == "__main__":
    main()