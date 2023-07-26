import json

from fuzzywuzzy import process
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from locations.data import data
from locations.models import Location
from locations.serializers import LocationSerializer

# # needed to make all states and local government lower case
# data = {k.lower(): {sub_k.lower(): sub_v for sub_k, sub_v in v.items()} for k, v in data.items()}

class LocationView(APIView):
    def get(self, request, *args, **kwargs):
        state = self.kwargs.get('state', None)
        local_govt = self.kwargs.get('local_govt', None)
        if state:
            # Convert the state and local_govt parameter to lower case
            state = state.lower()
            if local_govt:
                local_govt = local_govt.lower()
                # Use fuzzy matching to find the best match for the state and local government name
                best_state_match = process.extractOne(state, data.keys())
                best_local_govt_match = process.extractOne(local_govt, data[best_state_match[0]].keys())
                response_data = data.get(best_state_match[0], {}).get(best_local_govt_match[0], {})
            else:
                # Use fuzzy matching to find the best match for the state name
                best_state_match = process.extractOne(state, data.keys())
                response_data = data.get(best_state_match[0], {})
        else:
            response_data = data

        return Response(response_data)
    

# When using the database
# class LocationViewSet(viewsets.ModelViewSet):
#     queryset = Location.objects.all()
#     serializer_class = LocationSerializer
