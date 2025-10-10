from .appointments.router import router as appointments_router
from .clinic.router import router as clinic_router
from .clinic_specialties.router import router as clinic_specialties_router
from .locations.router import router as locations_router
from .medic_schedules.router import router as medic_schedules_router
from .medic_specialties.router import router as medic_specialties_router
from .notifications.router import router as notifications_router
from .service_slots.router import router as service_slots_router
from .specialties.router import router as specialties_router
from .users.router import router as users_router

ROUTERS = [
    appointments_router,
    clinic_router,
    clinic_specialties_router,
    locations_router,
    medic_schedules_router,
    medic_specialties_router,
    notifications_router,
    service_slots_router,
    specialties_router,
    users_router,
]

__all__ = [
    "ROUTERS",
    "appointments_router", "clinic_router", "clinic_specialties_router",
    "locations_router", "medic_schedules_router", "medic_specialties_router",
    "notifications_router", "service_slots_router", "specialties_router",
    "users_router",
]
