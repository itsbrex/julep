from typing import Literal
from uuid import UUID

from beartype import beartype
from sqlglot import parse_one
import ast

from ...autogen.openapi_model import Doc
from ..utils import pg_query, wrap_in_class

doc_query = parse_one("""
SELECT d.*
FROM docs d
LEFT JOIN doc_owners doc_own ON d.developer_id = doc_own.developer_id AND d.doc_id = doc_own.doc_id
WHERE d.developer_id = $1
  AND d.doc_id = $2
  AND (
    ($3::text IS NULL AND $4::uuid IS NULL)
    OR (doc_own.owner_type = $3 AND doc_own.owner_id = $4)
  )
LIMIT 1;
""").sql(pretty=True)


@wrap_in_class(
    Doc,
    one=True,
    transform=lambda d: {
        **d,
        "id": d["doc_id"],
        "content": ast.literal_eval(d["content"])[0] if len(ast.literal_eval(d["content"])) == 1 else ast.literal_eval(d["content"]),
        # "embeddings": d["embeddings"],
    },
)
@pg_query
@beartype
async def get_doc(
    *,
    developer_id: UUID,
    doc_id: UUID,
    owner_type: Literal["user", "agent"] | None = None,
    owner_id: UUID | None = None,
) -> tuple[str, list]:
    """
    Fetch a single doc, optionally constrained to a given owner.
    """
    return (
        doc_query,
        [developer_id, doc_id, owner_type, owner_id],
    )
