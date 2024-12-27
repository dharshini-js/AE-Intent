from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Employee,Admin
from .serializers import EmployeeSerializer,AdminSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/admin/', 
            'method': 'GET', 
            'description': 'Get admin details'
        },
        {
            'Endpoint': '/employees/', 
            'method': 'GET', 
            'description': 'List all employees or create a new employee'
        },
        {
            'Endpoint': '/employee/<id>/', 
            'method': 'GET', 
            'description': 'Retrieve details of a specific employee'
        },
        {
            'Endpoint': '/employee/delete/<id>/', 
            'method': 'DELETE', 
            'description': 'Delete an employee by Employee ID '
        },
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def getAdmin(request):
    if request.method == 'GET':
        admin = Admin.objects.all()
        serializer = AdminSerializer(admin, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Admin added successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            'status': False,
            'errors': serializer.errors,
            'message': 'Failed to add admin.'
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def getEmployee(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        emp_id = data.get('emp_id')
        password = data.get('password')

        admin = Admin.objects.filter(password=password).first()
        if not admin:
            return Response({
                'status': False,
                'message': 'Invalid admin password. Employee not added.'
            }, status=status.HTTP_401_UNAUTHORIZED)

        if Employee.objects.filter(emp_id=emp_id).exists():
            return Response({
                'status': False,
                'message': 'Employee ID already exists.'
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Employee added successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            'status': False,
            'errors': serializer.errors,
            'message': 'Failed to add employee.'
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getEmployeeById(request, pk):
    employee = Employee.objects.filter(emp_id=pk).first()
    if not employee:
        return Response({'detail': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteEmployee(request, pk):
    password = request.data.get('password', None)

    admin = Admin.objects.filter(password=password).first()
    if not admin:
        return Response({
            'status': False,
            'message': 'Invalid admin password. Employee not deleted.'
        }, status=status.HTTP_401_UNAUTHORIZED)

    employee = Employee.objects.filter(emp_id=pk).first()
    if not employee:
        return Response({
            'status': False,
            'message': 'Employee not found.'
        }, status=status.HTTP_404_NOT_FOUND)

    employee.delete()
    return Response({
        'status': True,
        'message': 'Employee deleted successfully.'
    }, status=status.HTTP_200_OK)
