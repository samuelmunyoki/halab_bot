import json
import hashlib

class FingerprintSimulator:
    def __init__(self):
        # Simulate User-Agent and other browser/device properties
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
        self.platform = "Win64"
        self.languages = ["en-US"]
        self.screen_width = 1920
        self.screen_height = 1080
        self.avail_width = 1920
        self.avail_height = 1080
        self.precision = self.get_precision_info()
        self.canvas_supported = self.is_canvas_supported()
        self.webgl_supported = self.is_webgl_supported()
        self.ad_block = self.get_ad_block()

    # Simulate canvas support
    def is_canvas_supported(self):
        return True  # Simulate as if the browser supports canvas

    # Simulate WebGL support
    def is_webgl_supported(self):
        return True  # Simulate as if the browser supports WebGL

    # Simulate ad blocker detection
    def get_ad_block(self):
        return False  # Simulate as if there's no ad blocker

    # Simulate precision information
    def get_precision_info(self):
        return {
            "fragmentShader": {
                "high": {"precision": 16, "rangeMin": -32768, "rangeMax": 32767},
                "medium": {"precision": 8, "rangeMin": -128, "rangeMax": 127},
                "low": {"precision": 4, "rangeMin": -8, "rangeMax": 7}
            },
            "vertexShader": {
                "high": {"precision": 16, "rangeMin": -32768, "rangeMax": 32767},
                "medium": {"precision": 8, "rangeMin": -128, "rangeMax": 127},
                "low": {"precision": 4, "rangeMin": -8, "rangeMax": 7}
            }
        }

    # Generate a simple hash
    def hash_string(self, string):
        return hashlib.md5(string.encode('utf-8')).hexdigest()

    # Generate the fingerprint
    def generate_fingerprint(self):
        info = {
            "userAgent": self.user_agent,
            "platform": self.platform,
            "languages": self.languages,
            "screenWidth": self.screen_width,
            "screenHeight": self.screen_height,
            "availWidth": self.avail_width,
            "availHeight": self.avail_height,
            "precision": self.precision,
            "canvasSupported": self.canvas_supported,
            "webGLSupported": self.webgl_supported,
            "adBlock": self.ad_block
        }

        info_string = json.dumps(info, sort_keys=True)
        return self.hash_string(info_string)
