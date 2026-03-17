# 1. General Options: 35개 옵션
## 1 (1-1): -h/--help
- short: ['-h']
- long: ['--help']
- dest(저장변수명): print_help
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Print this help text and exit
- metavar(표시 이름): None---

## 2 (1-2): --version
- short: []
- long: ['--version']
- dest(저장변수명): None
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Print program version and exit
- metavar(표시 이름): None---

## 3 (1-3): -U/--update
- short: ['-U']
- long: ['--update']
- dest(저장변수명): update_self
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Check if updates are available. You installed yt-dlp with pip or using the wheel from PyPi; Use that to update
- metavar(표시 이름): None---

## 4 (1-4): --no-update
- short: []
- long: ['--no-update']
- dest(저장변수명): update_self
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not check for updates (default)
- metavar(표시 이름): None---

## 5 (1-5): --update-to
- short: []
- long: ['--update-to']
- dest(저장변수명): update_self
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Upgrade/downgrade to a specific version. CHANNEL can be a repository as well. CHANNEL and TAG default to "stable" and "latest" respectively if omitted; See "UPDATE" for details. Supported channels: stable, nightly, master
- metavar(표시 이름): [CHANNEL]@[TAG]---

## 6 (1-6): -i/--ignore-errors
- short: ['-i']
- long: ['--ignore-errors']
- dest(저장변수명): ignoreerrors
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Ignore download and postprocessing errors. The download will be considered successful even if the postprocessing fails
- metavar(표시 이름): None---

## 7 (1-7): --no-abort-on-error
- short: []
- long: ['--no-abort-on-error']
- dest(저장변수명): ignoreerrors
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Continue with next video on download errors; e.g. to skip unavailable videos in a playlist (default)
- metavar(표시 이름): None---

## 8 (1-8): --abort-on-error/--no-ignore-errors
- short: []
- long: ['--abort-on-error', '--no-ignore-errors']
- dest(저장변수명): ignoreerrors
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Abort downloading of further videos if an error occurs (Alias: --no-ignore-errors)
- metavar(표시 이름): None---

## 9 (1-9): --list-extractors
- short: []
- long: ['--list-extractors']
- dest(저장변수명): list_extractors
- default: False
- type: None
- choices: None
- help: List all supported extractors and exit
- metavar(표시 이름): None---

## 10 (1-10): --extractor-descriptions
- short: []
- long: ['--extractor-descriptions']
- dest(저장변수명): list_extractor_descriptions
- default: False
- type: None
- choices: None
- help: Output descriptions of all supported extractors and exit
- metavar(표시 이름): None---

## 11 (1-11): --use-extractors/--ies
- short: []
- long: ['--use-extractors', '--ies']
- dest(저장변수명): allowed_extractors
- default: []
- type: string
- choices: None
- help: Extractor names to use separated by commas. You can also use regexes, "all", "default" and "end" (end URL matching); e.g. --ies "holodex.*,end,youtube". Prefix the name with a "-" to exclude it, e.g. --ies default,-generic. Use --list-extractors for a list of extractor names. (Alias: --ies)
- metavar(표시 이름): NAMES---

## 12 (1-12): --force-generic-extractor
- short: []
- long: ['--force-generic-extractor']
- dest(저장변수명): force_generic_extractor
- default: False
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 13 (1-13): --default-search
- short: []
- long: ['--default-search']
- dest(저장변수명): default_search
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Use this prefix for unqualified URLs. E.g. "gvsearch2:python" downloads two videos from google videos for the search term "python". Use the value "auto" to let yt-dlp guess ("auto_warning" to emit a warning when guessing). "error" just throws an error. The default value "fixup_error" repairs broken URLs, but emits an error if this is not possible instead of searching
- metavar(표시 이름): PREFIX---

## 14 (1-14): --ignore-config/--no-config
- short: []
- long: ['--ignore-config', '--no-config']
- dest(저장변수명): ignoreconfig
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Don't load any more configuration files except those given to --config-locations. For backward compatibility, if this option is found inside the system configuration file, the user configuration is not loaded. (Alias: --no-config)
- metavar(표시 이름): None---

## 15 (1-15): --no-config-locations
- short: []
- long: ['--no-config-locations']
- dest(저장변수명): config_locations
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not load any custom configuration files (default). When given inside a configuration file, ignore all previous --config-locations defined in the current file
- metavar(표시 이름): None---

## 16 (1-16): --config-locations
- short: []
- long: ['--config-locations']
- dest(저장변수명): config_locations
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Location of the main configuration file; either the path to the config or its containing directory ("-" for stdin). Can be used multiple times and inside other configuration files
- metavar(표시 이름): PATH---

## 17 (1-17): --plugin-dirs
- short: []
- long: ['--plugin-dirs']
- dest(저장변수명): plugin_dirs
- default: ['default']
- type: string
- choices: None
- help: Path to an additional directory to search for plugins. This option can be used multiple times to add multiple directories. Use "default" to search the default plugin directories (default)
- metavar(표시 이름): DIR---

## 18 (1-18): --no-plugin-dirs
- short: []
- long: ['--no-plugin-dirs']
- dest(저장변수명): plugin_dirs
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Clear plugin directories to search, including defaults and those provided by previous --plugin-dirs
- metavar(표시 이름): None---

## 19 (1-19): --js-runtimes
- short: []
- long: ['--js-runtimes']
- dest(저장변수명): js_runtimes
- default: ['deno']
- type: string
- choices: None
- help: Additional JavaScript runtime to enable, with an optional location for the runtime (either the path to the binary or its containing directory). This option can be used multiple times to enable multiple runtimes. Supported runtimes are (in order of priority, from highest to lowest): deno, node, quickjs, bun. Only "deno" is enabled by default. The highest priority runtime that is both enabled and available will be used. In order to use a lower priority runtime when "deno" is available, --no-js-runtimes needs to be passed before enabling other runtimes
- metavar(표시 이름): RUNTIME[:PATH]---

## 20 (1-20): --no-js-runtimes
- short: []
- long: ['--no-js-runtimes']
- dest(저장변수명): js_runtimes
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Clear JavaScript runtimes to enable, including defaults and those provided by previous --js-runtimes
- metavar(표시 이름): None---

## 21 (1-21): --remote-components
- short: []
- long: ['--remote-components']
- dest(저장변수명): remote_components
- default: []
- type: string
- choices: None
- help: Remote components to allow yt-dlp to fetch when required. This option is currently not needed if you are using an official executable or have the requisite version of the yt-dlp-ejs package installed. You can use this option multiple times to allow multiple components. Supported values: ejs:npm (external JavaScript components from npm), ejs:github (external JavaScript components from yt-dlp-ejs GitHub). By default, no remote components are allowed
- metavar(표시 이름): COMPONENT---

## 22 (1-22): --no-remote-components
- short: []
- long: ['--no-remote-components']
- dest(저장변수명): remote_components
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Disallow fetching of all remote components, including any previously allowed by --remote-components or defaults.
- metavar(표시 이름): None---

## 23 (1-23): --flat-playlist
- short: []
- long: ['--flat-playlist']
- dest(저장변수명): extract_flat
- default: False
- type: None
- choices: None
- help: Do not extract a playlist's URL result entries; some entry metadata may be missing and downloading may be bypassed
- metavar(표시 이름): None---

## 24 (1-24): --no-flat-playlist
- short: []
- long: ['--no-flat-playlist']
- dest(저장변수명): extract_flat
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Fully extract the videos of a playlist (default)
- metavar(표시 이름): None---

## 25 (1-25): --live-from-start
- short: []
- long: ['--live-from-start']
- dest(저장변수명): live_from_start
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Download livestreams from the start. Currently experimental and only supported for YouTube, Twitch, and TVer
- metavar(표시 이름): None---

## 26 (1-26): --no-live-from-start
- short: []
- long: ['--no-live-from-start']
- dest(저장변수명): live_from_start
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Download livestreams from the current time (default)
- metavar(표시 이름): None---

## 27 (1-27): --wait-for-video
- short: []
- long: ['--wait-for-video']
- dest(저장변수명): wait_for_video
- default: None
- type: string
- choices: None
- help: Wait for scheduled streams to become available. Pass the minimum number of seconds (or range) to wait between retries
- metavar(표시 이름): MIN[-MAX]---

## 28 (1-28): --no-wait-for-video
- short: []
- long: ['--no-wait-for-video']
- dest(저장변수명): wait_for_video
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not wait for scheduled streams (default)
- metavar(표시 이름): None---

## 29 (1-29): --mark-watched
- short: []
- long: ['--mark-watched']
- dest(저장변수명): mark_watched
- default: False
- type: None
- choices: None
- help: Mark videos watched (even with --simulate)
- metavar(표시 이름): None---

## 30 (1-30): --no-mark-watched
- short: []
- long: ['--no-mark-watched']
- dest(저장변수명): mark_watched
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not mark videos watched (default)
- metavar(표시 이름): None---

## 31 (1-31): --no-colors/--no-colours
- short: []
- long: ['--no-colors', '--no-colours']
- dest(저장변수명): color
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 32 (1-32): --color
- short: []
- long: ['--color']
- dest(저장변수명): color
- default: {}
- type: string
- choices: None
- help: Whether to emit color codes in output, optionally prefixed by the STREAM (stdout or stderr) to apply the setting to. Can be one of "always", "auto" (default), "never", or "no_color" (use non color terminal sequences). Use "auto-tty" or "no_color-tty" to decide based on terminal support only. Can be used multiple times
- metavar(표시 이름): [STREAM:]POLICY---

## 33 (1-33): --compat-options
- short: []
- long: ['--compat-options']
- dest(저장변수명): compat_opts
- default: set()
- type: string
- choices: None
- help: Options that can help keep compatibility with youtube-dl or youtube-dlc configurations by reverting some of the changes made in yt-dlp. See "Differences in default behavior" for details
- metavar(표시 이름): OPTS---

## 34 (1-34): --alias
- short: []
- long: ['--alias']
- dest(저장변수명): _
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Create aliases for an option string. Unless an alias starts with a dash "-", it is prefixed with "--". Arguments are parsed according to the Python string formatting mini-language. E.g. --alias get-audio,-X "-S aext:{0},abr -x --audio-format {0}" creates options "--get-audio" and "-X" that takes an argument (ARG0) and expands to "-S aext:ARG0,abr -x --audio-format ARG0". All defined aliases are listed in the --help output. Alias options can trigger more aliases; so be careful to avoid defining recursive options. As a safety measure, each alias may be triggered a maximum of 100 times. This option can be used multiple times
- metavar(표시 이름): ALIASES OPTIONS---

## 35 (1-35): -t/--preset-alias
- short: ['-t']
- long: ['--preset-alias']
- dest(저장변수명): _
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Applies a predefined set of options. e.g. --preset-alias mp3. The following presets are available: mp3, aac, mp4, mkv, sleep. See the "Preset Aliases" section at the end for more info. This option can be used multiple times
- metavar(표시 이름): PRESET---

# 2. Network Options: 8개 옵션
## 36 (2-1): --proxy
- short: []
- long: ['--proxy']
- dest(저장변수명): proxy
- default: None
- type: string
- choices: None
- help: Use the specified HTTP/HTTPS/SOCKS proxy. To enable SOCKS proxy, specify a proper scheme, e.g. socks5://user:pass@127.0.0.1:1080/. Pass in an empty string (--proxy "") for direct connection
- metavar(표시 이름): URL---

## 37 (2-2): --socket-timeout
- short: []
- long: ['--socket-timeout']
- dest(저장변수명): socket_timeout
- default: None
- type: float
- choices: None
- help: Time to wait before giving up, in seconds
- metavar(표시 이름): SECONDS---

## 38 (2-3): --source-address
- short: []
- long: ['--source-address']
- dest(저장변수명): source_address
- default: None
- type: string
- choices: None
- help: Client-side IP address to bind to
- metavar(표시 이름): IP---

## 39 (2-4): --impersonate
- short: []
- long: ['--impersonate']
- dest(저장변수명): impersonate
- default: None
- type: string
- choices: None
- help: Client to impersonate for requests. E.g. chrome, chrome-110, chrome:windows-10. Pass --impersonate="" to impersonate any client. Note that forcing impersonation for all requests may have a detrimental impact on download speed and stability
- metavar(표시 이름): CLIENT[:OS]---

## 40 (2-5): --list-impersonate-targets
- short: []
- long: ['--list-impersonate-targets']
- dest(저장변수명): list_impersonate_targets
- default: False
- type: None
- choices: None
- help: List available clients to impersonate.
- metavar(표시 이름): None---

## 41 (2-6): -4/--force-ipv4
- short: ['-4']
- long: ['--force-ipv4']
- dest(저장변수명): source_address
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Make all connections via IPv4
- metavar(표시 이름): None---

## 42 (2-7): -6/--force-ipv6
- short: ['-6']
- long: ['--force-ipv6']
- dest(저장변수명): source_address
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Make all connections via IPv6
- metavar(표시 이름): None---

## 43 (2-8): --enable-file-urls
- short: []
- long: ['--enable-file-urls']
- dest(저장변수명): enable_file_urls
- default: False
- type: None
- choices: None
- help: Enable file:// URLs. This is disabled by default for security reasons.
- metavar(표시 이름): None---

# 3. Geo-restriction: 6개 옵션
## 44 (3-1): --geo-verification-proxy
- short: []
- long: ['--geo-verification-proxy']
- dest(저장변수명): geo_verification_proxy
- default: None
- type: string
- choices: None
- help: Use this proxy to verify the IP address for some geo-restricted sites. The default proxy specified by --proxy (or none, if the option is not present) is used for the actual downloading
- metavar(표시 이름): URL---

## 45 (3-2): --xff
- short: []
- long: ['--xff']
- dest(저장변수명): geo_bypass
- default: default
- type: string
- choices: None
- help: How to fake X-Forwarded-For HTTP header to try bypassing geographic restriction. One of "default" (only when known to be useful), "never", an IP block in CIDR notation, or a two-letter ISO 3166-2 country code
- metavar(표시 이름): VALUE---

## 46 (3-3): --geo-bypass
- short: []
- long: ['--geo-bypass']
- dest(저장변수명): geo_bypass
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 47 (3-4): --no-geo-bypass
- short: []
- long: ['--no-geo-bypass']
- dest(저장변수명): geo_bypass
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 48 (3-5): --geo-bypass-country
- short: []
- long: ['--geo-bypass-country']
- dest(저장변수명): geo_bypass
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): CODE---

## 49 (3-6): --geo-bypass-ip-block
- short: []
- long: ['--geo-bypass-ip-block']
- dest(저장변수명): geo_bypass
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): IP_BLOCK---

# 4. Video Selection: 28개 옵션
## 50 (4-1): --playlist-start
- short: []
- long: ['--playlist-start']
- dest(저장변수명): playliststart
- default: 1
- type: int
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): NUMBER---

## 51 (4-2): --playlist-end
- short: []
- long: ['--playlist-end']
- dest(저장변수명): playlistend
- default: None
- type: int
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): NUMBER---

## 52 (4-3): -I/--playlist-items
- short: ['-I']
- long: ['--playlist-items']
- dest(저장변수명): playlist_items
- default: None
- type: string
- choices: None
- help: Comma-separated playlist_index of the items to download. You can specify a range using "[START]:[STOP][:STEP]". For backward compatibility, START-STOP is also supported. Use negative indices to count from the right and negative STEP to download in reverse order. E.g. "-I 1:3,7,-5::2" used on a playlist of size 15 will download the items at index 1,2,3,7,11,13,15
- metavar(표시 이름): ITEM_SPEC---

## 53 (4-4): --match-title
- short: []
- long: ['--match-title']
- dest(저장변수명): matchtitle
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): REGEX---

## 54 (4-5): --reject-title
- short: []
- long: ['--reject-title']
- dest(저장변수명): rejecttitle
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): REGEX---

## 55 (4-6): --min-filesize
- short: []
- long: ['--min-filesize']
- dest(저장변수명): min_filesize
- default: None
- type: string
- choices: None
- help: Abort download if filesize is smaller than SIZE, e.g. 50k or 44.6M
- metavar(표시 이름): SIZE---

## 56 (4-7): --max-filesize
- short: []
- long: ['--max-filesize']
- dest(저장변수명): max_filesize
- default: None
- type: string
- choices: None
- help: Abort download if filesize is larger than SIZE, e.g. 50k or 44.6M
- metavar(표시 이름): SIZE---

## 57 (4-8): --date
- short: []
- long: ['--date']
- dest(저장변수명): date
- default: None
- type: string
- choices: None
- help: Download only videos uploaded on this date. The date can be "YYYYMMDD" or in the format [now|today|yesterday][-N[day|week|month|year]]. E.g. "--date today-2weeks" downloads only videos uploaded on the same day two weeks ago
- metavar(표시 이름): DATE---

## 58 (4-9): --datebefore
- short: []
- long: ['--datebefore']
- dest(저장변수명): datebefore
- default: None
- type: string
- choices: None
- help: Download only videos uploaded on or before this date. The date formats accepted are the same as --date
- metavar(표시 이름): DATE---

## 59 (4-10): --dateafter
- short: []
- long: ['--dateafter']
- dest(저장변수명): dateafter
- default: None
- type: string
- choices: None
- help: Download only videos uploaded on or after this date. The date formats accepted are the same as --date
- metavar(표시 이름): DATE---

## 60 (4-11): --min-views
- short: []
- long: ['--min-views']
- dest(저장변수명): min_views
- default: None
- type: int
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): COUNT---

## 61 (4-12): --max-views
- short: []
- long: ['--max-views']
- dest(저장변수명): max_views
- default: None
- type: int
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): COUNT---

## 62 (4-13): --match-filters
- short: []
- long: ['--match-filters']
- dest(저장변수명): match_filter
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Generic video filter. Any "OUTPUT TEMPLATE" field can be compared with a number or a string using the operators defined in "Filtering Formats". You can also simply specify a field to match if the field is present, use "!field" to check if the field is not present, and "&" to check multiple conditions. Use a "\" to escape "&" or quotes if needed. If used multiple times, the filter matches if at least one of the conditions is met. E.g. --match-filters !is_live --match-filters "like_count>?100 & description~='(?i)\bcats \& dogs\b'" matches only videos that are not live OR those that have a like count more than 100 (or the like field is not available) and also has a description that contains the phrase "cats & dogs" (caseless). Use "--match-filters -" to interactively ask whether to download each video
- metavar(표시 이름): FILTER---

## 63 (4-14): --no-match-filters
- short: []
- long: ['--no-match-filters']
- dest(저장변수명): match_filter
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not use any --match-filters (default)
- metavar(표시 이름): None---

## 64 (4-15): --break-match-filters
- short: []
- long: ['--break-match-filters']
- dest(저장변수명): breaking_match_filter
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Same as "--match-filters" but stops the download process when a video is rejected
- metavar(표시 이름): FILTER---

## 65 (4-16): --no-break-match-filters
- short: []
- long: ['--no-break-match-filters']
- dest(저장변수명): breaking_match_filter
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not use any --break-match-filters (default)
- metavar(표시 이름): None---

## 66 (4-17): --no-playlist
- short: []
- long: ['--no-playlist']
- dest(저장변수명): noplaylist
- default: False
- type: None
- choices: None
- help: Download only the video, if the URL refers to a video and a playlist
- metavar(표시 이름): None---

## 67 (4-18): --yes-playlist
- short: []
- long: ['--yes-playlist']
- dest(저장변수명): noplaylist
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Download the playlist, if the URL refers to a video and a playlist
- metavar(표시 이름): None---

## 68 (4-19): --age-limit
- short: []
- long: ['--age-limit']
- dest(저장변수명): age_limit
- default: None
- type: int
- choices: None
- help: Download only videos suitable for the given age
- metavar(표시 이름): YEARS---

## 69 (4-20): --download-archive
- short: []
- long: ['--download-archive']
- dest(저장변수명): download_archive
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Download only videos not listed in the archive file. Record the IDs of all downloaded videos in it
- metavar(표시 이름): FILE---

## 70 (4-21): --no-download-archive
- short: []
- long: ['--no-download-archive']
- dest(저장변수명): download_archive
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not use archive file (default)
- metavar(표시 이름): None---

## 71 (4-22): --max-downloads
- short: []
- long: ['--max-downloads']
- dest(저장변수명): max_downloads
- default: None
- type: int
- choices: None
- help: Abort after downloading NUMBER files
- metavar(표시 이름): NUMBER---

## 72 (4-23): --break-on-existing
- short: []
- long: ['--break-on-existing']
- dest(저장변수명): break_on_existing
- default: False
- type: None
- choices: None
- help: Stop the download process when encountering a file that is in the archive supplied with the --download-archive option
- metavar(표시 이름): None---

## 73 (4-24): --no-break-on-existing
- short: []
- long: ['--no-break-on-existing']
- dest(저장변수명): break_on_existing
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not stop the download process when encountering a file that is in the archive (default)
- metavar(표시 이름): None---

## 74 (4-25): --break-on-reject
- short: []
- long: ['--break-on-reject']
- dest(저장변수명): break_on_reject
- default: False
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 75 (4-26): --break-per-input
- short: []
- long: ['--break-per-input']
- dest(저장변수명): break_per_url
- default: False
- type: None
- choices: None
- help: Alters --max-downloads, --break-on-existing, --break-match-filters, and autonumber to reset per input URL
- metavar(표시 이름): None---

## 76 (4-27): --no-break-per-input
- short: []
- long: ['--no-break-per-input']
- dest(저장변수명): break_per_url
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: --break-on-existing and similar options terminates the entire download queue
- metavar(표시 이름): None---

## 77 (4-28): --skip-playlist-after-errors
- short: []
- long: ['--skip-playlist-after-errors']
- dest(저장변수명): skip_playlist_after_errors
- default: None
- type: int
- choices: None
- help: Number of allowed failures until the rest of the playlist is skipped
- metavar(표시 이름): N---

# 5. Download Options: 28개 옵션
## 78 (5-1): -N/--concurrent-fragments
- short: ['-N']
- long: ['--concurrent-fragments']
- dest(저장변수명): concurrent_fragment_downloads
- default: 1
- type: int
- choices: None
- help: Number of fragments of a dash/hlsnative video that should be downloaded concurrently (default is %default)
- metavar(표시 이름): N---

## 79 (5-2): -r/--limit-rate/--rate-limit
- short: ['-r']
- long: ['--limit-rate', '--rate-limit']
- dest(저장변수명): ratelimit
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Maximum download rate in bytes per second, e.g. 50K or 4.2M
- metavar(표시 이름): RATE---

## 80 (5-3): --throttled-rate
- short: []
- long: ['--throttled-rate']
- dest(저장변수명): throttledratelimit
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Minimum download rate in bytes per second below which throttling is assumed and the video data is re-extracted, e.g. 100K
- metavar(표시 이름): RATE---

## 81 (5-4): -R/--retries
- short: ['-R']
- long: ['--retries']
- dest(저장변수명): retries
- default: 10
- type: string
- choices: None
- help: Number of retries (default is %default), or "infinite"
- metavar(표시 이름): RETRIES---

## 82 (5-5): --file-access-retries
- short: []
- long: ['--file-access-retries']
- dest(저장변수명): file_access_retries
- default: 3
- type: string
- choices: None
- help: Number of times to retry on file access error (default is %default), or "infinite"
- metavar(표시 이름): RETRIES---

## 83 (5-6): --fragment-retries
- short: []
- long: ['--fragment-retries']
- dest(저장변수명): fragment_retries
- default: 10
- type: string
- choices: None
- help: Number of retries for a fragment (default is %default), or "infinite" (DASH, hlsnative and ISM)
- metavar(표시 이름): RETRIES---

## 84 (5-7): --retry-sleep
- short: []
- long: ['--retry-sleep']
- dest(저장변수명): retry_sleep
- default: {}
- type: string
- choices: None
- help: Time to sleep between retries in seconds (optionally) prefixed by the type of retry (http (default), fragment, file_access, extractor) to apply the sleep to. EXPR can be a number, linear=START[:END[:STEP=1]] or exp=START[:END[:BASE=2]]. This option can be used multiple times to set the sleep for the different retry types, e.g. --retry-sleep linear=1::2 --retry-sleep fragment:exp=1:20
- metavar(표시 이름): [TYPE:]EXPR---

## 85 (5-8): --skip-unavailable-fragments/--no-abort-on-unavailable-fragments
- short: []
- long: ['--skip-unavailable-fragments', '--no-abort-on-unavailable-fragments']
- dest(저장변수명): skip_unavailable_fragments
- default: True
- type: None
- choices: None
- help: Skip unavailable fragments for DASH, hlsnative and ISM downloads (default) (Alias: --no-abort-on-unavailable-fragments)
- metavar(표시 이름): None---

## 86 (5-9): --abort-on-unavailable-fragments/--no-skip-unavailable-fragments
- short: []
- long: ['--abort-on-unavailable-fragments', '--no-skip-unavailable-fragments']
- dest(저장변수명): skip_unavailable_fragments
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Abort download if a fragment is unavailable (Alias: --no-skip-unavailable-fragments)
- metavar(표시 이름): None---

## 87 (5-10): --keep-fragments
- short: []
- long: ['--keep-fragments']
- dest(저장변수명): keep_fragments
- default: False
- type: None
- choices: None
- help: Keep downloaded fragments on disk after downloading is finished
- metavar(표시 이름): None---

## 88 (5-11): --no-keep-fragments
- short: []
- long: ['--no-keep-fragments']
- dest(저장변수명): keep_fragments
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Delete downloaded fragments after downloading is finished (default)
- metavar(표시 이름): None---

## 89 (5-12): --buffer-size
- short: []
- long: ['--buffer-size']
- dest(저장변수명): buffersize
- default: 1024
- type: string
- choices: None
- help: Size of download buffer, e.g. 1024 or 16K (default is %default)
- metavar(표시 이름): SIZE---

## 90 (5-13): --resize-buffer
- short: []
- long: ['--resize-buffer']
- dest(저장변수명): noresizebuffer
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: The buffer size is automatically resized from an initial value of --buffer-size (default)
- metavar(표시 이름): None---

## 91 (5-14): --no-resize-buffer
- short: []
- long: ['--no-resize-buffer']
- dest(저장변수명): noresizebuffer
- default: False
- type: None
- choices: None
- help: Do not automatically adjust the buffer size
- metavar(표시 이름): None---

## 92 (5-15): --http-chunk-size
- short: []
- long: ['--http-chunk-size']
- dest(저장변수명): http_chunk_size
- default: None
- type: string
- choices: None
- help: Size of a chunk for chunk-based HTTP downloading, e.g. 10485760 or 10M (default is disabled). May be useful for bypassing bandwidth throttling imposed by a webserver (experimental)
- metavar(표시 이름): SIZE---

## 93 (5-16): --test
- short: []
- long: ['--test']
- dest(저장변수명): test
- default: False
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 94 (5-17): --playlist-reverse
- short: []
- long: ['--playlist-reverse']
- dest(저장변수명): playlist_reverse
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 95 (5-18): --no-playlist-reverse
- short: []
- long: ['--no-playlist-reverse']
- dest(저장변수명): playlist_reverse
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 96 (5-19): --playlist-random
- short: []
- long: ['--playlist-random']
- dest(저장변수명): playlist_random
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Download playlist videos in random order
- metavar(표시 이름): None---

## 97 (5-20): --lazy-playlist
- short: []
- long: ['--lazy-playlist']
- dest(저장변수명): lazy_playlist
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Process entries in the playlist as they are received. This disables n_entries, --playlist-random and --playlist-reverse
- metavar(표시 이름): None---

## 98 (5-21): --no-lazy-playlist
- short: []
- long: ['--no-lazy-playlist']
- dest(저장변수명): lazy_playlist
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Process videos in the playlist only after the entire playlist is parsed (default)
- metavar(표시 이름): None---

## 99 (5-22): --hls-prefer-native
- short: []
- long: ['--hls-prefer-native']
- dest(저장변수명): hls_prefer_native
- default: None
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 100 (5-23): --hls-prefer-ffmpeg
- short: []
- long: ['--hls-prefer-ffmpeg']
- dest(저장변수명): hls_prefer_native
- default: None
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 101 (5-24): --hls-use-mpegts
- short: []
- long: ['--hls-use-mpegts']
- dest(저장변수명): hls_use_mpegts
- default: None
- type: None
- choices: None
- help: Use the mpegts container for HLS videos; allowing some players to play the video while downloading, and reducing the chance of file corruption if download is interrupted. This is enabled by default for live streams
- metavar(표시 이름): None---

## 102 (5-25): --no-hls-use-mpegts
- short: []
- long: ['--no-hls-use-mpegts']
- dest(저장변수명): hls_use_mpegts
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not use the mpegts container for HLS videos. This is default when not downloading live streams
- metavar(표시 이름): None---

## 103 (5-26): --download-sections
- short: []
- long: ['--download-sections']
- dest(저장변수명): download_ranges
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Download only chapters that match the regular expression. A "*" prefix denotes time-range instead of chapter. Negative timestamps are calculated from the end. "*from-url" can be used to download between the "start_time" and "end_time" extracted from the URL. Needs ffmpeg. This option can be used multiple times to download multiple sections, e.g. --download-sections "*10:15-inf" --download-sections "intro"
- metavar(표시 이름): REGEX---

## 104 (5-27): --downloader/--external-downloader
- short: []
- long: ['--downloader', '--external-downloader']
- dest(저장변수명): external_downloader
- default: {}
- type: string
- choices: None
- help: Name or path of the external downloader to use (optionally) prefixed by the protocols (http, ftp, m3u8, dash, rstp, rtmp, mms) to use it for. Currently supports native, aria2c, axel, curl, ffmpeg, httpie, wget. You can use this option multiple times to set different downloaders for different protocols. E.g. --downloader aria2c --downloader "dash,m3u8:native" will use aria2c for http/ftp downloads, and the native downloader for dash/m3u8 downloads (Alias: --external-downloader)
- metavar(표시 이름): [PROTO:]NAME---

## 105 (5-28): --downloader-args/--external-downloader-args
- short: []
- long: ['--downloader-args', '--external-downloader-args']
- dest(저장변수명): external_downloader_args
- default: {}
- type: string
- choices: None
- help: Give these arguments to the external downloader. Specify the downloader name and the arguments separated by a colon ":". For ffmpeg, arguments can be passed to different positions using the same syntax as --postprocessor-args. You can use this option multiple times to give different arguments to different downloaders (Alias: --external-downloader-args)
- metavar(표시 이름): NAME:ARGS---

# 6. Filesystem Options: 40개 옵션
## 106 (6-1): -a/--batch-file
- short: ['-a']
- long: ['--batch-file']
- dest(저장변수명): batchfile
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: File containing URLs to download ("-" for stdin), one URL per line. Lines starting with "#", ";" or "]" are considered as comments and ignored
- metavar(표시 이름): FILE---

## 107 (6-2): --no-batch-file
- short: []
- long: ['--no-batch-file']
- dest(저장변수명): batchfile
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not read URLs from batch file (default)
- metavar(표시 이름): None---

## 108 (6-3): --id
- short: []
- long: ['--id']
- dest(저장변수명): useid
- default: False
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 109 (6-4): -P/--paths
- short: ['-P']
- long: ['--paths']
- dest(저장변수명): paths
- default: {}
- type: string
- choices: None
- help: The paths where the files should be downloaded. Specify the type of file and the path separated by a colon ":". All the same TYPES as --output are supported. Additionally, you can also provide "home" (default) and "temp" paths. All intermediary files are first downloaded to the temp path and then the final files are moved over to the home path after download is finished. This option is ignored if --output is an absolute path
- metavar(표시 이름): [TYPES:]PATH---

## 110 (6-5): -o/--output
- short: ['-o']
- long: ['--output']
- dest(저장변수명): outtmpl
- default: {}
- type: string
- choices: None
- help: Output filename template; see "OUTPUT TEMPLATE" for details
- metavar(표시 이름): [TYPES:]TEMPLATE---

## 111 (6-6): --output-na-placeholder
- short: []
- long: ['--output-na-placeholder']
- dest(저장변수명): outtmpl_na_placeholder
- default: NA
- type: string
- choices: None
- help: Placeholder for unavailable fields in --output (default: "%default")
- metavar(표시 이름): TEXT---

## 112 (6-7): --autonumber-size
- short: []
- long: ['--autonumber-size']
- dest(저장변수명): autonumber_size
- default: ('NO', 'DEFAULT')
- type: int
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): NUMBER---

## 113 (6-8): --autonumber-start
- short: []
- long: ['--autonumber-start']
- dest(저장변수명): autonumber_start
- default: 1
- type: int
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): NUMBER---

## 114 (6-9): --restrict-filenames
- short: []
- long: ['--restrict-filenames']
- dest(저장변수명): restrictfilenames
- default: False
- type: None
- choices: None
- help: Restrict filenames to only ASCII characters, and avoid "&" and spaces in filenames
- metavar(표시 이름): None---

## 115 (6-10): --no-restrict-filenames
- short: []
- long: ['--no-restrict-filenames']
- dest(저장변수명): restrictfilenames
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Allow Unicode characters, "&" and spaces in filenames (default)
- metavar(표시 이름): None---

## 116 (6-11): --windows-filenames
- short: []
- long: ['--windows-filenames']
- dest(저장변수명): windowsfilenames
- default: None
- type: None
- choices: None
- help: Force filenames to be Windows-compatible
- metavar(표시 이름): None---

## 117 (6-12): --no-windows-filenames
- short: []
- long: ['--no-windows-filenames']
- dest(저장변수명): windowsfilenames
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Sanitize filenames only minimally
- metavar(표시 이름): None---

## 118 (6-13): --trim-filenames/--trim-file-names
- short: []
- long: ['--trim-filenames', '--trim-file-names']
- dest(저장변수명): trim_file_name
- default: 0
- type: int
- choices: None
- help: Limit the filename length (excluding extension) to the specified number of characters
- metavar(표시 이름): LENGTH---

## 119 (6-14): -w/--no-overwrites
- short: ['-w']
- long: ['--no-overwrites']
- dest(저장변수명): overwrites
- default: None
- type: None
- choices: None
- help: Do not overwrite any files
- metavar(표시 이름): None---

## 120 (6-15): --force-overwrites/--yes-overwrites
- short: []
- long: ['--force-overwrites', '--yes-overwrites']
- dest(저장변수명): overwrites
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Overwrite all video and metadata files. This option includes --no-continue
- metavar(표시 이름): None---

## 121 (6-16): --no-force-overwrites
- short: []
- long: ['--no-force-overwrites']
- dest(저장변수명): overwrites
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not overwrite the video, but overwrite related files (default)
- metavar(표시 이름): None---

## 122 (6-17): -c/--continue
- short: ['-c']
- long: ['--continue']
- dest(저장변수명): continue_dl
- default: True
- type: None
- choices: None
- help: Resume partially downloaded files/fragments (default)
- metavar(표시 이름): None---

## 123 (6-18): --no-continue
- short: []
- long: ['--no-continue']
- dest(저장변수명): continue_dl
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not resume partially downloaded fragments. If the file is not fragmented, restart download of the entire file
- metavar(표시 이름): None---

## 124 (6-19): --part
- short: []
- long: ['--part']
- dest(저장변수명): nopart
- default: False
- type: None
- choices: None
- help: Use .part files instead of writing directly into output file (default)
- metavar(표시 이름): None---

## 125 (6-20): --no-part
- short: []
- long: ['--no-part']
- dest(저장변수명): nopart
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not use .part files - write directly into output file
- metavar(표시 이름): None---

## 126 (6-21): --mtime
- short: []
- long: ['--mtime']
- dest(저장변수명): updatetime
- default: None
- type: None
- choices: None
- help: Use the Last-modified header to set the file modification time
- metavar(표시 이름): None---

## 127 (6-22): --no-mtime
- short: []
- long: ['--no-mtime']
- dest(저장변수명): updatetime
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not use the Last-modified header to set the file modification time (default)
- metavar(표시 이름): None---

## 128 (6-23): --write-description
- short: []
- long: ['--write-description']
- dest(저장변수명): writedescription
- default: False
- type: None
- choices: None
- help: Write video description to a .description file
- metavar(표시 이름): None---

## 129 (6-24): --no-write-description
- short: []
- long: ['--no-write-description']
- dest(저장변수명): writedescription
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not write video description (default)
- metavar(표시 이름): None---

## 130 (6-25): --write-info-json
- short: []
- long: ['--write-info-json']
- dest(저장변수명): writeinfojson
- default: None
- type: None
- choices: None
- help: Write video metadata to a .info.json file (this may contain personal information)
- metavar(표시 이름): None---

## 131 (6-26): --no-write-info-json
- short: []
- long: ['--no-write-info-json']
- dest(저장변수명): writeinfojson
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not write video metadata (default)
- metavar(표시 이름): None---

## 132 (6-27): --write-playlist-metafiles
- short: []
- long: ['--write-playlist-metafiles']
- dest(저장변수명): allow_playlist_files
- default: None
- type: None
- choices: None
- help: Write playlist metadata in addition to the video metadata when using --write-info-json, --write-description etc. (default)
- metavar(표시 이름): None---

## 133 (6-28): --no-write-playlist-metafiles
- short: []
- long: ['--no-write-playlist-metafiles']
- dest(저장변수명): allow_playlist_files
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not write playlist metadata when using --write-info-json, --write-description etc.
- metavar(표시 이름): None---

## 134 (6-29): --clean-info-json/--clean-infojson
- short: []
- long: ['--clean-info-json', '--clean-infojson']
- dest(저장변수명): clean_infojson
- default: None
- type: None
- choices: None
- help: Remove some internal metadata such as filenames from the infojson (default)
- metavar(표시 이름): None---

## 135 (6-30): --no-clean-info-json/--no-clean-infojson
- short: []
- long: ['--no-clean-info-json', '--no-clean-infojson']
- dest(저장변수명): clean_infojson
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Write all fields to the infojson
- metavar(표시 이름): None---

## 136 (6-31): --write-comments/--get-comments
- short: []
- long: ['--write-comments', '--get-comments']
- dest(저장변수명): getcomments
- default: False
- type: None
- choices: None
- help: Retrieve video comments to be placed in the infojson. The comments are fetched even without this option if the extraction is known to be quick (Alias: --get-comments)
- metavar(표시 이름): None---

## 137 (6-32): --no-write-comments/--no-get-comments
- short: []
- long: ['--no-write-comments', '--no-get-comments']
- dest(저장변수명): getcomments
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not retrieve video comments unless the extraction is known to be quick (Alias: --no-get-comments)
- metavar(표시 이름): None---

## 138 (6-33): --load-info-json
- short: []
- long: ['--load-info-json']
- dest(저장변수명): load_info_filename
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: JSON file containing the video information (created with the "--write-info-json" option)
- metavar(표시 이름): FILE---

## 139 (6-34): --cookies
- short: []
- long: ['--cookies']
- dest(저장변수명): cookiefile
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Netscape formatted file to read cookies from and dump cookie jar in
- metavar(표시 이름): FILE---

## 140 (6-35): --no-cookies
- short: []
- long: ['--no-cookies']
- dest(저장변수명): cookiefile
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not read/dump cookies from/to file (default)
- metavar(표시 이름): FILE---

## 141 (6-36): --cookies-from-browser
- short: []
- long: ['--cookies-from-browser']
- dest(저장변수명): cookiesfrombrowser
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: The name of the browser to load cookies from. Currently supported browsers are: brave, chrome, chromium, edge, firefox, opera, safari, vivaldi, whale. Optionally, the KEYRING used for decrypting Chromium cookies on Linux, the name/path of the PROFILE to load cookies from, and the CONTAINER name (if Firefox) ("none" for no container) can be given with their respective separators. By default, all containers of the most recently accessed profile are used. Currently supported keyrings are: basictext, gnomekeyring, kwallet, kwallet5, kwallet6
- metavar(표시 이름): BROWSER[+KEYRING][:PROFILE][::CONTAINER]---

## 142 (6-37): --no-cookies-from-browser
- short: []
- long: ['--no-cookies-from-browser']
- dest(저장변수명): cookiesfrombrowser
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not load cookies from browser (default)
- metavar(표시 이름): None---

## 143 (6-38): --cache-dir
- short: []
- long: ['--cache-dir']
- dest(저장변수명): cachedir
- default: None
- type: string
- choices: None
- help: Location in the filesystem where yt-dlp can store some downloaded information (such as client ids and signatures) permanently. By default ${XDG_CACHE_HOME}/yt-dlp
- metavar(표시 이름): DIR---

## 144 (6-39): --no-cache-dir
- short: []
- long: ['--no-cache-dir']
- dest(저장변수명): cachedir
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Disable filesystem caching
- metavar(표시 이름): None---

## 145 (6-40): --rm-cache-dir
- short: []
- long: ['--rm-cache-dir']
- dest(저장변수명): rm_cachedir
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Delete all filesystem cache files
- metavar(표시 이름): None---

# 7. Thumbnail Options: 4개 옵션
## 146 (7-1): --write-thumbnail
- short: []
- long: ['--write-thumbnail']
- dest(저장변수명): writethumbnail
- default: False
- type: None
- choices: None
- help: Write thumbnail image to disk
- metavar(표시 이름): None---

## 147 (7-2): --no-write-thumbnail
- short: []
- long: ['--no-write-thumbnail']
- dest(저장변수명): writethumbnail
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not write thumbnail image to disk (default)
- metavar(표시 이름): None---

## 148 (7-3): --write-all-thumbnails
- short: []
- long: ['--write-all-thumbnails']
- dest(저장변수명): writethumbnail
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Write all thumbnail image formats to disk
- metavar(표시 이름): None---

## 149 (7-4): --list-thumbnails
- short: []
- long: ['--list-thumbnails']
- dest(저장변수명): list_thumbnails
- default: False
- type: None
- choices: None
- help: List available thumbnails of each video. Simulate unless --no-simulate is used
- metavar(표시 이름): None---

# 8. Internet Shortcut Options: 4개 옵션
## 150 (8-1): --write-link
- short: []
- long: ['--write-link']
- dest(저장변수명): writelink
- default: False
- type: None
- choices: None
- help: Write an internet shortcut file, depending on the current platform (.url, .webloc or .desktop). The URL may be cached by the OS
- metavar(표시 이름): None---

## 151 (8-2): --write-url-link
- short: []
- long: ['--write-url-link']
- dest(저장변수명): writeurllink
- default: False
- type: None
- choices: None
- help: Write a .url Windows internet shortcut. The OS caches the URL based on the file path
- metavar(표시 이름): None---

## 152 (8-3): --write-webloc-link
- short: []
- long: ['--write-webloc-link']
- dest(저장변수명): writewebloclink
- default: False
- type: None
- choices: None
- help: Write a .webloc macOS internet shortcut
- metavar(표시 이름): None---

## 153 (8-4): --write-desktop-link
- short: []
- long: ['--write-desktop-link']
- dest(저장변수명): writedesktoplink
- default: False
- type: None
- choices: None
- help: Write a .desktop Linux internet shortcut
- metavar(표시 이름): None---

# 9. Verbosity and Simulation Options: 33개 옵션
## 154 (9-1): -q/--quiet
- short: ['-q']
- long: ['--quiet']
- dest(저장변수명): quiet
- default: None
- type: None
- choices: None
- help: Activate quiet mode. If used with --verbose, print the log to stderr
- metavar(표시 이름): None---

## 155 (9-2): --no-quiet
- short: []
- long: ['--no-quiet']
- dest(저장변수명): quiet
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Deactivate quiet mode. (Default)
- metavar(표시 이름): None---

## 156 (9-3): --no-warnings
- short: []
- long: ['--no-warnings']
- dest(저장변수명): no_warnings
- default: False
- type: None
- choices: None
- help: Ignore warnings
- metavar(표시 이름): None---

## 157 (9-4): -s/--simulate
- short: ['-s']
- long: ['--simulate']
- dest(저장변수명): simulate
- default: None
- type: None
- choices: None
- help: Do not download the video and do not write anything to disk
- metavar(표시 이름): None---

## 158 (9-5): --no-simulate
- short: []
- long: ['--no-simulate']
- dest(저장변수명): simulate
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Download the video even if printing/listing options are used
- metavar(표시 이름): None---

## 159 (9-6): --ignore-no-formats-error
- short: []
- long: ['--ignore-no-formats-error']
- dest(저장변수명): ignore_no_formats_error
- default: False
- type: None
- choices: None
- help: Ignore "No video formats" error. Useful for extracting metadata even if the videos are not actually available for download (experimental)
- metavar(표시 이름): None---

## 160 (9-7): --no-ignore-no-formats-error
- short: []
- long: ['--no-ignore-no-formats-error']
- dest(저장변수명): ignore_no_formats_error
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Throw error when no downloadable video formats are found (default)
- metavar(표시 이름): None---

## 161 (9-8): --skip-download/--no-download
- short: []
- long: ['--skip-download', '--no-download']
- dest(저장변수명): skip_download
- default: False
- type: None
- choices: None
- help: Do not download the video but write all related files (Alias: --no-download)
- metavar(표시 이름): None---

## 162 (9-9): -O/--print
- short: ['-O']
- long: ['--print']
- dest(저장변수명): forceprint
- default: {}
- type: string
- choices: None
- help: Field name or output template to print to screen, optionally prefixed with when to print it, separated by a ":". Supported values of "WHEN" are the same as that of --use-postprocessor (default: video). Implies --quiet. Implies --simulate unless --no-simulate or later stages of WHEN are used. This option can be used multiple times
- metavar(표시 이름): [WHEN:]TEMPLATE---

## 163 (9-10): --print-to-file
- short: []
- long: ['--print-to-file']
- dest(저장변수명): print_to_file
- default: {}
- type: string
- choices: None
- help: Append given template to the file. The values of WHEN and TEMPLATE are the same as that of --print. FILE uses the same syntax as the output template. This option can be used multiple times
- metavar(표시 이름): [WHEN:]TEMPLATE FILE---

## 164 (9-11): -g/--get-url
- short: ['-g']
- long: ['--get-url']
- dest(저장변수명): geturl
- default: False
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 165 (9-12): -e/--get-title
- short: ['-e']
- long: ['--get-title']
- dest(저장변수명): gettitle
- default: False
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 166 (9-13): --get-id
- short: []
- long: ['--get-id']
- dest(저장변수명): getid
- default: False
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 167 (9-14): --get-thumbnail
- short: []
- long: ['--get-thumbnail']
- dest(저장변수명): getthumbnail
- default: False
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 168 (9-15): --get-description
- short: []
- long: ['--get-description']
- dest(저장변수명): getdescription
- default: False
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 169 (9-16): --get-duration
- short: []
- long: ['--get-duration']
- dest(저장변수명): getduration
- default: False
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 170 (9-17): --get-filename
- short: []
- long: ['--get-filename']
- dest(저장변수명): getfilename
- default: False
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 171 (9-18): --get-format
- short: []
- long: ['--get-format']
- dest(저장변수명): getformat
- default: False
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 172 (9-19): -j/--dump-json
- short: ['-j']
- long: ['--dump-json']
- dest(저장변수명): dumpjson
- default: False
- type: None
- choices: None
- help: Quiet, but print JSON information for each video. Simulate unless --no-simulate is used. See "OUTPUT TEMPLATE" for a description of available keys
- metavar(표시 이름): None---

## 173 (9-20): -J/--dump-single-json
- short: ['-J']
- long: ['--dump-single-json']
- dest(저장변수명): dump_single_json
- default: False
- type: None
- choices: None
- help: Quiet, but print JSON information for each URL or infojson passed. Simulate unless --no-simulate is used. If the URL refers to a playlist, the whole playlist information is dumped in a single line
- metavar(표시 이름): None---

## 174 (9-21): --print-json
- short: []
- long: ['--print-json']
- dest(저장변수명): print_json
- default: False
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 175 (9-22): --force-write-archive/--force-write-download-archive/--force-download-archive
- short: []
- long: ['--force-write-archive', '--force-write-download-archive', '--force-download-archive']
- dest(저장변수명): force_write_download_archive
- default: False
- type: None
- choices: None
- help: Force download archive entries to be written as far as no errors occur, even if -s or another simulation option is used (Alias: --force-download-archive)
- metavar(표시 이름): None---

## 176 (9-23): --newline
- short: []
- long: ['--newline']
- dest(저장변수명): progress_with_newline
- default: False
- type: None
- choices: None
- help: Output progress bar as new lines
- metavar(표시 이름): None---

## 177 (9-24): --no-progress
- short: []
- long: ['--no-progress']
- dest(저장변수명): noprogress
- default: None
- type: None
- choices: None
- help: Do not print progress bar
- metavar(표시 이름): None---

## 178 (9-25): --progress
- short: []
- long: ['--progress']
- dest(저장변수명): noprogress
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Show progress bar, even if in quiet mode
- metavar(표시 이름): None---

## 179 (9-26): --console-title
- short: []
- long: ['--console-title']
- dest(저장변수명): consoletitle
- default: False
- type: None
- choices: None
- help: Display progress in console titlebar
- metavar(표시 이름): None---

## 180 (9-27): --progress-template
- short: []
- long: ['--progress-template']
- dest(저장변수명): progress_template
- default: {}
- type: string
- choices: None
- help: Template for progress outputs, optionally prefixed with one of "download:" (default), "download-title:" (the console title), "postprocess:",  or "postprocess-title:". The video's fields are accessible under the "info" key and the progress attributes are accessible under "progress" key. E.g. --console-title --progress-template "download-title:%(info.id)s-%(progress.eta)s"
- metavar(표시 이름): [TYPES:]TEMPLATE---

## 181 (9-28): --progress-delta
- short: []
- long: ['--progress-delta']
- dest(저장변수명): progress_delta
- default: 0
- type: float
- choices: None
- help: Time between progress output (default: 0)
- metavar(표시 이름): SECONDS---

## 182 (9-29): -v/--verbose
- short: ['-v']
- long: ['--verbose']
- dest(저장변수명): verbose
- default: False
- type: None
- choices: None
- help: Print various debugging information
- metavar(표시 이름): None---

## 183 (9-30): --dump-pages
- short: []
- long: ['--dump-pages']
- dest(저장변수명): dump_intermediate_pages
- default: False
- type: None
- choices: None
- help: Print downloaded pages encoded using base64 to debug problems (very verbose)
- metavar(표시 이름): None---

## 184 (9-31): --write-pages
- short: []
- long: ['--write-pages']
- dest(저장변수명): write_pages
- default: False
- type: None
- choices: None
- help: Write downloaded intermediary pages to files in the current directory to debug problems
- metavar(표시 이름): None---

## 185 (9-32): --load-pages
- short: []
- long: ['--load-pages']
- dest(저장변수명): load_pages
- default: False
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 186 (9-33): --print-traffic
- short: []
- long: ['--print-traffic']
- dest(저장변수명): debug_printtraffic
- default: False
- type: None
- choices: None
- help: Display sent and read HTTP traffic
- metavar(표시 이름): None---

# 10. Workarounds: 12개 옵션
## 187 (10-1): --encoding
- short: []
- long: ['--encoding']
- dest(저장변수명): encoding
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Force the specified encoding (experimental)
- metavar(표시 이름): ENCODING---

## 188 (10-2): --legacy-server-connect
- short: []
- long: ['--legacy-server-connect']
- dest(저장변수명): legacy_server_connect
- default: False
- type: None
- choices: None
- help: Explicitly allow HTTPS connection to servers that do not support RFC 5746 secure renegotiation
- metavar(표시 이름): None---

## 189 (10-3): --no-check-certificates
- short: []
- long: ['--no-check-certificates']
- dest(저장변수명): no_check_certificate
- default: False
- type: None
- choices: None
- help: Suppress HTTPS certificate validation
- metavar(표시 이름): None---

## 190 (10-4): --prefer-insecure/--prefer-unsecure
- short: []
- long: ['--prefer-insecure', '--prefer-unsecure']
- dest(저장변수명): prefer_insecure
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Use an unencrypted connection to retrieve information about the video (Currently supported only for YouTube)
- metavar(표시 이름): None---

## 191 (10-5): --user-agent
- short: []
- long: ['--user-agent']
- dest(저장변수명): user_agent
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): UA---

## 192 (10-6): --referer
- short: []
- long: ['--referer']
- dest(저장변수명): referer
- default: None
- type: string
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): URL---

## 193 (10-7): --add-headers
- short: []
- long: ['--add-headers']
- dest(저장변수명): headers
- default: {}
- type: string
- choices: None
- help: Specify a custom HTTP header and its value, separated by a colon ":". You can use this option multiple times
- metavar(표시 이름): FIELD:VALUE---

## 194 (10-8): --bidi-workaround
- short: []
- long: ['--bidi-workaround']
- dest(저장변수명): bidi_workaround
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Work around terminals that lack bidirectional text support. Requires bidiv or fribidi executable in PATH
- metavar(표시 이름): None---

## 195 (10-9): --sleep-requests
- short: []
- long: ['--sleep-requests']
- dest(저장변수명): sleep_interval_requests
- default: ('NO', 'DEFAULT')
- type: float
- choices: None
- help: Number of seconds to sleep between requests during data extraction
- metavar(표시 이름): SECONDS---

## 196 (10-10): --sleep-interval/--min-sleep-interval
- short: []
- long: ['--sleep-interval', '--min-sleep-interval']
- dest(저장변수명): sleep_interval
- default: ('NO', 'DEFAULT')
- type: float
- choices: None
- help: Number of seconds to sleep before each download. This is the minimum time to sleep when used along with --max-sleep-interval (Alias: --min-sleep-interval)
- metavar(표시 이름): SECONDS---

## 197 (10-11): --max-sleep-interval
- short: []
- long: ['--max-sleep-interval']
- dest(저장변수명): max_sleep_interval
- default: ('NO', 'DEFAULT')
- type: float
- choices: None
- help: Maximum number of seconds to sleep. Can only be used along with --min-sleep-interval
- metavar(표시 이름): SECONDS---

## 198 (10-12): --sleep-subtitles
- short: []
- long: ['--sleep-subtitles']
- dest(저장변수명): sleep_interval_subtitles
- default: 0
- type: float
- choices: None
- help: Number of seconds to sleep before each subtitle download
- metavar(표시 이름): SECONDS---

# 11. Video Format Options: 21개 옵션
## 199 (11-1): -f/--format
- short: ['-f']
- long: ['--format']
- dest(저장변수명): format
- default: None
- type: string
- choices: None
- help: Video format code, see "FORMAT SELECTION" for more details
- metavar(표시 이름): FORMAT---

## 200 (11-2): -S/--format-sort
- short: ['-S']
- long: ['--format-sort']
- dest(저장변수명): format_sort
- default: []
- type: string
- choices: None
- help: Sort the formats by the fields given, see "Sorting Formats" for more details
- metavar(표시 이름): SORTORDER---

## 201 (11-3): --format-sort-reset
- short: []
- long: ['--format-sort-reset']
- dest(저장변수명): format_sort
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Disregard previous user specified sort order and reset to the default
- metavar(표시 이름): None---

## 202 (11-4): --format-sort-force/--S-force
- short: []
- long: ['--format-sort-force', '--S-force']
- dest(저장변수명): format_sort_force
- default: False
- type: None
- choices: None
- help: Force user specified sort order to have precedence over all fields, see "Sorting Formats" for more details (Alias: --S-force)
- metavar(표시 이름): FORMAT---

## 203 (11-5): --no-format-sort-force
- short: []
- long: ['--no-format-sort-force']
- dest(저장변수명): format_sort_force
- default: False
- type: None
- choices: None
- help: Some fields have precedence over the user specified sort order (default)
- metavar(표시 이름): FORMAT---

## 204 (11-6): --video-multistreams
- short: []
- long: ['--video-multistreams']
- dest(저장변수명): allow_multiple_video_streams
- default: None
- type: None
- choices: None
- help: Allow multiple video streams to be merged into a single file
- metavar(표시 이름): None---

## 205 (11-7): --no-video-multistreams
- short: []
- long: ['--no-video-multistreams']
- dest(저장변수명): allow_multiple_video_streams
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Only one video stream is downloaded for each output file (default)
- metavar(표시 이름): None---

## 206 (11-8): --audio-multistreams
- short: []
- long: ['--audio-multistreams']
- dest(저장변수명): allow_multiple_audio_streams
- default: None
- type: None
- choices: None
- help: Allow multiple audio streams to be merged into a single file
- metavar(표시 이름): None---

## 207 (11-9): --no-audio-multistreams
- short: []
- long: ['--no-audio-multistreams']
- dest(저장변수명): allow_multiple_audio_streams
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Only one audio stream is downloaded for each output file (default)
- metavar(표시 이름): None---

## 208 (11-10): --all-formats
- short: []
- long: ['--all-formats']
- dest(저장변수명): format
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 209 (11-11): --prefer-free-formats
- short: []
- long: ['--prefer-free-formats']
- dest(저장변수명): prefer_free_formats
- default: False
- type: None
- choices: None
- help: Prefer video formats with free containers over non-free ones of the same quality. Use with "-S ext" to strictly prefer free containers irrespective of quality
- metavar(표시 이름): None---

## 210 (11-12): --no-prefer-free-formats
- short: []
- long: ['--no-prefer-free-formats']
- dest(저장변수명): prefer_free_formats
- default: False
- type: None
- choices: None
- help: Don't give any special preference to free containers (default)
- metavar(표시 이름): None---

## 211 (11-13): --check-formats
- short: []
- long: ['--check-formats']
- dest(저장변수명): check_formats
- default: None
- type: None
- choices: None
- help: Make sure formats are selected only from those that are actually downloadable
- metavar(표시 이름): None---

## 212 (11-14): --check-all-formats
- short: []
- long: ['--check-all-formats']
- dest(저장변수명): check_formats
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Check all formats for whether they are actually downloadable
- metavar(표시 이름): None---

## 213 (11-15): --no-check-formats
- short: []
- long: ['--no-check-formats']
- dest(저장변수명): check_formats
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not check that the formats are actually downloadable
- metavar(표시 이름): None---

## 214 (11-16): -F/--list-formats
- short: ['-F']
- long: ['--list-formats']
- dest(저장변수명): listformats
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: List available formats of each video. Simulate unless --no-simulate is used
- metavar(표시 이름): None---

## 215 (11-17): --list-formats-as-table
- short: []
- long: ['--list-formats-as-table']
- dest(저장변수명): listformats_table
- default: True
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 216 (11-18): --list-formats-old/--no-list-formats-as-table
- short: []
- long: ['--list-formats-old', '--no-list-formats-as-table']
- dest(저장변수명): listformats_table
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 217 (11-19): --merge-output-format
- short: []
- long: ['--merge-output-format']
- dest(저장변수명): merge_output_format
- default: None
- type: string
- choices: None
- help: Containers that may be used when merging formats, separated by "/", e.g. "mp4/mkv". Ignored if no merge is required. (currently supported: avi, flv, mkv, mov, mp4, webm)
- metavar(표시 이름): FORMAT---

## 218 (11-20): --allow-unplayable-formats
- short: []
- long: ['--allow-unplayable-formats']
- dest(저장변수명): allow_unplayable_formats
- default: False
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 219 (11-21): --no-allow-unplayable-formats
- short: []
- long: ['--no-allow-unplayable-formats']
- dest(저장변수명): allow_unplayable_formats
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

# 12. Subtitle Options: 8개 옵션
## 220 (12-1): --write-subs/--write-srt
- short: []
- long: ['--write-subs', '--write-srt']
- dest(저장변수명): writesubtitles
- default: False
- type: None
- choices: None
- help: Write subtitle file
- metavar(표시 이름): None---

## 221 (12-2): --no-write-subs/--no-write-srt
- short: []
- long: ['--no-write-subs', '--no-write-srt']
- dest(저장변수명): writesubtitles
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not write subtitle file (default)
- metavar(표시 이름): None---

## 222 (12-3): --write-auto-subs/--write-automatic-subs
- short: []
- long: ['--write-auto-subs', '--write-automatic-subs']
- dest(저장변수명): writeautomaticsub
- default: False
- type: None
- choices: None
- help: Write automatically generated subtitle file (Alias: --write-automatic-subs)
- metavar(표시 이름): None---

## 223 (12-4): --no-write-auto-subs/--no-write-automatic-subs
- short: []
- long: ['--no-write-auto-subs', '--no-write-automatic-subs']
- dest(저장변수명): writeautomaticsub
- default: False
- type: None
- choices: None
- help: Do not write auto-generated subtitles (default) (Alias: --no-write-automatic-subs)
- metavar(표시 이름): None---

## 224 (12-5): --all-subs
- short: []
- long: ['--all-subs']
- dest(저장변수명): allsubtitles
- default: False
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 225 (12-6): --list-subs
- short: []
- long: ['--list-subs']
- dest(저장변수명): listsubtitles
- default: False
- type: None
- choices: None
- help: List available subtitles of each video. Simulate unless --no-simulate is used
- metavar(표시 이름): None---

## 226 (12-7): --sub-format
- short: []
- long: ['--sub-format']
- dest(저장변수명): subtitlesformat
- default: best
- type: string
- choices: None
- help: Subtitle format; accepts formats preference separated by "/", e.g. "srt" or "ass/srt/best"
- metavar(표시 이름): FORMAT---

## 227 (12-8): --sub-langs/--srt-langs
- short: []
- long: ['--sub-langs', '--srt-langs']
- dest(저장변수명): subtitleslangs
- default: []
- type: string
- choices: None
- help: Languages of the subtitles to download (can be regex) or "all" separated by commas, e.g. --sub-langs "en.*,ja" (where "en.*" is a regex pattern that matches "en" followed by 0 or more of any character). You can prefix the language code with a "-" to exclude it from the requested languages, e.g. --sub-langs all,-live_chat. Use --list-subs for a list of available language tags
- metavar(표시 이름): LANGS---

# 13. Authentication Options: 14개 옵션
## 228 (13-1): -u/--username
- short: ['-u']
- long: ['--username']
- dest(저장변수명): username
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Login with this account ID
- metavar(표시 이름): USERNAME---

## 229 (13-2): -p/--password
- short: ['-p']
- long: ['--password']
- dest(저장변수명): password
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Account password. If this option is left out, yt-dlp will ask interactively
- metavar(표시 이름): PASSWORD---

## 230 (13-3): -2/--twofactor
- short: ['-2']
- long: ['--twofactor']
- dest(저장변수명): twofactor
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Two-factor authentication code
- metavar(표시 이름): TWOFACTOR---

## 231 (13-4): -n/--netrc
- short: ['-n']
- long: ['--netrc']
- dest(저장변수명): usenetrc
- default: False
- type: None
- choices: None
- help: Use .netrc authentication data
- metavar(표시 이름): None---

## 232 (13-5): --netrc-location
- short: []
- long: ['--netrc-location']
- dest(저장변수명): netrc_location
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Location of .netrc authentication data; either the path or its containing directory. Defaults to ~/.netrc
- metavar(표시 이름): PATH---

## 233 (13-6): --netrc-cmd
- short: []
- long: ['--netrc-cmd']
- dest(저장변수명): netrc_cmd
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Command to execute to get the credentials for an extractor.
- metavar(표시 이름): NETRC_CMD---

## 234 (13-7): --video-password
- short: []
- long: ['--video-password']
- dest(저장변수명): videopassword
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Video-specific password
- metavar(표시 이름): PASSWORD---

## 235 (13-8): --ap-mso
- short: []
- long: ['--ap-mso']
- dest(저장변수명): ap_mso
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Adobe Pass multiple-system operator (TV provider) identifier, use --ap-list-mso for a list of available MSOs
- metavar(표시 이름): MSO---

## 236 (13-9): --ap-username
- short: []
- long: ['--ap-username']
- dest(저장변수명): ap_username
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Multiple-system operator account login
- metavar(표시 이름): USERNAME---

## 237 (13-10): --ap-password
- short: []
- long: ['--ap-password']
- dest(저장변수명): ap_password
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Multiple-system operator account password. If this option is left out, yt-dlp will ask interactively
- metavar(표시 이름): PASSWORD---

## 238 (13-11): --ap-list-mso
- short: []
- long: ['--ap-list-mso']
- dest(저장변수명): ap_list_mso
- default: False
- type: None
- choices: None
- help: List all supported multiple-system operators
- metavar(표시 이름): None---

## 239 (13-12): --client-certificate
- short: []
- long: ['--client-certificate']
- dest(저장변수명): client_certificate
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Path to client certificate file in PEM format. May include the private key
- metavar(표시 이름): CERTFILE---

## 240 (13-13): --client-certificate-key
- short: []
- long: ['--client-certificate-key']
- dest(저장변수명): client_certificate_key
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Path to private key file for client certificate
- metavar(표시 이름): KEYFILE---

## 241 (13-14): --client-certificate-password
- short: []
- long: ['--client-certificate-password']
- dest(저장변수명): client_certificate_password
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Password for client certificate private key, if encrypted. If not provided, and the key is encrypted, yt-dlp will ask interactively
- metavar(표시 이름): PASSWORD---

# 14. Post-Processing Options: 40개 옵션
## 242 (14-1): -x/--extract-audio
- short: ['-x']
- long: ['--extract-audio']
- dest(저장변수명): extractaudio
- default: False
- type: None
- choices: None
- help: Convert video files to audio-only files (requires ffmpeg and ffprobe)
- metavar(표시 이름): None---

## 243 (14-2): --audio-format
- short: []
- long: ['--audio-format']
- dest(저장변수명): audioformat
- default: best
- type: string
- choices: None
- help: Format to convert the audio to when -x is used. (currently supported: best (default), aac, alac, flac, m4a, mp3, opus, vorbis, wav). You can specify multiple rules using similar syntax as --remux-video
- metavar(표시 이름): FORMAT---

## 244 (14-3): --audio-quality
- short: []
- long: ['--audio-quality']
- dest(저장변수명): audioquality
- default: 5
- type: string
- choices: None
- help: Specify ffmpeg audio quality to use when converting the audio with -x. Insert a value between 0 (best) and 10 (worst) for VBR or a specific bitrate like 128K (default %default)
- metavar(표시 이름): QUALITY---

## 245 (14-4): --remux-video
- short: []
- long: ['--remux-video']
- dest(저장변수명): remuxvideo
- default: None
- type: string
- choices: None
- help: Remux the video into another container if necessary (currently supported: avi, flv, gif, mkv, mov, mp4, webm, aac, aiff, alac, flac, m4a, mka, mp3, ogg, opus, vorbis, wav). If the target container does not support the video/audio codec, remuxing will fail. You can specify multiple rules; e.g. "aac>m4a/mov>mp4/mkv" will remux aac to m4a, mov to mp4 and anything else to mkv
- metavar(표시 이름): FORMAT---

## 246 (14-5): --recode-video
- short: []
- long: ['--recode-video']
- dest(저장변수명): recodevideo
- default: None
- type: string
- choices: None
- help: Re-encode the video into another format if necessary. The syntax and supported formats are the same as --remux-video
- metavar(표시 이름): FORMAT---

## 247 (14-6): --postprocessor-args/--ppa
- short: []
- long: ['--postprocessor-args', '--ppa']
- dest(저장변수명): postprocessor_args
- default: {}
- type: string
- choices: None
- help: Give these arguments to the postprocessors. Specify the postprocessor/executable name and the arguments separated by a colon ":" to give the argument to the specified postprocessor/executable. Supported PP are: Merger, ModifyChapters, SplitChapters, ExtractAudio, VideoRemuxer, VideoConvertor, Metadata, EmbedSubtitle, EmbedThumbnail, SubtitlesConvertor, ThumbnailsConvertor, FixupStretched, FixupM4a, FixupM3u8, FixupTimestamp and FixupDuration. The supported executables are: AtomicParsley, FFmpeg and FFprobe. You can also specify "PP+EXE:ARGS" to give the arguments to the specified executable only when being used by the specified postprocessor. Additionally, for ffmpeg/ffprobe, "_i"/"_o" can be appended to the prefix optionally followed by a number to pass the argument before the specified input/output file, e.g. --ppa "Merger+ffmpeg_i1:-v quiet". You can use this option multiple times to give different arguments to different postprocessors. (Alias: --ppa)
- metavar(표시 이름): NAME:ARGS---

## 248 (14-7): -k/--keep-video
- short: ['-k']
- long: ['--keep-video']
- dest(저장변수명): keepvideo
- default: False
- type: None
- choices: None
- help: Keep the intermediate video file on disk after post-processing
- metavar(표시 이름): None---

## 249 (14-8): --no-keep-video
- short: []
- long: ['--no-keep-video']
- dest(저장변수명): keepvideo
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Delete the intermediate video file after post-processing (default)
- metavar(표시 이름): None---

## 250 (14-9): --post-overwrites
- short: []
- long: ['--post-overwrites']
- dest(저장변수명): nopostoverwrites
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Overwrite post-processed files (default)
- metavar(표시 이름): None---

## 251 (14-10): --no-post-overwrites
- short: []
- long: ['--no-post-overwrites']
- dest(저장변수명): nopostoverwrites
- default: False
- type: None
- choices: None
- help: Do not overwrite post-processed files
- metavar(표시 이름): None---

## 252 (14-11): --embed-subs
- short: []
- long: ['--embed-subs']
- dest(저장변수명): embedsubtitles
- default: False
- type: None
- choices: None
- help: Embed subtitles in the video (only for mp4, webm and mkv videos)
- metavar(표시 이름): None---

## 253 (14-12): --no-embed-subs
- short: []
- long: ['--no-embed-subs']
- dest(저장변수명): embedsubtitles
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not embed subtitles (default)
- metavar(표시 이름): None---

## 254 (14-13): --embed-thumbnail
- short: []
- long: ['--embed-thumbnail']
- dest(저장변수명): embedthumbnail
- default: False
- type: None
- choices: None
- help: Embed thumbnail in the video as cover art
- metavar(표시 이름): None---

## 255 (14-14): --no-embed-thumbnail
- short: []
- long: ['--no-embed-thumbnail']
- dest(저장변수명): embedthumbnail
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not embed thumbnail (default)
- metavar(표시 이름): None---

## 256 (14-15): --embed-metadata/--add-metadata
- short: []
- long: ['--embed-metadata', '--add-metadata']
- dest(저장변수명): addmetadata
- default: False
- type: None
- choices: None
- help: Embed metadata to the video file. Also embeds chapters/infojson if present unless --no-embed-chapters/--no-embed-info-json are used (Alias: --add-metadata)
- metavar(표시 이름): None---

## 257 (14-16): --no-embed-metadata/--no-add-metadata
- short: []
- long: ['--no-embed-metadata', '--no-add-metadata']
- dest(저장변수명): addmetadata
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not add metadata to file (default) (Alias: --no-add-metadata)
- metavar(표시 이름): None---

## 258 (14-17): --embed-chapters/--add-chapters
- short: []
- long: ['--embed-chapters', '--add-chapters']
- dest(저장변수명): addchapters
- default: None
- type: None
- choices: None
- help: Add chapter markers to the video file (Alias: --add-chapters)
- metavar(표시 이름): None---

## 259 (14-18): --no-embed-chapters/--no-add-chapters
- short: []
- long: ['--no-embed-chapters', '--no-add-chapters']
- dest(저장변수명): addchapters
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not add chapter markers (default) (Alias: --no-add-chapters)
- metavar(표시 이름): None---

## 260 (14-19): --embed-info-json
- short: []
- long: ['--embed-info-json']
- dest(저장변수명): embed_infojson
- default: None
- type: None
- choices: None
- help: Embed the infojson as an attachment to mkv/mka video files
- metavar(표시 이름): None---

## 261 (14-20): --no-embed-info-json
- short: []
- long: ['--no-embed-info-json']
- dest(저장변수명): embed_infojson
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not embed the infojson as an attachment to the video file
- metavar(표시 이름): None---

## 262 (14-21): --metadata-from-title
- short: []
- long: ['--metadata-from-title']
- dest(저장변수명): metafromtitle
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): FORMAT---

## 263 (14-22): --parse-metadata
- short: []
- long: ['--parse-metadata']
- dest(저장변수명): parse_metadata
- default: {}
- type: string
- choices: None
- help: Parse additional metadata like title/artist from other fields; see "MODIFYING METADATA" for details. Supported values of "WHEN" are the same as that of --use-postprocessor (default: pre_process)
- metavar(표시 이름): [WHEN:]FROM:TO---

## 264 (14-23): --replace-in-metadata
- short: []
- long: ['--replace-in-metadata']
- dest(저장변수명): parse_metadata
- default: {}
- type: string
- choices: None
- help: Replace text in a metadata field using the given regex. This option can be used multiple times. Supported values of "WHEN" are the same as that of --use-postprocessor (default: pre_process)
- metavar(표시 이름): [WHEN:]FIELDS REGEX REPLACE---

## 265 (14-24): --xattrs/--xattr
- short: []
- long: ['--xattrs', '--xattr']
- dest(저장변수명): xattrs
- default: False
- type: None
- choices: None
- help: Write metadata to the video file's xattrs (using Dublin Core and XDG standards)
- metavar(표시 이름): None---

## 266 (14-25): --concat-playlist
- short: []
- long: ['--concat-playlist']
- dest(저장변수명): concat_playlist
- default: multi_video
- type: choice
- choices: ('never', 'always', 'multi_video')
- help: Concatenate videos in a playlist. One of "never", "always", or "multi_video" (default; only when the videos form a single show). All the video files must have the same codecs and number of streams to be concatenable. The "pl_video:" prefix can be used with "--paths" and "--output" to set the output filename for the concatenated files. See "OUTPUT TEMPLATE" for details
- metavar(표시 이름): POLICY---

## 267 (14-26): --fixup
- short: []
- long: ['--fixup']
- dest(저장변수명): fixup
- default: None
- type: choice
- choices: ('never', 'ignore', 'warn', 'detect_or_warn', 'force')
- help: Automatically correct known faults of the file. One of never (do nothing), warn (only emit a warning), detect_or_warn (the default; fix the file if we can, warn otherwise), force (try fixing even if the file already exists)
- metavar(표시 이름): POLICY---

## 268 (14-27): --ffmpeg-location
- short: []
- long: ['--ffmpeg-location']
- dest(저장변수명): ffmpeg_location
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Location of the ffmpeg binary; either the path to the binary or its containing directory
- metavar(표시 이름): PATH---

## 269 (14-28): --exec
- short: []
- long: ['--exec']
- dest(저장변수명): exec_cmd
- default: {}
- type: string
- choices: None
- help: Execute a command, optionally prefixed with when to execute it, separated by a ":". Supported values of "WHEN" are the same as that of --use-postprocessor (default: after_move). The same syntax as the output template can be used to pass any field as arguments to the command. If no fields are passed, %(filepath,_filename|)q is appended to the end of the command. This option can be used multiple times
- metavar(표시 이름): [WHEN:]CMD---

## 270 (14-29): --no-exec
- short: []
- long: ['--no-exec']
- dest(저장변수명): exec_cmd
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Remove any previously defined --exec
- metavar(표시 이름): None---

## 271 (14-30): --exec-before-download
- short: []
- long: ['--exec-before-download']
- dest(저장변수명): exec_before_dl_cmd
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): CMD---

## 272 (14-31): --no-exec-before-download
- short: []
- long: ['--no-exec-before-download']
- dest(저장변수명): exec_before_dl_cmd
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: SUPPRESSHELP
- metavar(표시 이름): None---

## 273 (14-32): --convert-subs/--convert-sub/--convert-subtitles
- short: []
- long: ['--convert-subs', '--convert-sub', '--convert-subtitles']
- dest(저장변수명): convertsubtitles
- default: None
- type: string
- choices: None
- help: Convert the subtitles to another format (currently supported: ass, lrc, srt, vtt). Use "--convert-subs none" to disable conversion (default) (Alias: --convert-subtitles)
- metavar(표시 이름): FORMAT---

## 274 (14-33): --convert-thumbnails
- short: []
- long: ['--convert-thumbnails']
- dest(저장변수명): convertthumbnails
- default: None
- type: string
- choices: None
- help: Convert the thumbnails to another format (currently supported: jpg, png, webp). You can specify multiple rules using similar syntax as "--remux-video". Use "--convert-thumbnails none" to disable conversion (default)
- metavar(표시 이름): FORMAT---

## 275 (14-34): --split-chapters/--split-tracks
- short: []
- long: ['--split-chapters', '--split-tracks']
- dest(저장변수명): split_chapters
- default: False
- type: None
- choices: None
- help: Split video into multiple files based on internal chapters. The "chapter:" prefix can be used with "--paths" and "--output" to set the output filename for the split files. See "OUTPUT TEMPLATE" for details
- metavar(표시 이름): None---

## 276 (14-35): --no-split-chapters/--no-split-tracks
- short: []
- long: ['--no-split-chapters', '--no-split-tracks']
- dest(저장변수명): split_chapters
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not split video based on chapters (default)
- metavar(표시 이름): None---

## 277 (14-36): --remove-chapters
- short: []
- long: ['--remove-chapters']
- dest(저장변수명): remove_chapters
- default: ('NO', 'DEFAULT')
- type: string
- choices: None
- help: Remove chapters whose title matches the given regular expression. The syntax is the same as --download-sections. This option can be used multiple times
- metavar(표시 이름): REGEX---

## 278 (14-37): --no-remove-chapters
- short: []
- long: ['--no-remove-chapters']
- dest(저장변수명): remove_chapters
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not remove any chapters from the file (default)
- metavar(표시 이름): None---

## 279 (14-38): --force-keyframes-at-cuts
- short: []
- long: ['--force-keyframes-at-cuts']
- dest(저장변수명): force_keyframes_at_cuts
- default: False
- type: None
- choices: None
- help: Force keyframes at cuts when downloading/splitting/removing sections. This is slow due to needing a re-encode, but the resulting video may have fewer artifacts around the cuts
- metavar(표시 이름): None---

## 280 (14-39): --no-force-keyframes-at-cuts
- short: []
- long: ['--no-force-keyframes-at-cuts']
- dest(저장변수명): force_keyframes_at_cuts
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not force keyframes around the chapters when cutting/splitting (default)
- metavar(표시 이름): None---

## 281 (14-40): --use-postprocessor
- short: []
- long: ['--use-postprocessor']
- dest(저장변수명): add_postprocessors
- default: []
- type: string
- choices: None
- help: The (case-sensitive) name of plugin postprocessors to be enabled, and (optionally) arguments to be passed to it, separated by a colon ":". ARGS are a semicolon ";" delimited list of NAME=VALUE. The "when" argument determines when the postprocessor is invoked. It can be one of "pre_process" (after video extraction), "after_filter" (after video passes filter), "video" (after --format; before --print/--output), "before_dl" (before each video download), "post_process" (after each video download; default), "after_move" (after moving the video file to its final location), "after_video" (after downloading and processing all formats of a video), or "playlist" (at end of playlist). This option can be used multiple times to add different postprocessors
- metavar(표시 이름): NAME[:ARGS]---

# 15. SponsorBlock Options: 5개 옵션
## 282 (15-1): --sponsorblock-mark
- short: []
- long: ['--sponsorblock-mark']
- dest(저장변수명): sponsorblock_mark
- default: set()
- type: string
- choices: None
- help: SponsorBlock categories to create chapters for, separated by commas. Available categories are sponsor, intro, outro, selfpromo, preview, filler, interaction, music_offtopic, hook, poi_highlight, chapter, all and default (=all). You can prefix the category with a "-" to exclude it. See [1] for descriptions of the categories. E.g. --sponsorblock-mark all,-preview [1] https://wiki.sponsor.ajay.app/w/Segment_Categories
- metavar(표시 이름): CATS---

## 283 (15-2): --sponsorblock-remove
- short: []
- long: ['--sponsorblock-remove']
- dest(저장변수명): sponsorblock_remove
- default: set()
- type: string
- choices: None
- help: SponsorBlock categories to be removed from the video file, separated by commas. If a category is present in both mark and remove, remove takes precedence. The syntax and available categories are the same as for --sponsorblock-mark except that "default" refers to "all,-filler" and poi_highlight, chapter are not available
- metavar(표시 이름): CATS---

## 284 (15-3): --sponsorblock-chapter-title
- short: []
- long: ['--sponsorblock-chapter-title']
- dest(저장변수명): sponsorblock_chapter_title
- default: [SponsorBlock]: %(category_names)l
- type: string
- choices: None
- help: An output template for the title of the SponsorBlock chapters created by --sponsorblock-mark. The only available fields are start_time, end_time, category, categories, name, category_names. Defaults to "%default"
- metavar(표시 이름): TEMPLATE---

## 285 (15-4): --no-sponsorblock
- short: []
- long: ['--no-sponsorblock']
- dest(저장변수명): no_sponsorblock
- default: False
- type: None
- choices: None
- help: Disable both --sponsorblock-mark and --sponsorblock-remove
- metavar(표시 이름): None---

## 286 (15-5): --sponsorblock-api
- short: []
- long: ['--sponsorblock-api']
- dest(저장변수명): sponsorblock_api
- default: https://sponsor.ajay.app
- type: string
- choices: None
- help: SponsorBlock API location, defaults to %default
- metavar(표시 이름): URL---

# 16. Extractor Options: 6개 옵션
## 287 (16-1): --extractor-retries
- short: []
- long: ['--extractor-retries']
- dest(저장변수명): extractor_retries
- default: 3
- type: string
- choices: None
- help: Number of retries for known extractor errors (default is %default), or "infinite"
- metavar(표시 이름): RETRIES---

## 288 (16-2): --allow-dynamic-mpd/--no-ignore-dynamic-mpd
- short: []
- long: ['--allow-dynamic-mpd', '--no-ignore-dynamic-mpd']
- dest(저장변수명): dynamic_mpd
- default: True
- type: None
- choices: None
- help: Process dynamic DASH manifests (default) (Alias: --no-ignore-dynamic-mpd)
- metavar(표시 이름): None---

## 289 (16-3): --ignore-dynamic-mpd/--no-allow-dynamic-mpd
- short: []
- long: ['--ignore-dynamic-mpd', '--no-allow-dynamic-mpd']
- dest(저장변수명): dynamic_mpd
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not process dynamic DASH manifests (Alias: --no-allow-dynamic-mpd)
- metavar(표시 이름): None---

## 290 (16-4): --hls-split-discontinuity
- short: []
- long: ['--hls-split-discontinuity']
- dest(저장변수명): hls_split_discontinuity
- default: False
- type: None
- choices: None
- help: Split HLS playlists to different formats at discontinuities such as ad breaks
- metavar(표시 이름): None---

## 291 (16-5): --no-hls-split-discontinuity
- short: []
- long: ['--no-hls-split-discontinuity']
- dest(저장변수명): hls_split_discontinuity
- default: ('NO', 'DEFAULT')
- type: None
- choices: None
- help: Do not split HLS playlists into different formats at discontinuities such as ad breaks (default)
- metavar(표시 이름): None---

## 292 (16-6): --extractor-args
- short: []
- long: ['--extractor-args']
- dest(저장변수명): extractor_args
- default: {}
- type: string
- choices: None
- help: Pass ARGS arguments to the IE_KEY extractor. See "EXTRACTOR ARGUMENTS" for details. You can use this option multiple times to give arguments for different extractors
- metavar(표시 이름): IE_KEY:ARGS---

