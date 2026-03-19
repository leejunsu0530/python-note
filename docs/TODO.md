# TODO

## 파이썬 관련
- [ ] gradio와 백앤드 연결 어떻게 할지
- [ ] deque가 리스트에서 앞쪽에서 값을 뺄때는 더 속도가 빠르지 않나? 근데 그냥 제너레이터를 쓰면 되지 않나? 제너레이터 대신 그냥 반복문으로 즉석 처리를 하면 되지 않나?
- [ ] 

## yt-dlp 관련

### info dict 관련
- [ ] _InfoDict 객체 찾기
- [ ] 더 빠른 info 다운로드(멀티스레딩) 찾아보기
- [ ] 내가 extract_info할때와 --write-info-dict 할때 차이? (개별 영상은 따로 저장되나?)
- [ ] 플리를 통째로 가져와서 파일로 저장하면 그건 파일로 다운로드가 되는지?
- [ ] 플레이리스트를 개별 영상 파일들로 쪼개기
- [ ] yt-dlp가 다운때 플리를 어떻게 가져오는지 디버깅용 출력 pp와 -j 옵션으로 알아내기. 출력 메시지 상 플리의 개략적인 정보를 알아오고 개별 영상을 불러오는 구조인데 내가 그냥 할때랑 다른 이유?

### pp 관련
- [ ] [여기](https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#plugins)서 pp에 인자 전달 방법 및 기본 시점 정의하는 방법 찾기

### 인자(optparse) 관련
- [ ] 인자 출력 부분 ** 사용해서 강조. 아래 내용 보고 인자(metavar 등)를 어떻게 쓰고 있고 파싱하는지 확인
    - https://docs.python.org/ko/3/howto/argparse-optparse.html
    - https://docs.python.org/ko/3/library/optparse.html
