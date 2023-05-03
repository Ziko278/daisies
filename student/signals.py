from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from student.models import StudentsModel, StudentAcademicRecordModel
from school_setting.models import SchoolAcademicInfoModel


@receiver(post_save, sender=StudentsModel)
def create_academic_record(sender, instance, created, **kwargs):
    if created:
        student = instance
        student_class = instance.student_class
        academic_info = SchoolAcademicInfoModel.objects.first()
        session = academic_info.session
        term = academic_info.term
        academic_record = {
            session.session: {
                academic_info.term: student_class.id
            }
        }

        student_record = StudentAcademicRecordModel.objects.create(student=student, entry_class=student_class,
                                                                   current_class=student_class,
                                                                   previous_classes=academic_record)
        student_record.save()

