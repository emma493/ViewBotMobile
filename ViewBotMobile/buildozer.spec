[app]
title = ViewBot Mobile
package.name = viewbotmobile
package.domain = org.viewbot
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3, kivy==2.2.1, requests, fake-useragent
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# FIXED: Updated NDK and API versions
android.ndk_version = 25.2.9519653
android.sdk = 28
android.ndk_path = /opt/android-ndk
android.api = 28
android.minapi = 21

# Use newer toolchain
p4a.branch = develop
android.arch = armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
