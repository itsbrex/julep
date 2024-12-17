from uuid import UUID

import asyncpg
from beartype import beartype
from fastapi import HTTPException
from sqlglot import parse_one
from sqlglot.optimizer import optimize

from ...autogen.openapi_model import ResourceUpdatedResponse, UpdateUserRequest
from ...metrics.counters import increase_counter
from ..utils import partialclass, pg_query, rewrap_exceptions, wrap_in_class

# Define the raw SQL query outside the function
raw_query = """
UPDATE users
SET 
    name = $3,
    about = $4,
    metadata = $5
WHERE developer_id = $1 
AND user_id = $2
RETURNING *
"""

# Parse and optimize the query
query = parse_one(raw_query).sql(pretty=True)


@rewrap_exceptions(
    {
        asyncpg.ForeignKeyViolationError: partialclass(
            HTTPException,
            status_code=404,
            detail="The specified developer does not exist.",
        )
    }
)
@wrap_in_class(
    ResourceUpdatedResponse,
    one=True,
    transform=lambda d: {**d, "id": d["user_id"]},
)
@increase_counter("update_user")
@pg_query
@beartype
async def update_user(
    *, developer_id: UUID, user_id: UUID, data: UpdateUserRequest
) -> tuple[str, list]:
    """
    Constructs an optimized SQL query to update a user's details.
    Uses primary key for efficient update.

    Args:
        developer_id (UUID): The developer's UUID
        user_id (UUID): The user's UUID
        data (UpdateUserRequest): Updated user data

    Returns:
        tuple[str, list]: SQL query and parameters
    """
    params = [
        developer_id,
        user_id,
        data.name,
        data.about,
        data.metadata or {},
    ]

    return (
        query,
        params,
    )
