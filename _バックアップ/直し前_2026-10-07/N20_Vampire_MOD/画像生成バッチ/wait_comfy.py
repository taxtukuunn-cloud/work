import urllib.request, time, sys
t = time.time()
while time.time() - t < 300:
    try:
        urllib.request.urlopen("http://127.0.0.1:8188/system_stats", timeout=3); sys.exit(0)
    except Exception:
        time.sleep(3)
sys.exit(1)
