import streamlit as st

# 1. 웹페이지 기본 설정
st.set_page_config(
    page_title="당곡고 소울 애니멀 매칭 🐾",
    page_icon="🐾",
    layout="centered"
)

# 2. 귀여운 파스텔톤 배경과 '둥실둥실 움직이는 이모지 애니메이션'을 위한 CSS
st.markdown("""
<style>
    /* 전체 배경색 설정 */
    .stApp {
        background-color: #FFF9F2;
    }
    h1 {
        color: #FF8A8A;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        text-align: center;
    }
    h3 {
        color: #4A4A4A;
        text-align: center;
    }
    /* 결과 카드 디자인 */
    .cute-card {
        background-color: #FFFFFF;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.05);
        border: 2px solid #FFE3E3;
        margin-top: 20px;
        text-align: center;
    }
    /* MBTI 뱃지 스타일 */
    .mbti-badge {
        background-color: #FF8A8A;
        color: white;
        padding: 5px 15px;
        border-radius: 50px;
        font-weight: bold;
        font-size: 1.2rem;
        display: inline-block;
        margin-bottom: 15px;
    }
    
    /* 둥실둥실 움직이는 이모지 애니메이션 정의 */
    @keyframes bounce {
        from {
            transform: translateY(0px);
        }
        to {
            transform: translateY(-15px);
        }
    }
    
    /* 거대하고 귀여운 이모지 영역 스타일 */
    .giant-emoji {
        font-size: 8rem;
        text-align: center;
        margin: 25px 0;
        display: block;
        animation: bounce 0.8s infinite alternate ease-in-out; /* 부드러운 왕복 운동 */
        filter: drop-shadow(0px 10px 10px rgba(0, 0, 0, 0.1));
    }
</style>
""", unsafe_allow_html=True)

# 3. MBTI별 이모지 데이터베이스 구축 (이미지 URL 제거 및 이모지 집중)
mbti_db = {
    "ISTJ": {
        "animal": "성실한 비버 (Beaver)",
        "desc": "매우 책임감이 강하고 철저하게 계획을 세워 행동하는 당신! 비버처럼 차근차근 자신의 집을 짓는 꼼꼼한 실천가예요.",
        "emoji": "🦫",
        "best_match": "ESFP",
        "traits": ["계획적", "성실함", "책임감", "규칙주의"]
    },
    "ISFJ": {
        "animal": "포근한 양 (Sheep)",
        "desc": "주변 사람들을 조용하고 따뜻하게 챙겨주는 당신! 양처럼 포근하고 다정한 성품으로 늘 타인에게 안정감을 준답니다.",
        "emoji": "🐑",
        "best_match": "ESTP",
        "traits": ["다정다감", "헌신적", "조용한 조력자", "세심함"]
    },
    "INFJ": {
        "animal": "신비로운 사슴 (Deer)",
        "desc": "깊은 통찰력을 가지고 세상을 바라보는 섬세한 당신! 숲속의 사슴처럼 신비롭고 고결한 분위기를 지니고 있어요.",
        "emoji": "🦌",
        "best_match": "ENFP",
        "traits": ["통찰력", "이상주의", "섬세함", "신비로움"]
    },
    "INTJ": {
        "animal": "지혜로운 올빼미 (Owl)",
        "desc": "전략적인 사고와 뛰어난 분석력의 소유자인 당신! 올빼미처럼 높은 곳에서 멀리 보며 깊은 생각에 잠기는 독립적인 해결사예요.",
        "emoji": "🦉",
        "best_match": "ENFP",
        "traits": ["전략가", "독립심", "지적호기심", "논리적"]
    },
    "ISTP": {
        "animal": "시크한 고양이 (Cat)",
        "desc": "마이웨이 성향이 강하고 실용적인 도구를 잘 다루는 당신! 도도하고 조용하지만 호기심이 생기면 무섭게 집중하는 고양이 같아요.",
        "emoji": "🐱",
        "best_match": "ESFJ",
        "traits": ["적응력", "과묵함", "실용주의", "효율중시"]
    },
    "ISFP": {
        "animal": "느긋한 코알라 (Koala)",
        "desc": "예술적 감각이 뛰어나고 평화를 사랑하는 따뜻한 당신! 나무 위에서 여유를 즐기는 코알라처럼 느긋하고 편안한 에너지를 풍겨요.",
        "emoji": "🐨",
        "best_match": "ENFJ",
        "traits": ["예술가", "자유 영혼", "온화함", "평화주의"]
    },
    "INFP": {
        "animal": "사랑스런 토끼 (Rabbit)",
        "desc": "상상력이 풍부하고 감수성이 깊은 낭만파인 당신! 작고 귀여운 토끼처럼 마음이 따뜻하고, 자신만의 비밀 정원을 가꾸는 예술가예요.",
        "emoji": "🐰",
        "best_match": "ENTJ",
        "traits": ["이상가", "감수성", "이타적", "예술적"]
    },
    "INTP": {
        "animal": "궁금한 미어캣 (Meerkat)",
        "desc": "끝없는 호기심과 독창적인 생각으로 똘똘 뭉친 당신! 주위를 두리번거리며 새로운 지식과 논리를 탐구하는 영리한 탐험가 같아요.",
        "emoji": "🦦", # 미어캣 대용으로 귀여운 수달 이모지 사용!
        "best_match": "ENTJ",
        "traits": ["아이디어", "호기심", "분석적", "독창적"]
    },
    "ESTP": {
        "animal": "날렵한 여우 (Fox)",
        "desc": "활동적이고 센스 넘치는 에너지파 당신! 똑똑하고 눈치 빠른 여우처럼 현실 적응력이 빠르고 매 순간 스릴과 재미를 추구해요.",
        "emoji": "🦊",
        "best_match": "ISFJ",
        "traits": ["모험가", "빠른 실행", "센스만점", "유연성"]
    },
    "ESFP": {
        "animal": "흥부자 강아지 (Retriever)",
        "desc": "긍정 에너지가 넘치고 사람들을 좋아하는 마당발 당신! 꼬리를 흔들며 모두에게 친근하게 다가가는 리트리버처럼 언제나 밝은 웃음을 전달해요.",
        "emoji": "🐶",
        "best_match": "ISTJ",
        "traits": ["친화력", "긍정왕", "유머러스", "에너지"]
    },
    "ENFP": {
        "animal": "재기발랄 돌고래 (Dolphin)",
        "desc": "상상력이 풍부하고 사교성이 아주 뛰어난 당신! 바닷속을 자유롭게 헤엄치며 친구들과 노래하는 돌고래처럼 활기차고 매력적인 사람이에요.",
        "emoji": "🐬",
        "best_match": "INFJ",
        "traits": ["열정가", "사교적", "자유로움", "크리에이터"]
    },
    "ENTP": {
        "animal": "말괄량이 앵무새 (Parrot)",
        "desc": "독창적이고 뛰어난 화술을 가진 유쾌한 변론가 당신! 화려하고 똑똑하게 말을 잘하는 앵무새처럼 세상을 다채롭고 재미있게 뒤흔들어요.",
        "emoji": "🦜",
        "best_match": "INFJ",
        "traits": ["아이디어뱅크", "토론광", "유머러스", "임기응변"]
    },
    "ESTJ": {
        "animal": "든든한 사자 (Lion)",
        "desc": "추진력이 뛰어나고 단체나 조직을 멋지게 이끄는 리더인 당신! 초원의 왕 사자처럼 든든한 카리스마와 강한 책임감으로 무리를 지켜냅니다.",
        "emoji": "🦁",
        "best_match": "ISFP",
        "traits": ["지도자", "추진력", "책임감", "현실적"]
    },
    "ESFJ": {
        "animal": "사랑둥이 펭귄 (Penguin)",
        "desc": "동료애가 강하고 조화로운 분위기를 중시하는 다정한 당신! 남극에서 옹기종기 모여 서로를 배려하는 펭귄 같은 사교적인 성격의 소유자예요.",
        "emoji": "🐧",
        "best_match": "ISTP",
        "traits": ["배려심", "친절함", "협력적", "조화주의"]
    },
    "ENFJ": {
        "animal": "따뜻한 코끼리 (Elephant)",
        "desc": "사람들을 따뜻하게 배려하고 바른 길로 인도하는 당신! 평화로우면서도 거대한 품으로 무리를 돌보는 따뜻하고 이타적인 코끼리 같은 인도자예요.",
        "emoji": "🐘",
        "best_match": "ISFP",
        "traits": ["이타심", "선한 영향력", "소통능력", "다정함"]
    },
    "ENTJ": {
        "animal": "용맹한 독수리 (Eagle)",
        "desc": "장기적인 비전을 설정하고 사람들을 진두지휘하는 열정가 당신! 높은 하늘을 날아오르며 멀리 내다보고 냉철하게 결단을 내리는 카리스마 리더입니다.",
        "emoji": "🦅",
        "best_match": "INFP",
        "traits": ["지도력", "비전가", "도전정신", "결단력"]
    }
}

# 4. 헤더 영역 구성
st.markdown("<h1>🐾 나의 MBTI 소울 애니멀 매칭!</h1>", unsafe_allow_html=True)
st.markdown("<h3>당곡고 친구들을 위한 나만의 특별한 동물 친구 찾기 💡</h3>", unsafe_allow_html=True)
st.write("---")

# 5. 두 가지 입력 방식 탭 구성
tab1, tab2 = st.tabs(["💡 MBTI 바로 선택하기", "📝 미니 테스트로 찾기"])

# 사용자가 결정한 MBTI를 저장할 변수 초기화
selected_mbti = None

with tab1:
    st.write("이미 내 MBTI를 알고 있다면 아래에서 선택해 주세요!")
    mbti_list = sorted(list(mbti_db.keys()))
    selected_mbti = st.selectbox("당신의 MBTI는 무엇인가요?", mbti_list)

with tab2:
    st.write("간단한 4가지 질문을 통해 내 성향에 맞는 동물을 찾아보세요!")
    
    col1, col2 = st.columns(2)
    with col1:
        q1 = st.radio(
            "1. 주말에 에너지를 충전하는 방법은?",
            ("친구들과 신나게 외출하기 (E)", "혼자 방에서 조용히 쉬기 (I)")
        )
    with col2:
        q2 = st.radio(
            "2. 새로운 대상을 볼 때 나의 초점은?",
            ("현실적이고 구체적인 사실 (S)", "가능성과 상상, 미래 가치 (N)")
        )
        
    col3, col4 = st.columns(2)
    with col3:
        q3 = st.radio(
            "3. 힘들어하는 친구를 위로할 때?",
            ("감정에 공감하며 위로하기 (F)", "원인을 분석하고 조언하기 (T)")
        )
    with col4:
        q4 = st.radio(
            "4. 계획과 일상생활을 대하는 태도는?",
            ("꼼꼼하게 계획을 세워 행동 (J)", "그때그때 유연하고 즉흥적 (P)")
        )
    
    calc_mbti = ""
    calc_mbti += "E" if "E" in q1 else "I"
    calc_mbti += "S" if "S" in q2 else "N"
    calc_mbti += "T" if "T" in q3 else "F"
    calc_mbti += "J" if "J" in q4 else "P"
    
    if st.button("결과 확인하기 🎉"):
        selected_mbti = calc_mbti
        st.success(f"당신의 조합 결과는 **{selected_mbti}**입니다!")

# 6. 매칭 결과 표시 영역
if selected_mbti:
    st.balloons()  # 축하 풍선 이펙트
    
    animal_info = mbti_db[selected_mbti]
    best_mbti = animal_info["best_match"]
    best_animal_info = mbti_db[best_mbti]
    
    # 둥실둥실 움직이는 대형 이모지 렌더링 영역 (st.image를 대체하는 핵심 요소!)
    st.markdown(f'<div class="giant-emoji">{animal_info["emoji"]}</div>', unsafe_allow_html=True)
    
    # 결과 설명 카드
    st.markdown(f"""
    <div class="cute-card">
        <span class="mbti-badge">{selected_mbti}</span>
        <h2 style='color:#FF8A8A; margin-top:5px; margin-bottom:15px;'>{animal_info['animal']}</h2>
        <p style='color:#555555; font-size:1.1rem; line-height:1.7; word-break:keep-all;'>{animal_info['desc']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write(" ")
    
    # 성격 키워드 태그 표시
    st.write("#### 🌟 나의 주요 성격 키워드")
    cols = st.columns(len(animal_info["traits"]))
    for idx, trait in enumerate(animal_info["traits"]):
        cols[idx].info(f"#{trait}")
        
    st.write("---")
    
    # 단짝 매칭 정보 제공
    st.write("#### 💞 나와 가장 잘 어울리는 소울메이트 단짝 동물!")
    col_left, col_right = st.columns([1, 4])
    with col_left:
        # 단짝 동물 이모지도 가볍게 흔들리도록 스타일 부여 가능
        st.markdown(f"<div style='font-size: 4rem; text-align: center;'>{best_animal_info['emoji']}</div>", unsafe_allow_html=True)
    with col_right:
        st.write(f"**{best_mbti}** 성향의 **{best_animal_info['animal']}**")
        st.caption(best_animal_info["desc"])

    st.write(" ")
    st.button("🔗 친구들에게 결과 링크 공유하기 (당곡고 단톡방 고고!)")
