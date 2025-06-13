# 클릭! 오늘의 명언

## 1. 🌟 프로젝트 소개

이 프로젝트는 사용자에게 매일 새로운 영감을 주는 명언을 제공하는 간단한 웹 기반 애플리케이션입니다. Flask 프레임워크를 사용하여 백엔드를 구축하고, HTML/CSS로 사용자 인터페이스를 구현했습니다.

## 2. ✨ 주요 기능

* **명언 표시:** 웹 페이지에 접속하면 초기 명언이 표시됩니다.
* **새 명언 보기:** "오늘의 명언 보기" 버튼을 클릭할 때마다 `quotes.json` 파일에 저장된 명언 중에서 무작위로 새로운 명언이 표시됩니다.
* **데이터 관리:** 명언 데이터는 `quotes.json` 파일에 JSON 형태로 저장되어 있어, 쉽게 추가/수정/삭제가 가능합니다. (`app.py` 실행 시 자동으로 생성됩니다.)
* **간단한 UI:** 직관적이고 사용하기 쉬운 디자인으로 구성되어 있습니다.

## 3. 🛠 기술 스택

* **백엔드:** Python 3.x, Flask (웹 프레임워크)
* **프론트엔드:** HTML5, CSS3

## 4. 🚀 실행 방법

이 프로젝트는 Python과 Flask를 기반으로 하므로, Python 환경이 필요합니다.

### 4.1. 사전 준비

* **Python 3.x 설치:**
    * [Python 공식 웹사이트](https://www.python.org/downloads/)에서 최신 Python 3 버전을 다운로드하여 설치합니다.
    * **설치 시 반드시 "Add Python to PATH" 옵션을 체크**해야 합니다.
* **Visual Studio Code (또는 다른 코드 편집기) 설치:**
    * 코드를 편집하고 터미널을 사용하기 편리합니다.

### 4.2. 프로젝트 파일 다운로드

* Git을 사용하는 경우:
*   우선 바탕화면에 폴더를 하나 만들어줍니다
    그리고 윈도우 + r키를 통해 cmd창을 열어서 cd 폴더경로로 복사해줍니다
    복사후 git init 명렁어를 입력해줍니다
    그 다음 밑에있는 대로 따라합니다
    ```bash
    git clone https://github.com/parkgeonho123/MyQuoteApp.git
    cd MyQuoteApp # 또는 당신의 프로젝트 폴더 이름 (예: QuoteProject)
    ```
    git clone https://github.com/parkgeonho123/MyQuoteApp.git 입력후 폴더에보면 MyquoteApp라고 있을겁니다.
    그걸 마우스 우클릭해서 복사를 해줍니다 그 후 다시 cmd창에 들어가 cd 붙여넣기를 해줍니다
    그 후 밑에 4.3을 따라하면 실행이 됩니다 .

### 4.3. 가상 환경 설정 및 활성화

프로젝트 폴더(다운로드한 폴더, 예: `MyQuoteApp` 또는 `QuoteProject`)로 이동한 후
가상환경생성하는 코드를 입력하고 
가상 환경 활성화를 해주는 코드를 입력하고 
필요한 라이브러리 설치를 해주고 
마지막으로 애플리케이션을 실행시켜주고
http::이 주소를 복사하여 웹 브라우저에 접속하면 
실행이 됩니다.
```powershell
# 가상 환경 생성 (최초 1회)
python -m venv venv

# 가상 환경 활성화 (세션 시작 시마다)
.\venv\Scripts\activate

4.4. 필요한 라이브러리 설치
pip install -r requirements.txt

4.5. 애플리케이션 실행
python app.py


4.6. 웹 브라우저 접속
[http://127.0.0.1:5000](http://127.0.0.1:5000)
