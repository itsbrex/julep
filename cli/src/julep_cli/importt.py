import datetime
import hashlib
from pathlib import Path

import typer
from julep.types.agent import Agent
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.text import Text

from .app import console, error_console, import_app, local_tz
from .models import LockedEntity
from .utils import (
    add_agent_to_julep_yaml,
    add_entity_to_lock_file,
    get_entity_from_lock_file,
    get_julep_client,
    update_existing_entity_in_lock_file,
    update_yaml_for_existing_entity,
)


@import_app.command()
def agent(
    id: str = typer.Option(..., "--id", "-i", help="ID of the agent to import"),
    source: Path = typer.Option(
        Path.cwd(),
        "--source",
        "-s",
        help="Path to the source directory. Defaults to current working directory",
    ),
    output: Path = typer.Option(
        None,
        "--output",
        "-o",
        help="Path to save the imported agent. Defaults to <project_dir>/src/agents",
    ),
    yes: bool = typer.Option(False, "--yes", "-y", help="Skip confirmation prompt"),
):
    """
    Import an agent from the Julep platform.
    """

    output = output or source / "src/agents"

    if not (source / "julep-lock.json").exists():
        error_console.print(
            Text(
                "Error: 'julep-lock.json' not found in the source directory. Please run 'julep sync' to sync your project and create a lock file.",
                style="bold red",
            )
        )
        raise typer.Exit(1)

    client = get_julep_client()

    # Importing an existing agent
    if locked_agent := get_entity_from_lock_file(type="agent", id=id, project_dir=source):
        console.print(Text(f"Agent '{id}' already exists in the lock file", style="bold yellow"), highlight=True)
        confirm = typer.confirm(
            f"Do you want to overwrite the existing agent in the lock file and {locked_agent.path}?"
        )

        if not confirm:
            console.print(Text("Operation cancelled", style="bold red"), highlight=True)
            raise typer.Exit(1)

        console.print(Text("Overwriting existing agent...", style="bold blue"), highlight=True)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
            console=console,
        ) as progress:
            try:
                fetch_task = progress.add_task("Fetching agent from remote...", start=False)
                progress.start_task(fetch_task)
                remote_agent: Agent = client.agents.get(agent_id=id)
            except Exception as e:
                error_console.print(
                    Text(
                        f"Error fetching agent from remote: {e}",
                        style="bold red",
                    ),
                    highlight=True,
                )
                raise typer.Exit(1)

        # Create a table to display agent data
        table = Table(title="Agent Data")
        table.add_column("Field", style="cyan", no_wrap=True)
        table.add_column("Value", style="magenta")

        # Populate the table with agent data
        for key, value in remote_agent.model_dump().items():
            table.add_row(key, str(value))

        console.print(table, highlight=True)

        agent_yaml_path = source / locked_agent.path

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
            console=console,
        ) as progress:
            try:
                update_task = progress.add_task(
                    f"Updating agent in '{agent_yaml_path}'...", start=False
                )
                progress.start_task(update_task)
                update_yaml_for_existing_entity(
                    agent_yaml_path,
                    remote_agent.model_dump(exclude={"id", "created_at", "updated_at"}),
                )
            except Exception as e:
                error_console.print(
                    Text(
                        f"Error updating agent in '{agent_yaml_path}': {e}",
                        style="bold red",
                    ),
                    highlight=True,
                )
                raise typer.Exit(1)

        console.print(Text("Updated successfully.", style="bold green"), highlight=True)

        console.print(
            Text(f"Updating agent '{id}' in lock file...", style="bold blue"),
            highlight=True,
        )
        update_existing_entity_in_lock_file(
            type="agent",
            new_entity=LockedEntity(
                path=str(agent_yaml_path.relative_to(source)),
                id=id,
                last_synced=datetime.datetime.now(tz=local_tz).isoformat(
                    timespec="milliseconds"
                ),
                revision_hash=hashlib.sha256(
                    remote_agent.model_dump_json().encode()
                ).hexdigest(),
            ),
            project_dir=source,
        )

        console.print(
            Text(
                f"Agent '{id}' imported successfully to '{agent_yaml_path}'",
                style="bold green",
            ),
            highlight=True,
        )

        return

    # Importing a new agent (doesn't exist in lock file)
    if not yes:
        confirm = typer.confirm(f"Are you sure you want to import agent '{id}' to '{output}'?")
        if not confirm:
            console.print(Text("Operation cancelled", style="bold red"), highlight=True)
            raise typer.Exit

    try:
        client = get_julep_client()

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
            console=console,
        ) as progress:
            try:
                fetch_task = progress.add_task("Fetching agent from remote...", start=False)
                progress.start_task(fetch_task)
                remote_agent: Agent = client.agents.get(agent_id=id)
            except Exception as e:
                error_console.print(
                    Text(f"Error fetching agent from remote: {e}", style="bold red")
                )
                raise typer.Exit(1)

        # Create a table to display agent data
        table = Table(title="Agent Data")
        table.add_column("Field", style="cyan", no_wrap=True)
        table.add_column("Value", style="magenta")

        # Populate the table with agent data
        for key, value in remote_agent.model_dump().items():
            table.add_row(key, str(value))

        console.print(table, highlight=True)

        agent_name = remote_agent.name.lower().replace(" ", "_")

        agent_yaml_path: Path = output / f"{agent_name}.yaml"
        typer.echo(f"Adding agent '{remote_agent.name}' to '{agent_yaml_path}'...")
        update_yaml_for_existing_entity(
            agent_yaml_path, remote_agent.model_dump(exclude={"id", "created_at", "updated_at"})
        )

        typer.echo(f"Agent '{id}' imported successfully to '{agent_yaml_path}'")

        add_agent_to_julep_yaml(
            source,
            {
                "definition": str(agent_yaml_path.relative_to(source)),
            },
        )

        typer.echo(f"Adding agent '{id}' to lock file...")
        add_entity_to_lock_file(
            type="agent",
            new_entity=LockedEntity(
                path=str(agent_yaml_path.relative_to(source)),
                id=remote_agent.id,
                last_synced=datetime.datetime.now(tz=local_tz).isoformat(
                    timespec="milliseconds"
                ),
                revision_hash=hashlib.sha256(
                    remote_agent.model_dump_json().encode()
                ).hexdigest(),
            ),
            project_dir=source,
        )

        console.print(
            Text(
                f"Agent '{id}' imported successfully to '{agent_yaml_path}' and added to lock file",
                style="bold green",
            ),
            highlight=True,
        )

    except Exception as e:
        error_console.print(
            Text(f"Error importing agent: {e}", style="bold red"),
            highlight=True,
        )
        raise typer.Exit(1)
