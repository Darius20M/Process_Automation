from model_utils import Choices


VERIFICATION_STATUS = Choices(
    ('pending', 'Pending'),
    ('denied', 'Denied'),
    ('accepted', 'Accepted'),
)


REQUEST_STATUS = Choices(
    ('progress', 'Progress'),
    ('pending', 'Pending'),
    ('denied', 'Denied'),
    ('approved', 'Approved'),
)
