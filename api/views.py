from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},

    ]
    return Response(routes,)
# our decorator:api view
@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getProjects(request):
#   print('USER:',request.user)
    projects = Project.objects.all()
#here context doesnt work we have to serialize our data by creating a serializer 
# class that takes projects queryset and turn it into json data
    serializer = ProjectSerializer(projects,many=True)     
    return Response(serializer.data)

@api_view(['GET'])
def getProject(request,pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project,many=False)     
    return Response(serializer.data)









##the view code just with api before we work with Rest framework :

# from django.http import JsonResponse

# def getRoutes(request):
#     routes = [
#         {'GET': '/api/projects'},
#         {'GET': '/api/projects/id'},
#         {'POST': '/api/projects/id/vote'},

#         {'POST': '/api/users/token'},
#         {'POST': '/api/users/token/refresh'},

#     ]
#     return JsonResponse(routes,safe=False)  
