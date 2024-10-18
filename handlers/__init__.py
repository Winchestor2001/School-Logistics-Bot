from . import commands
from . import study_plan_handlers


routers_list = [
    commands.router,
    study_plan_handlers.router,
]

__all__ = [
    "routers_list",
]
