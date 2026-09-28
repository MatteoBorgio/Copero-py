from config import ROLES, LEAGUE_RATIO, FOOT


class Player:
    def __init__(
        self, role: str, foot: str, team: dict[str, str], start_overall: int
    ) -> None:
        if role not in ROLES.keys():
            raise ValueError("Role is not valid.")
        if foot not in FOOT:
            raise ValueError("Foot is not valid.")
        if start_overall < 30 or start_overall > 99:
            raise ValueError("Overall is not valid")

        self.__role = role
        self.__foot = foot
        self.__team = team
        self.__overall = start_overall

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, new_role: str) -> None:
        if new_role not in ROLES.keys():
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
