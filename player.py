from config import ROLES, LEAGUE_RATIO, FOOT, START_AGE


class Player:
    def __init__(
        self, role: str, foot: str, team: dict[str, str], start_overall: int
    ) -> None:
        if role not in ROLES:
            raise ValueError("Role is not valid.")
        if foot not in FOOT:
            raise ValueError("Foot is not valid.")
        if start_overall < 30 or start_overall > 99:
            raise ValueError("Overall is not valid")

        self.__role = role
        self.__foot = foot
        self.__team = team
        self.__overall = start_overall
        self.__age = START_AGE
        self.__total_appearence = 0
        self.__total_goal = 0
        self.__total_assist = 0
        self.__career_average = 6.00

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, new_role: str) -> None:
        if new_role not in ROLES:
            raise ValueError("Role is not valid.")
        self.__role = new_role

    @property
    def foot(self) -> str:
        return self.__foot

    @property
    def team(self) -> dict[str, str]:
        return self.__team

    @team.setter
    def team(self, new_team: dict[str, str]) -> None:
        self.__team = new_team

    @property
    def overall(self) -> int:
        return self.__overall

    @overall.setter
    def overall(self, new_overall: int) -> None:
        if new_overall < 30 or new_overall > 99:
            raise ValueError("Overall is not valid")
        self.__overall = new_overall

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, new_age: int) -> None:
        if new_age < 16 or new_age > 45:
            raise ValueError("Age is not valid.")
        self.__age = new_age

    @property
    def total_appearence(self) -> int:
        return self.__total_appearence

    @total_appearence.setter
    def total_appearence(self, updated_appearence: int) -> None:
        if updated_appearence < 0 or updated_appearence < self.__total_appearence:
            raise ValueError("Updated appearence are not valid.")
        self.__total_appearence = updated_appearence

    @property
    def total_goal(self) -> int:
        return self.__total_goal

    @total_goal.setter
    def total_goal(self, updated_goal: int) -> None:
        if updated_goal < 0 or updated_goal < self.__total_goal:
            raise ValueError("Updated goal are not valid.")
        self.__total_goal = updated_goal

    @property
    def total_assist(self) -> int:
        return self.__total_assist

    @total_assist.setter
    def total_assist(self, updated_assist: int) -> None:
        if updated_assist < 0 or updated_assist < self.__total_assist:
            raise ValueError("Updated assists are not valid.")

    @property
    def career_average(self) -> float:
        return self.__career_average

    @career_average.setter
    def career_average(self, updated_average: float) -> None:
        if updated_average < 0:
            raise ValueError("Updated average is not valid.")
        self.__career_average = updated_average

    def standard_update(self, last_season_appearence: int, last_season_average: float):
        def multiplier(self, last_season_appearence: int, last_season_average: float):
            multiplier = 1
            if self.__age <= 20:
                multiplier += (
                    0.1 + (last_season_appearence * 0.01) + (last_season_average * 0.01)
                )
            elif self.__age > 20 and self.__age < 28:
                pass
