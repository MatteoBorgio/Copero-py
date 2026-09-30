from config import COUNTRIES


class Team:
    def __init__(
        self, name: str, league: str, country: str, tier: int, rating: int
    ) -> None:
        self.__name = name
        self.__league = league
        if country not in COUNTRIES:
            raise Exception("Not a valid country.")
        self.__country = country
        if tier not in [1, 2]:
            raise ValueError("Not a valid tier.")
        self.__tier = tier
        if rating < 0 or rating > 99:
            raise ValueError("Not a valid rating.")
        self.__rating = rating

    @property
    def name(self) -> str:
        return self.__name

    @property
    def league(self) -> str:
        return self.__league

    @league.setter
    def league(self, new_league: str) -> None:
        self.__league = new_league

    @property
    def country(self) -> str:
        return self.__country

    @property
    def rating(self) -> int:
        return self.__rating

    @rating.setter
    def rating(self, new_rating: int) -> None:
        if new_rating < 0 or new_rating > 99:
            raise ValueError("Not a valid rating.")
        self.__rating = new_rating
