from model_utils import Choices


VERIFICATION_STATUS = Choices(
    ('pending', 'Pending'),
    ('denied', 'Denied'),
    ('accepted', 'Accepted'),
)
DIAS_SEMANA = (
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
    )

REQUEST_STATUS = Choices(
    ('progress', 'Progress'),
    ('pending', 'Pending'),
    ('denied', 'Denied'),
    ('approved', 'Approved'),
)
