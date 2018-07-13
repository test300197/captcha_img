use Image::OCR::Tesseract 'get_ocr';

my $image = './clean-img.jpg';

my $text = get_ocr($image);

print $text;
