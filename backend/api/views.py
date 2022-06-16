from __future__ import division
from select import select
from rest_framework.response import Response
from rest_framework.decorators import api_view
from backend.models import *
from .serializers import *

@api_view(['GET'])
def getPosition(request):
    positions = Position.objects.all()
    serializer = PositionSerializer(positions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDivision(request):
    divisions = Division.objects.all()
    serializer = DivisionSerializer(divisions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSection(request):
    sections = Section.objects.all()
    serializer = SectionSerializer(sections, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def employeeDetail(request):
    employee_detail_join = AuthUser.objects.all().extra(
        select={'firstname': 'auth_user.first_name','lastname': 'auth_user.last_name','username':'auth_user.username'
        ,'contact_number':'tbl_employee_personalinfo.mobile_no','id_number':'tbl_employee_user_details.id_number'},
        tables=['tbl_employee_personalinfo','tbl_employee_user_details'],
        where=['auth_user.id = tbl_employee_personalinfo.auth_user_id', 'tbl_employee_personalinfo.id = tbl_employee_user_details.id']
        )
    
    
    return Response({'data': list(employee_detail_join.values('firstname','lastname','id_number','contact_number'))}) 