import os
import json
import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


QUOTES_FILE = 'quotes.json' 

def load_quotes():
    """
    quotes.json 파일에서 명언 데이터를 불러옵니다.
    파일이 없거나 비어있으면 초기 명언 데이터를 생성합니다.
    """
    if not os.path.exists(QUOTES_FILE) or os.path.getsize(QUOTES_FILE) == 0:
        print(f"'{QUOTES_FILE}' 파일을 찾을 수 없거나 비어 있습니다. 초기 명언 데이터를 생성합니다.")
        initial_quotes = [
            {"quote": "모든 것을 가질 수는 없지만, 당신이 진정으로 원하는 것을 가질 수는 있습니다.", "author": "오프라 윈프리"},
            {"quote": "성공은 최종적인 것이 아니며, 실패는 치명적인 것이 아니다. 중요한 것은 계속하려는 용기이다.", "author": "윈스턴 처칠"},
            {"quote": "상상력은 지식보다 중요하다. 지식은 제한되어 있지만, 상상력은 세상을 아우른다.", "author": "알베르트 아인슈타인"},
            {"quote": "가장 중요한 것은 인생을 즐기는 것이다. 행복하게 사는 것, 그것이 전부이다.", "author": "오드리 헵번"},
            {"quote": "우리가 두려워해야 할 유일한 것은 두려움 그 자체이다.", "author": "프랭클린 D. 루스벨트"},
            {"quote": "시작이 반이다.", "author": "아리스토텔레스"},
            {"quote": "인생은 속도가 아니라 방향이다.", "author": "마하트마 간디"},
            {"quote": "가장 큰 위험은 아무런 위험도 감수하지 않는 삶이다.", "author": "마크 저커버버그"}
        ]
        with open(QUOTES_FILE, 'w', encoding='utf-8') as f:
            json.dump(initial_quotes, f, ensure_ascii=False, indent=4)
        return initial_quotes
    else:
        try:
            with open(QUOTES_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"오류: '{QUOTES_FILE}' 파일의 JSON 형식이 올바르지 않습니다. 파일을 확인해주세요.")
            return [] 

quotes_data = load_quotes() 

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    메인 웹페이지를 렌더링하고, 명언을 선택하여 표시합니다.
    GET 요청 시에는 명언이 없는 초기 페이지를 보여주거나,
    POST 요청 (버튼 클릭) 시에는 새 명언을 선택하여 보여줍니다.
    """
    selected_quote = None
    selected_author = None

    if request.method == 'POST':
        
        if quotes_data:
            random_item = random.choice(quotes_data)
            selected_quote = random_item.get('quote', '명언을 찾을 수 없습니다.')
            selected_author = random_item.get('author', '알 수 없음')
        else:
            selected_quote = "명언을 찾을 수 없습니다. quotes.json 파일을 확인해주세요."
            selected_author = "시스템"

    
    return render_template('index.html', quote=selected_quote, author=selected_author)

if __name__ == '__main__':
    app.run(debug=True)
