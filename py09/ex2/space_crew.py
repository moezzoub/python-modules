from typing import Self
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from enum import Enum

class RankCrew(str, Enum):
    CADET = 'cadet'
    OFFICER = 'officer'
    LIEUTENAT = 'lieutenant'
    CAPTAIN = 'captain'
    COMMANDER = 'commander'

class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: RankCrew
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    s_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(ge=1, le=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_rules(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError('mission_id must start with "M"')

        if not any(member.rank in {RankCrew.COMMANDER, RankCrew.CAPTAIN} for member in self.crew):
            raise ValueError('mission must have at least one Commander or Captain')

        if self.duration_days > 365:
            experienced = sum(1 for member in self.crew if member.years_experience >= 5)
            if experienced < len(self.crew) / 2:
                raise ValueError('long missions need at least 50% experienced crew')

        if any(not member.is_active for member in self.crew):
            raise ValueError('all crew members must be active')

        return self

def Info_Mission(members: CrewMember, mission: SpaceMission):
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {mission.crew}")
    print("Crew members:")
    print(f"- {members.name} ({members.rank.value} - Mission Command)")
    print(f"- {members.name} ({members.rank.value} - Navigation)")
    print(f"- {members.name} ({members.rank.value} - Engineering)")
    print()

def main():

