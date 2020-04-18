#!/usr/bin/env perl

use uni::perl       qw| :dumper |;

use Image::Magick;

use constant {
    DENSITY => 2000,
    QUALITY => '100%',
};

my $image = Image::Magick->new();
$image->Read('source/Lorem.pdf');

# $image->Set(density => DENSITY);
# $image->Set(quality => QUALITY);

my $resized_width = 2048;
$image->Resize(geometry => $resized_width.'x'.$resized_width/2);
warn "\n\n";
warn $image->get('density');
warn "\n\n";

my $filename = 'res/Lorem.png';

system("rm -rf res && mkdir res");
open my $fh, '>', $filename or die "Can't open $filename: $!";
$image->Write(file => \*$fh, filename => $filename);
close $fh;

system("identify $filename");

=head
$p->Read("imagefile");
$p->Set(attribute => value, ...)
($a, ...) = $p->Get("attribute", ...)
$p->routine(parameter => value, ...)
$p->Mogrify("Routine", parameter => value, ...)
$p->Write("filename");

