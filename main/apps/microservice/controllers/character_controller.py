from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from main.libraries.di_container import Container
from main.libraries.tools.core.log_tool import LogTool

router = APIRouter()


@router.get(
    "/characters",
    tags=["Characters"],
    responses={
        200: {"description": "Success", "content": {"application/json": {}}},
        500: {
            "description": "Internal Server Error",
            "content": {"application/json": {}},
        },
    },
)
@inject
async def get_characters(logger: LogTool = Depends(Provide[Container.log_tool])):
    """
    Get all characters.

    Returns a JSON object with a list of characters.

    Returns:
        - 200: Success with the list of characters.
        - 500: Internal Server Error with the error message.
    """
    try:
        # Mocked characters data
        characters = [
            {"id": 1, "name": "Character 1"},
            {"id": 2, "name": "Character 2"},
            {"id": 3, "name": "Character 3"},
        ]

        logger.info("Characters information requested and returned successfully.")
        return characters
    except Exception as e:
        logger.error(f"Error while getting characters: {str(e)}")
        return {"error": str(e)}, 500


@router.post(
    "/characters",
    tags=["Characters"],
    responses={
        200: {"description": "Success", "content": {"application/json": {}}},
        500: {
            "description": "Internal Server Error",
            "content": {"application/json": {}},
        },
    },
)
@inject
async def create_character(logger: LogTool = Depends(Provide[Container.log_tool])):
    """
    Create a new character.

    Returns a JSON object with the created character.

    Returns:
        - 200: Success with the created character.
        - 500: Internal Server Error with the error message.
    """
    try:
        # Mocked character data
        character = {"id": 4, "name": "New Character"}

        logger.info("Character creation requested and returned successfully.")
        return character
    except Exception as e:
        logger.error(f"Error while creating character: {str(e)}")
        return {"error": str(e)}, 500


@router.put(
    "/characters/{character_id}",
    tags=["Characters"],
    responses={
        200: {"description": "Success", "content": {"application/json": {}}},
        500: {
            "description": "Internal Server Error",
            "content": {"application/json": {}},
        },
    },
)
@inject
async def update_character(
    character_id: int, logger: LogTool = Depends(Provide[Container.log_tool])
):
    """
    Update an existing character.

    Returns a JSON object with the updated character.

    Returns:
        - 200: Success with the updated character.
        - 500: Internal Server Error with the error message.
    """
    try:
        # Mocked character data
        character = {"id": character_id, "name": "Updated Character"}

        logger.info(
            f"Character update requested for ID {character_id} and returned successfully."
        )
        return character
    except Exception as e:
        logger.error(f"Error while updating character: {str(e)}")
        return {"error": str(e)}, 500


@router.delete(
    "/characters/{character_id}",
    tags=["Characters"],
    responses={
        200: {"description": "Success", "content": {"application/json": {}}},
        500: {
            "description": "Internal Server Error",
            "content": {"application/json": {}},
        },
    },
)
@inject
async def delete_character(
    character_id: int, logger: LogTool = Depends(Provide[Container.log_tool])
):
    """
    Delete an existing character.

    Returns a JSON object with the deleted character.

    Returns:
        - 200: Success with the deleted character.
        - 500: Internal Server Error with the error message.
    """
    try:
        # Mocked character data
        character = {"id": character_id, "name": "Deleted Character"}

        logger.info(
            f"Character deletion requested for ID {character_id} and returned successfully."
        )
        return character
    except Exception as e:
        logger.error(f"Error while deleting character: {str(e)}")
        return {"error": str(e)}, 500
