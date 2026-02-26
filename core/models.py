from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class CandidateProfile:
    full_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    experience_years: Optional[str] = None
    desired_position: Optional[str] = None
    location: Optional[str] = None
    tech_stack: List[str] = field(default_factory=list)
    tech_questions: List[str] = field(default_factory=list)
    answers: dict = field(default_factory=dict)

    def is_complete(self) -> bool:
        # Check if basic info is gathered before technical screening
        required = [self.full_name, self.email, self.experience_years, self.tech_stack]
        return all(required)