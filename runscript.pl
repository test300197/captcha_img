use strict;
use utf8;
use open ':std', ':encoding(UTF-8)';

my $name_img = 'clean-img.jpg';
my $name_out = 'text';
my $text_out;
my $cmd = 'tesseract ' . $name_img . ' '. $name_out . ' -l rus';

system($cmd);

my $filename = $name_out .'.txt';
if (open(my $text, '<:encoding(UTF-8)', $filename)) {
  my $row = <$text>;
  $text_out = $row;
  close($text);
}

print $text_out;
