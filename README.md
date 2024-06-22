Hardware/Software Environment
Processor : RaspberryPi3, 4
Camera : Raspberry Pi Camera(B) Rev 2.0
Language : Python
Library : OpenCV, Google Client Library

Flow
구글 드라이버를 사용하기 위해 사용자 동의가 필요하다.
프로그램에서 OAuth 동의서를 사용자에게 요청하고 사용자가 동의하게 되면 프로그램에게 동의서(동의 정보)를 전달하게 된다. 프로그램은 동의서를 구글에게 전달해 API 사용을 허가받게 되고, 그 후에 구글 API를 사용할 수 있게 된다.
추가 자세한 내용은 Google Cloud Create 부분에서 설명

Google Cloud Create
플리케이션과 동의 화면, API를 관리하는 프로젝트를 생성한다.
자세한 설명은 유튜브 설명을 따라 하면 된다.(1, 2편으로 나눠져 있다.)
중간에 json 파일을 다운로드하는 과정이 있는데 잘 보관하고 있어야 한다.(접속, 사용에 필요한 키)
이 json 파일의 파일명을 token.json으로 변경하는 게 아래 실습 코드를 사용하는 데 도움이 된다.
1편 : https://www.youtube.com/watch?v=A05rjn6x4vY
2편 : https://www.youtube.com/watch?v=1mFOa8OsYbQ

Python을 활용하여 Google Driver API 사용하기
우선 Python으로 사용하려면 Google Client Library 설치해야 한다.
Install_pack.sh를 실행하여 각종 패키지와 Google API, OpenCV 라이브러리를 설치한다.

Conclusion
이번 포스팅에서는 Python을 이용하여 Google 드라이브에 접속하고 업로드하는 부분을 다루었고, API 사용에 전체적인 구조를 알 수 있었다.또한 라즈베리파이 3, 4모델 둘 다 테스트해 본 결과 두 모델 모두 정상적으로 동작하는 것을 확인하였다.
다음 실험에서는 업로드 과정에서 Google Drive 상에 현재 시간으로 폴더를 생성한 후 그 폴더에 데이터를 저장하고, 반대로 Download 하여 이미지 데이터를 처리하는 부분을 실험할 예정이다.
