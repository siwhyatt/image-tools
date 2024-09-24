import base64

sample_string = b"user2@gazegillorganics.co.uk:green2"

base64_string = base64.b64encode(sample_string)

print(f"Encoded string: {base64_string}")
