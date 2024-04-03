from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course, Enrollment
from .serializers import CourseSerializer, EnrollmentSerializer
from .services import CourseService, EnrollmentService

@api_view(['GET', 'POST'])
def course_list(request):
    if request.method == 'GET':
        courses = CourseService.get_courses()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def course_detail(request, pk):
    course = CourseService.get_course_by_id(pk)
    if not course:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)

@api_view(['GET'])
def filter_courses(request):
    instructor = request.query_params.get('instructor', None)
    price = request.query_params.get('price', None)
    duration = request.query_params.get('duration', None)
    courses = CourseService.filter_courses(instructor=instructor, price=price, duration=duration)
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

# @api_view(['POST'])
# def enroll_student(request):
#     serializer = EnrollmentSerializer(data=request.data)
#     if serializer.is_valid():
#         student_name = serializer.validated_data['student_name']
#         course_id = serializer.validated_data['course_id']
#         if not EnrollmentService.validate_enrollment(student_name, course_id):
#             return Response({'error': 'Invalid course ID'}, status=status.HTTP_400_BAD_REQUEST)
#         enrollment = EnrollmentService.enroll_student(student_name, course_id)
#         if enrollment:
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response({'error': 'Failed to enroll student'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def enroll_student(request):
    # Extract data from the request
    student_name = request.data.get('student_name')
    course_id = request.data.get('course_id')

    # Validate data
    if not student_name or not course_id:
        return Response({"error": "Both student_name and course_id are required"}, status=400)

    # Create enrollment
    try:
        enrollment = Enrollment.objects.create(student_name=student_name, course_id=course_id)
        serializer = EnrollmentSerializer(enrollment)
        return Response(serializer.data, status=201)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
