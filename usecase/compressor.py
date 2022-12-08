from PIL import Image


class CompressionEngine:

    def image_compression(filepath, filename, compression_ratio_value, verbose=False):
        try:
            print("Compression engine module")
            print("Image compression in progress...")
            picture = Image.open(filepath + "\\" + filename)
            picture.save(filepath + "Compressed_" + filename, "JPEG", optimize=True, quality=compression_ratio_value)
            print("Image compression done.\nCompressed image stored in the same location.")
            return
        except Exception as e:
            print("Exception occurred:", e)
