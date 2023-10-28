from catalog.models import SubjectStudentModel
from general.models import SubjectModel, PensumSubjectModel


def is_subject_available_handler(subject, user):
    subject = SubjectStudentModel.objects.get(subject=subject, student__user=user).subject

    prerequisite = PensumSubjectModel.objects.get(subject=subject).prerequisites
    if prerequisite:
        if not SubjectStudentModel.objects.get(subject=prerequisite, student__user=user).status == 'approved':
            return True

    return False
