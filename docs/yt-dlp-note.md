# yt-dlp-note

## PP

### 1. PP의 기본 시점 정의 위치
좀 쪼개져 있는 듯한데, 사실 중요하진 않음. 내 PP는 내가 파이썬 함수로 결정하면 되니까.

1. CLI 옵션에서 --embed-thumbnail는 플래그만 켭니다. 
2. 실제 PP(후처리) 리스트에 EmbedThumbnail을 올리는 곳: `yt_dlp/__init__.py`: 651 근처 

    <summary>

    ```python
    def get_postprocessors(opts):
        yield from opts.add_postprocessors

        for when, actions in opts.parse_metadata.items():
            yield {
                'key': 'MetadataParser',
                'actions': actions,
                'when': when,
            }
        sponsorblock_query = opts.sponsorblock_mark | opts.sponsorblock_remove
        if sponsorblock_query:
            yield {
                'key': 'SponsorBlock',
                'categories': sponsorblock_query,
                'api': opts.sponsorblock_api,
                'when': 'after_filter',
            }
        if opts.convertsubtitles:
            yield {
                'key': 'FFmpegSubtitlesConvertor',
                'format': opts.convertsubtitles,
                'when': 'before_dl',
            }
        if opts.convertthumbnails:
            yield {
                'key': 'FFmpegThumbnailsConvertor',
                'format': opts.convertthumbnails,
                'when': 'before_dl',
            }
        if opts.extractaudio:
            yield {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': opts.audioformat,
                'preferredquality': opts.audioquality,
                'nopostoverwrites': opts.nopostoverwrites,
            }
        if opts.remuxvideo:
            yield {
                'key': 'FFmpegVideoRemuxer',
                'preferedformat': opts.remuxvideo,
            }
        if opts.recodevideo:
            yield {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': opts.recodevideo,
            }
        # If ModifyChapters is going to remove chapters, subtitles must already be in the container.
        if opts.embedsubtitles:
            keep_subs = 'no-keep-subs' not in opts.compat_opts
            yield {
                'key': 'FFmpegEmbedSubtitle',
                # already_have_subtitle = True prevents the file from being deleted after embedding
                'already_have_subtitle': opts.writesubtitles and keep_subs,
            }
            if not opts.writeautomaticsub and keep_subs:
                opts.writesubtitles = True

        # ModifyChapters must run before FFmpegMetadataPP
        if opts.remove_chapters or sponsorblock_query:
            yield {
                'key': 'ModifyChapters',
                'remove_chapters_patterns': opts.remove_chapters,
                'remove_sponsor_segments': opts.sponsorblock_remove,
                'remove_ranges': opts.remove_ranges,
                'sponsorblock_chapter_title': opts.sponsorblock_chapter_title,
                'force_keyframes': opts.force_keyframes_at_cuts,
            }
        # FFmpegMetadataPP should be run after FFmpegVideoConvertorPP and
        # FFmpegExtractAudioPP as containers before conversion may not support
        # metadata (3gp, webm, etc.)
        # By default ffmpeg preserves metadata applicable for both
        # source and target containers. From this point the container won't change,
        # so metadata can be added here.
        if opts.addmetadata or opts.addchapters or opts.embed_infojson:
            yield {
                'key': 'FFmpegMetadata',
                'add_chapters': opts.addchapters,
                'add_metadata': opts.addmetadata,
                'add_infojson': opts.embed_infojson,
            }
        if opts.embedthumbnail:
            yield {
                'key': 'EmbedThumbnail',
                # already_have_thumbnail = True prevents the file from being deleted after embedding
                'already_have_thumbnail': opts.writethumbnail,
            }
            if not opts.writethumbnail:
                opts.writethumbnail = True
                opts.outtmpl['pl_thumbnail'] = ''
        if opts.split_chapters:
            yield {
                'key': 'FFmpegSplitChapters',
                'force_keyframes': opts.force_keyframes_at_cuts,
            }
        # XAttrMetadataPP should be run after post-processors that may change file contents
        if opts.xattrs:
            yield {'key': 'XAttrMetadata'}
        if opts.concat_playlist != 'never':
            yield {
                'key': 'FFmpegConcat',
                'only_multi_video': opts.concat_playlist != 'always',
                'when': 'playlist',
            }
        # Exec must be the last PP of each category
        for when, exec_cmd in opts.exec_cmd.items():
            yield {
                'key': 'Exec',
                'exec_cmd': exec_cmd,
                'when': when,
            }

    ```
    </summary>
    
    **몇몇 PP는 여기에 when 정의 안 되어 있음.**

3. 몇몇 PP가 when 기본값을 채우는 곳: `yt_dlp/YoutubeDL.py:826` 근처

    ```python
    for pp_def_raw in self.params.get('postprocessors', []):
        pp_def = dict(pp_def_raw)
        when = pp_def.pop('when', 'post_process')
        self.add_post_processor(
            get_postprocessor(pp_def.pop('key'))(self, **pp_def),
            when=when)
    ```

## infodict
플리 업로더 등 데이터는 일단 no flat에서만 기록됨(당연히)
1. 자동 기록(no flat)으로 하면 동영상 파일 각각에 기록됨. 이게 가장 좋지만, 가속은 안됨
2. 내가 기록하면 no flat일때, 전체 플리 데이터가 한 파일에 들어감. 이건 x.
> 1에서 가속은 어떻게 하지?

## yt-dlp args

### 1. cli의 호출 구조 및 파서 내부 활용 구조
1. cmd에서 'yt-dlp' 사용시 `yt-dlp.main` 호출
2. `__init__`의 `main()` 호출
3. `__init__`의 `_real_main()`에서 `parser, opts, all_urls, ydl_opts = parse_options(argv)`로 사용
4. `__init__`의 `parse_options`에서 `parsedOpts` 호출
    ```python
    ParsedOptions = collections.namedtuple('ParsedOptions', ('parser', 'options', 'urls', 'ydl_opts'))

    def parse_options(argv=None):
        """@returns ParsedOptions(parser, opts, urls, ydl_opts)"""
        parser, opts, urls = parseOpts(argv)
        ...
    ```
5. `options.py`의 `parseOpts`에서 `create_parser` 호출
6. `create_parser`로 정의된 파서 가져옴.

그러니까, 파서는 일단 보이기에는 2가지가 있다. `__init__`의 `parse_options의 첫번째 인자`와 `options.py`의 `create_parser`(원본 파서)

이 둘은 같은 객체이다.  
`create_parser()`가 만든 `_YoutubeDLOptionParser` 인스턴스가 `parseOpts()`를 거쳐 그대로 `parse_options()`로 전달된다.  
즉 `parse_options()`가 반환하는 `parser`는 원본 파서와 **동일한 객체**다.

그 대신 달라지는 건 `opts`와 `ydl_opts` 쪽이다.
1. `parseOpts()`에서 config/CLI/override args를 병합하고 `opts, args`를 만든다.
2. `parse_options()`에서 `set_compat_opts(opts)` + `validate_options(opts)`로 값 정규화/검증을 수행한다.
3. 실행 흐름에 맞춰 `quiet`, `extract_flat`, `postprocessors`, `final_ext` 같은 파생 상태를 계산한다.
4. 마지막에 `opts`를 기반으로 `ydl_opts` dict로 변환해 `YoutubeDL`에 전달한다.



### 2. parser의 옵션 정의 구조

`options.py`의 `create_parser` 내에는 다음과 같이 정의됨.

<details>
<summary>파서 정의 예제 펼치기</summary>

```python
downloader = optparse.OptionGroup(parser, 'Download Options')
downloader.add_option(
    '-N', '--concurrent-fragments',
    dest='concurrent_fragment_downloads', metavar='N', default=1, type=int,
    help='Number of fragments of a dash/hlsnative video that should be downloaded concurrently (default is %default)')
downloader.add_option(
    '--retry-sleep',
    dest='retry_sleep', metavar='[TYPE:]EXPR', default={}, type='str',
    action='callback', callback=_dict_from_options_callback,
    callback_kwargs={
        'allowed_keys': 'http|fragment|file_access|extractor',
        'default_key': 'http',
    }, help=(
        'Time to sleep between retries in seconds (optionally) prefixed by the type of retry '
        '(http (default), fragment, file_access, extractor) to apply the sleep to. '
        'EXPR can be a number, linear=START[:END[:STEP=1]] or exp=START[:END[:BASE=2]]. '
        'This option can be used multiple times to set the sleep for the different retry types, '
        'e.g. --retry-sleep linear=1::2 --retry-sleep fragment:exp=1:20'))
downloader.add_option(
    '--downloader-args', '--external-downloader-args',
    metavar='NAME:ARGS', dest='external_downloader_args', default={}, type='str',
    action='callback', callback=_dict_from_options_callback,
    callback_kwargs={
        'allowed_keys': r'ffmpeg_[io]\d*|{}'.format('|'.join(map(re.escape, list_external_downloaders()))),
        'default_key': 'default',
        'process': shlex.split,
    }, help=(
        'Give these arguments to the external downloader. '
        'Specify the downloader name and the arguments separated by a colon ":". '
        'For ffmpeg, arguments can be passed to different positions using the same syntax as --postprocessor-args. '
        'You can use this option multiple times to give different arguments to different downloaders '
        '(Alias: --external-downloader-args)'))

# choices는 현재 기준 이 2개뿐
postproc.add_option(
    '--concat-playlist',
    metavar='POLICY', dest='concat_playlist', default='multi_video',
    choices=('never', 'always', 'multi_video'),
    help=(
        'Concatenate videos in a playlist. One of "never", "always", or '
        '"multi_video" (default; only when the videos form a single show). '
        'All the video files must have the same codecs and number of streams to be concatenable. '
        'The "pl_video:" prefix can be used with "--paths" and "--output" to '
        'set the output filename for the concatenated files. See "OUTPUT TEMPLATE" for details'))
postproc.add_option(
    '--fixup',
    metavar='POLICY', dest='fixup', default=None,
    choices=('never', 'ignore', 'warn', 'detect_or_warn', 'force'),
    help=(
        'Automatically correct known faults of the file. '
        'One of never (do nothing), warn (only emit a warning), '
        'detect_or_warn (the default; fix the file if we can, warn otherwise), '
        'force (try fixing even if the file already exists)'))

postproc.add_option(
    '--parse-metadata',
    metavar='[WHEN:]FROM:TO', dest='parse_metadata', **when_prefix('pre_process'),
    help=(
        'Parse additional metadata like title/artist from other fields; see "MODIFYING METADATA" for details. '
        'Supported values of "WHEN" are the same as that of --use-postprocessor (default: pre_process)'))
postproc.add_option(
    '--replace-in-metadata',
    dest='parse_metadata', metavar='[WHEN:]FIELDS REGEX REPLACE', nargs=3, **when_prefix('pre_process'),
    help=(
        'Replace text in a metadata field using the given regex. This option can be used multiple times. '
        'Supported values of "WHEN" are the same as that of --use-postprocessor (default: pre_process)'))

extractor.add_option(
    '--extractor-args',
    metavar='IE_KEY:ARGS', dest='extractor_args', default={}, type='str',
    action='callback', callback=_dict_from_options_callback,
    callback_kwargs={
        'multiple_keys': False,
        'process': lambda val: dict(
            _extractor_arg_parser(*arg.split('=', 1)) for arg in val.split(';')),
    }, help=(
        'Pass ARGS arguments to the IE_KEY extractor. See "EXTRACTOR ARGUMENTS" for details. '
        'You can use this option multiple times to give arguments for different extractors'))

```
</details>


또한 -t로 시작하는 프리셋은 다음과 같음.

<details>
<summary>-t 정의 함수 펼치기</summary>

```python
_PRESET_ALIASES = {
    'mp3': ['-f', 'ba[acodec^=mp3]/ba/b', '-x', '--audio-format', 'mp3'],
    'aac': ['-f', 'ba[acodec^=aac]/ba[acodec^=mp4a.40.]/ba/b', '-x', '--audio-format', 'aac'],
    'mp4': ['--merge-output-format', 'mp4', '--remux-video', 'mp4', '-S', 'vcodec:h264,lang,quality,res,fps,hdr:12,acodec:aac'],
    'mkv': ['--merge-output-format', 'mkv', '--remux-video', 'mkv'],
    'sleep': ['--sleep-subtitles', '5', '--sleep-requests', '0.75', '--sleep-interval', '10', '--max-sleep-interval', '20'],
}

...

def format_option_help(self, formatter=None):
    assert formatter, 'Formatter can not be None'
    formatted_help = super().format_option_help(formatter=formatter)
    formatter.indent()
    heading = formatter.format_heading('Preset Aliases')
    formatter.indent()
    description = formatter.format_description(
        'Predefined aliases for convenience and ease of use. Note that future versions of yt-dlp '
        'may add or adjust presets, but the existing preset names will not be changed or removed')
    result = []
    for name, args in _PRESET_ALIASES.items():
        option = optparse.Option('-t', help=shlex.join(args))
        formatter.option_strings[option] = f'-t {name}'
        result.append(formatter.format_option(option))
    formatter.dedent()
    formatter.dedent()
    help_lines = '\n'.join(result)
    return f'{formatted_help}\n{heading}{description}\n{help_lines}'

```

</details>

여기서 정의에 사용하는 인자는 다음과 같음.

- metavars
- type
- choices(2개만 사용)
- 

### 3. 옵션 꺼내기
옵션은 다음과 같은 방법으로 꺼낼 수 있음.
```python
from yt_dlp.options import create_parser

parser = create_parser()
target_opt = None

for group in parser.option_groups:
    if group.title == "Download Options":
        for opt in group.option_list:
            # opt._long_opts에는 '--download-sections' 같은 값들이 들어있음
            if "--download-sections" in opt._long_opts:
                target_opt = opt
                break

if target_opt:
    print("help:", target_opt.help)
    print("metavar:", target_opt.metavar)

# 또는 그룹은 접근할 필요 없으면,
opt = parser.get_option("--download-sections")
print(opt.help)
print(opt.metavar)
```



## outtmpl

### 1. 형식에 값 채워넣기
- ydl.evaluate_outtmpl 쓰면 출력 템플릿에 infodict 넣을 수 있음.
- playlist_uploader 쓰면 플리를 영상 업로더가 아니라 플리 업로더로 분류 가능

