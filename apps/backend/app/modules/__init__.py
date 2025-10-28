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
<<<<<<< Updated upstream
from .users.router import medico_router as medico_router
from .users.router import paciente_router as paciente_router

=======
from .users.router import router_medic as medics_routers
from .users.router import router_fhir as router_fhir
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
    medico_router,
    paciente_router,
=======
    medics_routers,
    router_fhir,
>>>>>>> Stashed changes
]

__all__ = [
    "ROUTERS",
    "appointments_router", "clinic_router", "clinic_specialties_router",
    "locations_router", "medic_schedules_router", "medic_specialties_router",
    "notifications_router", "service_slots_router", "specialties_router",
<<<<<<< Updated upstream
    "users_router","medico_router","paciente_router",
=======
    "users_router","medics_routers","router_fhir"
>>>>>>> Stashed changes
]