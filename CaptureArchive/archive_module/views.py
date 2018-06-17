from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from io import BytesIO
from mongoengine import *

connect( 'MY_MONGO_DB2', host='192.168.0.26', port=27017, username='', password='' )

class Challenge(Document):
    html = StringField()
    img = BinaryField()
    challengeText = StringField()
    rows = StringField()
    cols = StringField()

# Create your views here.
@api_view( ['POST',] )
def send_capture_content( request, format='json' ):
    request_data = request.data
    request_html = request_data['html']
    request_img_url = request_data['imgUrl']
    request_challenge_text = request_data['challengeText']
    request_rows = request_data['rows']
    request_cols = request_data['cols']
    #url = 'https://staticmemes.fjcdn.com/pictures/I+just+google+something+funny_6abee9_5716037.jpg'
    url_response = requests.get( request_img_url )
    im = BytesIO( url_response.content )
    # get the bytes
    im_byte_array = im.getvalue()
    #print(im_byte_array)
    #im = Image.open( BytesIO( url_response.content ) )
    #im.show()
    challenge = Challenge( html=request_html,
                            img=im_byte_array,
                            challengeText=request_challenge_text,
                            rows=str(request_rows),
                            cols=str(request_cols)).save()
    print("Saved to DB")
    """for challenge in Challenge.objects:
        print( challenge.html )"""
    return Response( { 'Message':'It worked!' } )
