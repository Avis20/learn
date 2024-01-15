#!/usr/bin/env perl

use uni::perl       qw| :dumper |;
use Date::Parse     qw| str2time |;

my $date = "2023-09-26";
my $date = "1695675600";

warn str2time($date);

exit;