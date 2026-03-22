# yt-dlp-note

## PP

## infodict

### 다운로드 시 flat

플리 업로더 등 데이터는 일단 no flat에서만 기록됨(당연히)
1. 자동 기록(no flat)으로 하면 동영상 파일 각각에 기록됨. 이게 가장 좋지만, 가속은 안됨
2. 내가 기록하면 no flat일때, 전체 플리 데이터가 한 파일에 들어감. 이건 x.

1에서 가속은 어떻게?

## yt-dlp args

## outtmpl

### 형식에 값 채워넣기

- ydl.evaluate_outtmpl 쓰면 출력 템플릿에 infodict 넣을 수 있음.
- playlist_uploader 쓰면 플리를 영상 업로더가 아니라 플리 업로더로 분류 가능

