from fastapi import APIRouter, Depends, Query, status, HTTPException

router = APIRouter(prefix="/news", tags=["news"])