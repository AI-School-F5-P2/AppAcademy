from fastapi import APIRouter, Response, status
from controllers import inscriptions
from data.Models import Inscription
from data.Models import InscriptionDetail
from typing import List

router = APIRouter(prefix="/inscriptions", tags=["Inscriptions"])


@router.get(
    "/",
    summary="Get all inscriptions",
    response_description="All inscriptions in database shown",
    status_code=status.HTTP_200_OK,
)
async def get_all_inscriptions(response: Response):
    return await inscriptions.get_all_inscriptions(response)


@router.get(
    "/{id_inscriptions}",
    summary="Get a inscription by id",
    response_description="Search a inscription by id",
    status_code=status.HTTP_200_OK,
)
async def get_inscription(id_inscriptions: int, response: Response):
    return await inscriptions.get_inscription(id_inscriptions, response)


@router.get(
    "/student/{id_students}",
    summary="Get all inscriptions by student id",
    response_description="All inscriptions in database shown by student id",
    status_code=status.HTTP_200_OK,
)
async def get_inscription_by_id_student(id_students: str, response: Response):
    return await inscriptions.get_inscription_by_id_student(id_students, response)


@router.post(
    "/create/",
    summary="Create a new inscription",
    response_description="A new inscription will be created in database",
    status_code=status.HTTP_201_CREATED,
)
async def create_inscription(
    inscription: Inscription,
    inscriptions_detail: List[InscriptionDetail],
    response: Response,
):
    return await inscriptions.create_inscription(
        inscription, inscriptions_detail, response
    )