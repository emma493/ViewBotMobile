[app]
title = ViewBot Mobile
package.name = viewbotmobile
package.domain = org.viewbot
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,requests,fake-useragent,urllib3,chardet,idna
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.1.0
fullscreen = 0
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 28
android.minapi = 21
android.ndk = 23b
p4a.branch = master
android.arch = armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1