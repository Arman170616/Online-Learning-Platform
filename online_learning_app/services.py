from .models import Course, Enrollment

class CourseService:
    @staticmethod
    def get_courses():
        return Course.objects.all()

    @staticmethod
    def create_course(title, description, instructor, duration, price):
        return Course.objects.create(title=title, description=description, instructor=instructor, duration=duration, price=price)

    @staticmethod
    def get_course_by_id(course_id):
        return Course.objects.filter(pk=course_id).first()

    @staticmethod
    def filter_courses(instructor=None, price=None, duration=None):
        courses = Course.objects.all()
        if instructor:
            courses = courses.filter(instructor=instructor)
        if price:
            courses = courses.filter(price=price)
        if duration:
            courses = courses.filter(duration=duration)
        return courses

class EnrollmentService:
    @staticmethod
    def enroll_student(student_name, course_id):
        course = CourseService.get_course_by_id(course_id)
        if not course:
            return None
        return Enrollment.objects.create(student_name=student_name, course=course)

    @staticmethod
    def validate_enrollment(student_name, course_id):
        course = CourseService.get_course_by_id(course_id)
        if not course:
            return False
        return True
