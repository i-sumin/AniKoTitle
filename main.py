import tvdb_v4_official
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')
tvdb = tvdb_v4_official.TVDB(API_KEY)

# 쇼 이름을 검색
show_name = "Frieren - Beyond Journey's End"  # 검색하려는 쇼 이름
search_results = tvdb.search(show_name)

# 검색 결과 출력
# print("Search results:", search_results)

# 검색 결과에서 한국어 제목 찾기
for result in search_results:
    if 'kor' in result['translations']:
        print("title:", result['translations']['kor'])