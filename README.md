[프로젝트 이름: Flask REST Inventory Manager]
Sphinx와 Flasgger를 활용한 전문적인 파이썬 API 문서화 및 관리 시스템

2. Visual Demonstration

3. Motivation & Problem
   많은 백엔드 프로젝트에서 개발자와 사용자 간의 소통 부재로 인해 API 활용에 어려움을 겪습니다.

Problem: 문서화되지 않은 API는 유지보수가 불가능하며, 테스트가 어렵습니다.

Goal: 1. 코드 주석만으로 **자동화된 기술 문서(Sphinx)**를 구축합니다. 2. 사용자에게 인터랙티브한 **테스트 환경(Swagger UI)**을 제공합니다. 3. RESTful한 5개의 핵심 기능을 구현하여 실제 서비스 가능한 구조를 학습합니다.

4. Tech Stack & Rationale
   Python / Flask: 가볍고 유연한 마이크로 프레임워크로 빠른 API 프로토타이핑에 적합합니다.

Flasgger (Swagger): 별도의 문서 작성 없이 코드 내 docstring만으로 시각적인 API 테스트 환경을 구축할 수 있어 선정했습니다.

Sphinx: 파이썬 표준 문서화 도구로, 대규모 프로젝트에서도 체계적인 HTML 문서를 생성할 수 있어 사용했습니다.

GitHub Pages: 결과물을 정적 웹사이트로 배포하여 누구나 접근 가능한 포트폴리오를 만들기 위해 활용했습니다.

5. Key Features
   Full CRUD Operations: 데이터 조회(GET), 생성(POST), 수정(PUT), 삭제(DELETE)가 가능한 5개의 API 엔드포인트.

Interactive Documentation: Swagger UI를 통해 브라우저에서 직접 API 호출 및 응답 확인 가능.

Automated Technical Site: Sphinx를 이용해 코드 구조와 모듈 설명을 담은 독립적인 기술 문서 사이트 제공.

6. Getting Started Guide
   Prerequisites
   Python 3.x

pip (Python package manager)

Installation
Bash

# 1. Repository Clone

git clone [본인_레포지토리_URL]
cd [폴더명]

# 2. Install Dependencies

pip install -r requirements.txt

# 3. Run Server

python app.py
Links
API Documentation (Local): http://localhost:5000/apidocs/

Official Tech Docs: (https://welsh-bit.github.io/web-service/)

7. Lessons Learned / Challenges
   Challenge: Sphinx 빌드 및 GitHub Pages 배포 환경 설정
   프로젝트를 진행하는 도중에 git bash를 이용해서 파일 디렉토리를 찾는 부분에 문제가 있어서 시간을 조금 지체했습니다. 3학년 때 편입하게 돼서 github나 gitbash를 사용하는 법이나 html로 웹사이트 디자인을 하는 것에 있어서 기본 지식이 많이 뒤떨어지는 것 같아서 주어진 과제에 있는 문제를 해결하는 것만으로도 벅찬 것 같습니다.
   하지만 프로젝트를 하나하나 해결하면서 merge를 사용하는 법이나 github의 사용방법을 조금씩 익혀나가고 있는 것 같고 해결할때마다 나름의 성취감도 느껴지는 것 같습니다.
   기본지식이 떨어지다 보니 솔직히 ai를 의지하는 부분이 많은데 장기적으로는 이미 익힌 부분은 스스로 할 수 있게되는 것을 목표로 삼고 싶습니다.
