import requests
import json




auth_token = '' # Your API Key
url = "https://dolphin-anty-api.com/browser_profiles"


payload = {
  "name": "browser",
  "browserType": "anty",
  "tags": [],
  "tabs": [],
  "platform": "windows",
  "platformVersion": "10.0.0",
  "mainWebsite": "google",
  "useragent": {
    "mode": "manual",
    "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
  },
  "webrtc": {
    "mode": "altered"
  },
  "canvas": {
    "mode": "real"
  },
  "webgl": {
    "mode": "real"
  },
  "webglInfo": {
    "mode": "manual",
    "vendor": "Intel Inc.",
    "renderer": "Intel Iris Pro 5200",
    "webgl2Maximum": {
      "MAX_SAMPLES": 8,
      "MAX_DRAW_BUFFERS": 8,
      "MAX_TEXTURE_SIZE": 16384,
      "MAX_ELEMENT_INDEX": 4294967294,
      "MAX_VIEWPORT_DIMS": [16384, 16384],
      "MAX_VERTEX_ATTRIBS": 16,
      "MAX_3D_TEXTURE_SIZE": 2048,
      "MAX_VARYING_VECTORS": 30,
      "MAX_ELEMENTS_INDICES": 2147483647,
      "MAX_TEXTURE_LOD_BIAS": 15,
      "MAX_COLOR_ATTACHMENTS": 8,
      "MAX_ELEMENTS_VERTICES": 2147483647,
      "MAX_RENDERBUFFER_SIZE": 16384,
      "MAX_UNIFORM_BLOCK_SIZE": 65536,
      "MAX_VARYING_COMPONENTS": 120,
      "MAX_TEXTURE_IMAGE_UNITS": 32,
      "MAX_ARRAY_TEXTURE_LAYERS": 2048,
      "MAX_PROGRAM_TEXEL_OFFSET": 7,
      "MIN_PROGRAM_TEXEL_OFFSET": -8,
      "MAX_CUBE_MAP_TEXTURE_SIZE": 16384,
      "MAX_VERTEX_UNIFORM_BLOCKS": 13,
      "MAX_VERTEX_UNIFORM_VECTORS": 4096,
      "MAX_COMBINED_UNIFORM_BLOCKS": 60,
      "MAX_FRAGMENT_UNIFORM_BLOCKS": 13,
      "MAX_UNIFORM_BUFFER_BINDINGS": 72,
      "MAX_FRAGMENT_UNIFORM_VECTORS": 4096,
      "MAX_VERTEX_OUTPUT_COMPONENTS": 124,
      "MAX_FRAGMENT_INPUT_COMPONENTS": 124,
      "MAX_VERTEX_UNIFORM_COMPONENTS": 16384,
      "MAX_VERTEX_TEXTURE_IMAGE_UNITS": 32,
      "MAX_FRAGMENT_UNIFORM_COMPONENTS": 16384,
      "UNIFORM_BUFFER_OFFSET_ALIGNMENT": 256,
      "MAX_COMBINED_TEXTURE_IMAGE_UNITS": 64,
      "MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS": 229376,
      "MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS": 4,
      "MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS": 229376,
      "MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS": 4,
      "MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS": 128
    }
  }
}


payload_json = json.dumps(payload)

headers = {
  'Content-Type': 'application/json',
   'Authorization': 'Bearer ' + auth_token

}

response = requests.request("POST", url, headers=headers, data=payload_json)

print(response.text)


if response.status_code == 200:
    
    # If profile created successfully, update profile to create a new digital footprint.
    browser_profile_id = browser_profile_id = json.loads(response.text).get("browserProfileId")

    url = f"https://dolphin-anty-api.com/browser_profiles/{browser_profile_id}"

    updated_payload = {
        "name": "Browser",
        "canvas": {"mode": "real"},
        "webgl": {"mode": "real"},
        "webglInfo": {
            "mode": "software"
        },
        "timezone": {
            "mode": "auto"
        },
        "locale": {
            "mode": "manual",
            "value": "tr_TR"
        },
        "geolocation": {
            "mode": "real"
        },
        "cpu": {
            "mode": "real"
        },
        "memory": {
            "mode": "real"
        }
    }

    updated_payload_json = json.dumps(updated_payload)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + auth_token
    }

    response = requests.patch(url, headers=headers, data=updated_payload_json)

    if response.status_code == 200:
        print("Profile updated successfully.")
    else:
        print("Profile wasn't be able to update.")
else:
    print("Profile isn't created.")

