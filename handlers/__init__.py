from . import commands
from . import study_plan_handlers
from . import tariff_plan_handlers
from . import testimonial_handlers
from . import teacher_handlers
from . import faq_handlers


routers_list = [
    commands.router,
    study_plan_handlers.router,
    tariff_plan_handlers.router,
    testimonial_handlers.router,
    teacher_handlers.router,
    faq_handlers.router,
]

__all__ = [
    "routers_list",
]
