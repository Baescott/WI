# 점심시간 맛집+강수예보 앱 구현 계획 (이슈 #8)

## 결정된 사항

| 항목 | 결정 |
|---|---|
| 맛집 위치 데이터 | 카카오 로컬 API (키워드/카테고리 검색) |
| 기준 위치 | 회사 주소를 설정값으로 입력받음 (하드코딩 X — 나중에 사용자별로 늘어나도 각자 이 값만 따로 가지면 확장 가능) |
| 지오코딩(주소→좌표) | 카카오 로컬 API 주소검색으로 통합 (구글맵 지오코딩은 폐기) |

## 기존 코드(2021~2022) 감사 결과

| 파일 | 상태 | 비고 |
|---|---|---|
| `get_kmo/lambert.py` | ✅ 재사용 가능 | 기상청 공식 좌표변환 공식 그대로라 수년째 안 바뀜 |
| `get_kmo/get_weather_srt_ncst.py` | ⚠️ 수정 필요 | 하드코딩된 서비스키가 죽어있음(`SERVICE_KEY_IS_NOT_REGISTERED_ERROR`, 실제로 호출해서 확인함). 재발급 필요 + 이미 공개 레포에 노출됐던 키라 보안상으로도 교체 대상 |
| `get_kmo/get_weather_srt_fcst.py` | ⚠️ 수정 필요 | 위와 동일한 키 문제 |
| import 구조 | 🐛 버그 | `get_weather_srt_ncst.py`는 `from get_kmo.lambert import ...`, `get_weather_srt_fcst.py`는 `from lambert import ...`로 서로 다른 방식이라 같이 못 씀. main.py에도 이 두 함수 import가 주석처리돼 있던 이유로 보임 |
| 에러 처리 | 🐛 없음 | API 실패 시 그대로 예외 발생 |
| `get_course/get_coordinates.py` | ❌ 폐기 | Google Maps 지오코딩 사용. `viewport.northeast`(지도 뷰박스 모서리)를 장소의 실제 좌표처럼 잘못 쓰고 있음(딕셔너리 키를 이름이 아니라 순서로 접근하다 잘못 짚은 버그) + 별도 GCP 빌링 계정 필요 |

## 사전 준비 (본인이 직접 발급)

- [ ] 기상청 서비스키 재발급 — [공공데이터포털](https://www.data.go.kr/data/15084084/openapi.do) (기상청 단기예보 조회서비스)
- [ ] 카카오 REST API 키 발급 — [카카오 디벨로퍼스](https://developers.kakao.com) (로컬 API: 주소검색 + 키워드 장소검색)
- 두 키 모두 **커밋 금지** — `.env` 또는 별도 비공개 설정 파일로 관리

## 구현 단계

```
0. [옛날 코드 정비]
   → verify: lambert.py는 그대로 유지, ncst/fcst의 import 버그 수정 + 최소 에러처리 추가,
     구글맵 의존성(get_coordinates.py) 제거

1. [카카오 REST API 키 발급]
   → verify: 키 하나로 주소검색 API + 키워드 장소검색 API 둘 다 테스트 호출 성공

2. [회사 주소 입력받기]
   → verify: 텍스트로 회사 주소 입력하면 카카오 주소검색으로 좌표(위경도) 변환됨
     (한 번 설정하면 재사용 — 나중에 여러 사용자가 써도 각자 이 값만 따로 가지면 확장 가능)

3. [반경 내 맛집 목록 조회]
   → verify: 카카오 로컬 API 키워드검색(음식점 카테고리, category_group_code=FD6)으로
     회사 주변 맛집 리스트(이름+좌표)가 실제로 나옴

4. [맛집 좌표 → 기상청 격자 변환 + 예보 조회]
   → verify: lambert.py로 좌표를 격자(X,Y)로 변환하고, 같은 격자에 속한 맛집은
     API 호출 한 번으로 묶여서 쿼터가 절약됨

5. [강수확률/강수형태 임계값으로 "우산" 판정]
   → verify: 초단기예보(getUltraSrtFcst)의 PTY(강수형태)/POP(강수확률) 값을
     임계값과 비교해 O/X가 정확히 갈림

6. [맛집명 + 판정 결과 출력]
   → verify: 실행하면 "OO식당 - 우산 챙기셈" 형태로 리스트가 출력됨

7. [실측 테스트]
   → verify: 실제 비 오는 날 / 안 오는 날 값을 비교해 판정이 맞게 나오는지 확인
```

## 관련 자료

- 이슈: https://github.com/Baescott/WI/issues/8
- 노면 습윤 이슈(향후 확장 후보): https://github.com/Baescott/WI/issues/7
- 리서치 원본: `~/Documents/weather-app-research.md`
