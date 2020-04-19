#!/usr/bin/env perl

use uni::perl       qw| :dumper |;

use Image::Magick;

my $image = Image::Magick->new( format => 'pdf' );
$image->Read('pdf:source/Lorem.pdf[1]');
$image->Set( verbose => 'True' );
$image->Set( 'density' => '300',  );

my $blur = 9.999;
my $width = 2481;
my $original_width = $image->Get('width');
my $original_height = $image->Get('height');
my $aspect_ratio = $original_width/$original_height;

$image->AdaptiveResize(blur => $blur, width => $width, height => $width / $aspect_ratio);

my $status = $image->Write( "pdf:res/Lorem.pdf" );
warn "Write failed: $status" if $status;

# system("identify ./res/Lorem.png");

=head

my $stamp = Image::Magick->new();
$stamp->Read('png:source/stamp.png');

$pdf->Composite( image => $stamp, compose => 'over' );
$pdf->Set( quality => 100 );

my $resized_width = 2048;
$pdf->Resize( geometry => $resized_width.'x'.$resized_width/2 );

$pdf->Write("pdf:res/Lorem.pdf");

