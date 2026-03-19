"""Pydantic schemas for resume scoring endpoints."""

from pydantic import BaseModel


class ScoreRequest(BaseModel):
    """Request body for creating a resume-job score."""

    resume_id: str
    job_id: str


class ScoreResult(BaseModel):
    """Response model for a resume-job match score."""

    score_id: str
    resume_id: str
    job_id: str
    score: int
    ai_score: int
    match_reasons: str
    red_flags: dict[str, list[str]]
    website: str
    label: str
    emoji: str
    color: str
    cached: bool
    created_at: str
