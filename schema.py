from pydantic import BaseModel, Field
from typing import List, Optional

class CompanyDetails(BaseModel):
    company_name: str = Field(..., description="Official name of the company")
    company_type: str = Field(..., description="e.g. MNC, Startup, PSU, Consulting")
    company_turnover: Optional[str] = Field(None, description="Annual revenue or turnover if mentioned")
    company_address: Optional[str] = Field(None, description="Headquarters or office address")
    
    role_title: str = Field(..., description="Specific job or internship title")
    role_type: str = Field(..., description="e.g. Internship (2 months), 6 Months, or Full-Time")
    location: str = Field(..., description="Work location (e.g., Bangalore, Remote, On-site)")
    
    eligible_branches: List[str] = Field(..., description="List of departments like CSE, MnC, EE, etc.")
    min_cgpa: Optional[float] = Field(None, description="Minimum CGPA requirement")
    
    ctc_lpa: Optional[str] = Field(None, description="CTC for full-time in Lakhs Per Annum")
    stipend_monthly: Optional[str] = Field(None, description="Monthly stipend for interns")
    
    selection_process: List[str] = Field(..., description="Steps like Online Test, Interview, GD")
    deadline: Optional[str] = Field(None, description="Last date to apply")
    additional_info: Optional[str] = Field(None, description="Any other important perks or notes")