# AniKoTitle
tvdb API를 이용하여 다국어로 작성된 애니메이션 이름을 한국어 이름으로 출력해줍니다.


## How to Use
env 파일에 tvdb의 API를 작성합니다.
- API 정보: https://thetvdb.com/api-information#general

<h3>.env 파일은 main.py와 같은 디렉터리에 생성합니다.</h3>
`.env -> API_KEY='API KEY 입력'`


<h3>종속성 패키지를 설치합니다.</h3>
`pip install -r requirements.txt`

`show_name`에 작품의 이름을 작성합니다.

ex) "Frieren - Beyond Journey's End"

결과) `title: 장송의 프리렌`
