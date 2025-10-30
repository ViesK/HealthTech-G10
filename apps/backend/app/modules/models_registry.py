# Importa SOLO modelos (sin routers, sin services)
from app.modules.users.model import UsersModel
from app.modules.clinic.model import ClinicModel
from app.modules.appointments.model import Appointment
from app.modules.notifications.model import Notification
from app.modules.medic_schedules.model import Medic_SchedulesModel
from app.modules.specialties.model import Specialty
from app.modules.service_slots.model import ServiceSlot
from app.modules.locations.model import Location
from app.modules.clinic_specialties.model import ClinicSpecialty
from app.modules.medic_specialties.model import MedicSpecialty

__all__ = [
    "UsersModel", "ClinicModel", "Appointment", "Notification",
    "Medic_SchedulesModel", "Specialty", "ServiceSlot", "Location",
    "ClinicSpecialty", "MedicSpecialty",
]
