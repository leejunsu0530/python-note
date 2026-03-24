from yt_dlp.options import create_parser
from yt_dlp import parse_options
import sys
import optparse
from rich.pretty import pprint

if __name__ == "__main__":
    parser, opts, urls, ydl_opts = parse_options(["-f", "ba+bv", "-o", "OUTPUT___________________", "TEST_UTL______________________"])
    pprint(parser.down)
    # 1. opts나 ydl_opts > 이 함수로 cli2api 대체 가능? 애초에 그 파일의 달라지는 점이 뭔데... 그 파일에서 애초에 쓰긴 함 >> 그냥 이건 원래대로
    # 2. 여기 파서와 아래 파서의 차이? 질문하기
    # pprint(opts)
    # print("urls____________")
    # pprint(urls)
    # print("ydlopts______________")
    # pprint(ydl_opts)

    parser2 = create_parser()
    pprint(parser2)
