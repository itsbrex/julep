"""
The `agent` module within the `queries` package provides a comprehensive suite of SQL query functions for managing agents in the PostgreSQL database. This includes:

- Creating new agents
- Updating existing agents
- Retrieving details about specific agents
- Listing agents with filtering and pagination
- Deleting agents from the database

Each function in this module constructs and returns SQL queries along with their parameters for database operations.
"""

# ruff: noqa: F401, F403, F405

from .create_agent import create_agent
from .create_or_update_agent import create_or_update_agent_query
from .delete_agent import delete_agent_query
from .get_agent import get_agent_query
from .list_agents import list_agents_query
from .patch_agent import patch_agent_query
from .update_agent import update_agent_query
