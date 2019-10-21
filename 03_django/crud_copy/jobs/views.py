from django.shortcuts import render
from .models import Job
from IPython import embed
from faker import Faker
import requests
from pprint import pprint
# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')

def past_life(request):
    name = request.POST.get('name')
    person = Job.objects.filter(name=name).first()

    if person:
        past_job = person.past_job

    else:
        fake = Faker('ko-KR')
        past_job = fake.jobs()
        past = Job(name=name, past_job=past_job)


    #GIPHY
    GIPHY_API_KEY = config('GIPHY_API_KEY')

    url = f'http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q{past_job}=&limit=10&lang=ko'

    data = requests.get(url).json()
    try:
        image = data.get('data')[0].get('images').get('original').get('url')
    except IndexError:
        image = None


    #naver image
    #1. 요청 헤더 정보 준비
    NAVER_ID = config('NAVER_ID')
    NAVER_SECRET = config('NAVER_SECRET')

    headers = {
        'X-naver-Client-Id':NAVER_ID,
        'X-naver-Client-Secret':NAVER_SECRET,
    }

    #2. 요청  URL 준비
    naver_url = f'https://openapi.naver.com/v1/search/image?query={past_job}&filter=medium&display=1'

    #3. 실제 요청 보내기
    requests.get(naver_url, headers=headers).json()
    pprint(naver_data)
    #4. 
    naver_image = naver_data.get('items')[0].get('link')

    context = {
        'name' : name,
        'person' : person,
        'image' : image,
        'naver_image': naver_image,
    }
    return render(request, 'jobs/past_job.html', context)