import logging
import random
import tempfile
import unittest

from PIL import Image

import profileimageutil

logger = logging.getLogger('tests')


class TestImageGenerator(unittest.TestCase):

    def test_image_generation(self):
        test_size = (random.choice(((100, 100), (200, 200), (300, 300))))
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
            profileimageutil.generate_image("Test", temp_file, width=test_size[0], height=test_size[1])
            logger.debug("Written to file", temp_file.name)
            im = Image.open(temp_file.name)
            self.assertTupleEqual(test_size, im.size, "Image sizes don't match")

if __name__ == '__main__':
    unittest.main()
